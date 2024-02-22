from typing import Dict
from src.domain.test import mock_pets
from src.domain.models import Pets


class RemovePetSpy:
    """Clss to define usecase: Remove Pet"""

    def __init__(self, pet_repository: any):
        self.pet_repository = pet_repository

        self.remove_param = {}

    def remove(
        self,
        pet_id: int,
    ) -> Dict[bool, Pets]:
        """RemovePet use case"""

        self.remove_param["pet_id"] = pet_id

        response = None

        validate_entry = isinstance(pet_id, str)

        if validate_entry:
            response = mock_pets()

        return {"Success": validate_entry, "Data": response}
