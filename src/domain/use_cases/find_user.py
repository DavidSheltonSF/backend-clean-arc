from typing import Dict, List
from abc import ABC, abstractmethod
from src.domain.models import Users


class FindUser(ABC):
    """Interface to FindUser use case"""

    @classmethod
    @abstractmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[Users]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id")

    @classmethod
    @abstractmethod
    def by_name(cls, user_name: str) -> Dict[bool, List[Users]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_name")

    @classmethod
    @abstractmethod
    def by_id_and_name(cls, user_id: int, user_name: str) -> Dict[bool, List[Users]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id_name")
