from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import RegisterPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class RegisterPetController(RouteInterface):
    """Class to Define a controller to RegisterPet use case"""

    def __init__(self, register_pet_use_case: Type[RegisterPet]):
        self.register_pet_use_case = register_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        # Check if there is a body in http_request
        if http_request.body:

            body_params = http_request.body.keys()

            # Check if required pet attributes are in body_params
            if (
                "pet_name" in body_params
                and "specie" in body_params
                and "user_information" in body_params
            ):
                user_information_params = http_request.body["user_information"].keys()

                # Check if required user attributes are in body_params
                if (
                    "user_id" in user_information_params
                    or "user_name" in user_information_params
                ):

                    pet_name = http_request.body["pet_name"]
                    specie = http_request.body["specie"]
                    user_information = http_request.body["user_information"]

                    if "age" in body_params:
                        age = http_request.body["age"]
                    else:
                        age = None

                    response = self.register_pet_use_case.register(
                        pet_name=pet_name,
                        specie=specie,
                        user_information=user_information,
                        age=age,
                    )
                else:
                    response = {"Success": False, "Data": None}

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
