from typing import Type
from src.domain.use_cases import FindUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class FindUserController:
    """Class to define controller to find_user use case"""

    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        # Check if there is a query in http_request
        if http_request.query:
            query_string_params = http_request.query.keys()

            # Check if user_id and user_name are in query_string_params
            if "user_id" in query_string_params and "user_name" in query_string_params:
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]
                response = self.find_user_use_case.by_id_and_name(
                    user_id=user_id, user_name=user_name
                )

            # Check if user_id is in query_string_params but user_name is not
            elif (
                "user_id" in query_string_params
                and "user_name" not in query_string_params
            ):
                user_id = http_request.query["user_id"]
                response = self.find_user_use_case.by_id(user_id=user_id)

            # Check if user_id is not in query_string_params but user_name is in
            elif (
                "user_id" not in query_string_params
                and "user_name" in query_string_params
            ):
                user_name = http_request.query["user_name"]
                response = self.find_user_use_case.by_name(user_name=user_name)

            # In last case
            else:
                response = {"Success": False, "Data": None}

            # If the request failed
            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
