from typing import Type
from src.main.interface import RouteInterface
from src.data.alter_pet import AlterPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class AlterPetController(RouteInterface):
    """Class to define a controller to AlterPet use case"""

    def __init__(self, alter_pet_use_case: Type[AlterPet]):
        self.alter_pet_use_case = alter_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None
        print(http_request.body)
        # Check if there is a body in http_request
        if http_request.body:
            body_params = http_request.body.keys()

            required_params = ["pet_id", "pet_name", "specie", "age"]
            checker = all(item in body_params for item in required_params)

            # check if pet_id and user_id are in body_params
            if checker:

                pet_id = http_request.body["pet_id"]
                pet_name = http_request.body["pet_name"]
                specie = http_request.body["specie"]
                age = http_request.body["age"]

                response = self.alter_pet_use_case.alter(
                    pet_id=pet_id, pet_name=pet_name, specie=specie, age=age
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
