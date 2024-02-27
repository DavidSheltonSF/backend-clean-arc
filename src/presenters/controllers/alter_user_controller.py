from typing import Type
from src.main.interface import RouteInterface
from src.data.alter_user import AlterUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class AlterUserController(RouteInterface):
    """Class to define a controller to AlterUser use case"""

    def __init__(self, alter_user_use_case: Type[AlterUser]):
        self.alter_user_use_case = alter_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        # Check if there is a body in http_request
        if http_request.body:
            body_params = http_request.body.keys()

            required_params = ["user_name", "password"]
            checker = all(item in body_params for item in required_params)

            # check if user_id and user_id are in body_params
            if checker:

                user_id = http_request.view_arg["user_id"]
                user_name = http_request.body["user_name"]
                password = http_request.body["password"]

                response = self.alter_user_use_case.alter(
                    user_id=user_id, user_name=user_name, password=password
                )

            # In last case
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
