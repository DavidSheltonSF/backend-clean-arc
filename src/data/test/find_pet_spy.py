from typing import Dict, List
from src.domain.models import Pets
from src.domain.test import mock_pets


class FindPetSpy:
    """Class to define usecase: Select User"""

    def __init__(self, pet_repository: any):
        self.user_repository = pet_repository
        self.by_pet_id_param = {}
        self.by_user_id_param = {}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet by pet_id"""

        self.by_pet_id_param["pet_id"] = pet_id

        response = None

        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by user_id"""

        self.by_user_id_param["user_id"] = user_id

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[Pets]]:
        """Select all pets"""

        response = [mock_pets()]

        return {"Success": True, "Data": response}
