from typing import Type
from src.main.interface import RouteInterface
from src.data.remove_user import RemoveUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class RemoveUserController(RouteInterface):
    """Class to define a controller to RemoveUser use case"""

    def __init__(self, remove_user_use_case: Type[RemoveUser]):
        self.remove_user_use_case = remove_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        user_id = http_request.view_args["user_id"]

        response = self.remove_user_use_case.remove(user_id=user_id)

        # If request failed, Unprocessable Entity
        if response["Success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])
