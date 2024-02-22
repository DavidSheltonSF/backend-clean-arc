from typing import Dict
from src.domain.test import mock_pets
from src.domain.models import Pets


class AlterPetSpy:
    """Clss to define usecase: Alter Pet"""

    def __init__(self, pet_repository: any):
        self.pet_repository = pet_repository

        self.alter_param = {}

    def alter(
        self,
        pet_id: int,
        pet_name: str,
        specie: str,
        age: int = None,
    ) -> Dict[bool, Pets]:
        """AlterPet use case"""

        self.alter_param["pet_id"] = pet_id
        self.alter_param["pet_name"] = pet_name
        self.alter_param["specie"] = specie
        self.alter_param["age"] = age

        response = None

        validate_entry = (
            isinstance(pet_id, int)
            and isinstance(pet_name, str)
            and isinstance(specie, str)
            and (isinstance(age, int) or age is None)
        )

        if validate_entry:
            response = mock_pets()

        return {"Success": validate_entry, "Data": response}
