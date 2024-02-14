from typing import Type
from src.main.interface import RouteInterface
from src.data.find_pet import FindPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class FindPetController(RouteInterface):
    """Controller"""

    def __init__(self, find_pet_use_case: Type[FindPet]):
        self.find_pet_use_case = find_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        # Check if there is a query in http_request
        if http_request.query:
            query_string_params = http_request.query.keys()

            # check if pet_id and user_id are in query_string_params
            if "pet_id" in query_string_params and "user_id" in query_string_params:

                pet_id = http_request.query["pet_id"]
                user_id = http_request.query["user_id"]

                response = self.find_pet_use_case.by_pet_id_and_user_id(
                    pet_id=pet_id, user_id=user_id
                )

            # check if pet_id is in query_string_params and user_id is not
            elif (
                "pet_id" in query_string_params and "user_id" not in query_string_params
            ):

                pet_id = http_request.query["pet_id"]

                response = self.find_pet_use_case.by_pet_id(pet_id=pet_id)

            # check if pet_id is not in query_string_params and user_id is in
            elif (
                "pet_id" not in query_string_params
                and "user_id" not in query_string_params
            ):

                user_id = http_request.query["user_id"]

                response = self.find_pet_use_case.by_user_id(user_id=user_id)

            # In last case
            else:
                response = {"Success": False, "Data": None}

            # If request failed
            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

        # If there is no query in http_request
        http_error = HttpErrors.error_400()

        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
