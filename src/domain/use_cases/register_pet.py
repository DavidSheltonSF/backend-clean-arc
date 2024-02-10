from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class RegisterPet(ABC):
    """RegisterPet's interface use case"""

    @classmethod
    @abstractmethod
    def register(
        cls,
        name: str,
        specie: str,
        user_information: Dict[int, str],
        age: int = None,
    ) -> Dict[bool, Pets]:
        """Case"""
        raise NotImplementedError("Should implement method: register")
