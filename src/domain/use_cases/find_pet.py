from typing import Dict, List
from abc import ABC, abstractmethod
from src.domain.models import Pets


class FindPet(ABC):
    """Interface to FindPet use case"""

    @abstractmethod
    def by_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id")

    @abstractmethod
    def by_user_id(self, user_id: str) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_name")

    @abstractmethod
    def by_id_and_user_id(self, pet_id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id_name")
