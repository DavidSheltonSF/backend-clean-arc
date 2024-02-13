from typing import Dict, List
from src.domain.test import mock_pets, mock_users
from src.domain.models import Pets, Users


class RegisterPetSpy:
    """Clss to define usecase: Register Pet"""

    def __init__(self, pet_repository: any, find_user: any):
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.register_param = {}

    def register(
        self,
        pet_name: str,
        specie: str,
        user_information: Dict[int, str],
        age: int = None,
    ) -> Dict[bool, Pets]:
        """RegisterPet use case"""

        self.register_param["pet_name"] = pet_name
        self.register_param["specie"] = specie
        self.register_param["user_information"] = user_information
        self.register_param["age"] = age

        response = None

        validate_entry = (
            isinstance(pet_name, str)
            and isinstance(specie, str)
            and (isinstance(age, int) or age is None)
            and isinstance(user_information, dict)
        )
        # Try to find the user
        user = self.__find_user_information(user_information)

        # Check validate_entry and user found
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pets()

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user infos and select user"""

        user_founded = None
        user_params = user_information.keys()

        # Check if user_id  and user_name is in params
        if "user_id" in user_params and "user_name" in user_params:
            user_founded = {"Success": True, "Data": mock_users()}

        # Check if user_id is in params and user_name is not
        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = user_founded = {"Success": True, "Data": mock_users()}

        # Check if user_id is not in params and user_name is in
        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = user_founded = {"Success": True, "Data": mock_users()}

        # In last case
        else:
            return {"Success": False, "Data": None}

        return user_founded
