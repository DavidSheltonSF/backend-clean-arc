from typing import Dict, List
from abc import ABC, abstractmethod
from src.domain.models import Pets


class FindPet(ABC):
    """Interface to FindPet use case"""

    @abstractmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id")

    @abstractmethod
    def by_user_id(self, user_id: str) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_name")

    @abstractmethod
    def all(self) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id_name")
