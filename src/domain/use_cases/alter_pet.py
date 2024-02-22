from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class AlterPet(ABC):
    """AlterPet's interface use case"""

    @abstractmethod
    def alter(
        self,
        pet_id: int,
        pet_name: str,
        specie: str,
        age: int = None,
    ) -> Dict[bool, Pets]:
        """Case"""
        raise NotImplementedError("Should implement method: alter")
