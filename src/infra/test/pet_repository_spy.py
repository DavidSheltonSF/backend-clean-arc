from typing import List
from src.domain.models import Pets
from src.domain.test import mock_pets


class PetRepositorySpy:
    """Spy to Pet Repository"""

    def __init__(self):
        self.insert_pet_params = {}
        self.select_pet_params = {}

    def insert_pet(
        self,
        name: str = None,
        specie: str = None,
        age: int = None,
        user_id: int = None,
    ) -> Pets:
        """Spy to all the attributes"""
        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id

        return mock_pets()

    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Spy to all the attributes"""
        self.select_pet_params["pet_id"] = pet_id
        self.select_pet_params["user_id"] = user_id

        return [mock_pets()]
