from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class RegisterPet(ABC):
    """RegisterPet's interface use case"""

    @abstractmethod
    def register(
        self,
        pet_name: str,
        specie: str,
        user_id: int,
        age: int = None,
    ) -> Dict[bool, Pets]:
        """Case"""
        raise NotImplementedError("Should implement method: register")
