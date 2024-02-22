from typing import Type
from src.main.interface import RouteInterface
from src.data.remove_pet import RemovePet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class RemovePetController(RouteInterface):
    """Class to define a controller to RemovePet use case"""

    def __init__(self, remove_pet_use_case: Type[RemovePet]):
        self.remove_pet_use_case = remove_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        # Check if there is a body in http_request
        if http_request.body:
            body_params = http_request.body.keys()

            # check if pet_id and user_id are in body_params
            if "pet_id" in body_params:

                pet_id = http_request.body["pet_id"]

                response = self.remove_pet_use_case.remove(pet_id=pet_id)

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
