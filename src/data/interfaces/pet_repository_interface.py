from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @classmethod
    @abstractmethod
    def insert_pet(cls, pet_name: str, specie: str, age: int, user_id: int) -> Pets:
        """Abstract method"""
        raise NotImplementedError("Should implement method: insert_pet")

    @classmethod
    @abstractmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Abstract method"""
        raise NotImplementedError("Should implement method: select_pet")
