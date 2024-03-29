from typing import Type
from src.main.interface import RouteInterface
from src.data.register_user import RegisterUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class RegisterUserController(RouteInterface):
    """Class to define a controller to RegisterUser use case"""

    def __init__(self, register_user_use_case: Type[RegisterUser]):
        self.register_user_use_case = register_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        # Check if there is a body in http_request
        if http_request.body:

            body_params = http_request.body.keys()

            # Check if required user attributes  are in body_params
            if "user_name" in body_params and "password" in body_params:

                user_name = http_request.body["user_name"]
                password = http_request.body["password"]

                response = self.register_user_use_case.register(
                    user_name=user_name, password=password
                )
            else:
                response = {"Success": False, "Data": None}

            # If request failed, Unprocessable Entity
            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # Bad request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
