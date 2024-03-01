from typing import Type
from src.main.interface import RouteInterface
from src.data.find_pet import FindPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class FindPetController(RouteInterface):
    """Class to define a controller to FindPet use case"""

    def __init__(self, find_pet_use_case: Type[FindPet]):
        self.find_pet_use_case = find_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None
        print(f"Args ->{http_request.view_args}")
        # Check if there is a view_args in http_request
        if http_request.view_args:
            view_args = http_request.view_args.keys()

            # check if pet_id is in view_args
            if "pet_id" in view_args:

                pet_id = http_request.view_args["pet_id"]

                response = self.find_pet_use_case.by_pet_id(
                    pet_id=pet_id,
                )
                print(response)

            # check if user_id is in view_args
            elif "user_id" in view_args:

                user_id = http_request.view_args["user_id"]

                response = self.find_pet_use_case.by_user_id(user_id=user_id)

            else:
                response = {"Success": False, "Data": None}

            # If request failed, Unprocessable Entity
            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

        else:
            response = self.find_pet_use_case.all()

        return HttpResponse(status_code=200, body=response["Data"])
