from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import FindUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class FindUserController(RouteInterface):
    """Class to define a controller to FindUser use case"""

    def __init__(self, find_user_use_case: Type[FindUser]):
        """Constructor method

        Args:
            find_user_use_case (Type[FindUser]): _description_
            check_user (bool): If it is False, the controller
            will find user by id, name or both, if it is True,
            it will check if user is in database finding user by id.
        """
        self.find_user_use_case = find_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        # Check if there is a view_arg in http_request
        if http_request.view_arg:

            view_arg = http_request.view_arg.keys()

            # Check if user_id is in view_arg
            if "user_id" in view_arg:
                user_id = http_request.view_arg["user_id"]
                response = self.find_user_use_case.by_id(
                    user_id=user_id,
                )

            # Check if user_name is in view_arg
            elif "user_name" in view_arg:
                user_name = http_request.view_arg["user_name"]
                response = self.find_user_use_case.by_name(user_name=user_name)

            else:
                response = {"Success": False, "Data": None}

            # If the request failed
            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

        else:
            response = self.find_user_use_case.all()

        return HttpResponse(status_code=200, body=response["Data"])
