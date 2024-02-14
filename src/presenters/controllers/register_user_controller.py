from typing import Type
from src.main.interface import RouteInterface
from src.data.register_user import RegisterUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class RegisterUserController(RouteInterface):
    """_summary_"""

    def __init__(self, register_user_use_case: Type[RegisterUser]):
        self.register_user_use_case = register_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """___"""

        response = None

        # Check if there is a body in http_request
        if http_request.body:

            body_params = http_request.body.keys()

            # Check required user data
            if "user_name" in body_params and "password" in body_params:

                user_name = http_request.body["user_name"]
                password = http_request.body["password"]

                response = self.register_user_use_case.register(
                    user_name=user_name, password=password
                )
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If there is no body
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
