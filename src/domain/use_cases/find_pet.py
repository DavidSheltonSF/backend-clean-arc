from typing import Dict, List
from abc import ABC, abstractmethod
from src.domain.models import Pets


class FindPet(ABC):
    """Interface to FindPet use case"""

    @classmethod
    @abstractmethod
    def by_id(cls, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id")

    @classmethod
    @abstractmethod
    def by_user_id(cls, user_id: str) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_name")

    @classmethod
    @abstractmethod
    def by_id_and_user_id(cls, pet_id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id_name")
