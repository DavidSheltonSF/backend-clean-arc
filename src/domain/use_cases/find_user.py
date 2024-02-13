from typing import Dict, List
from abc import ABC, abstractmethod
from src.domain.models import Users


class FindUser(ABC):
    """Interface to FindUser use case"""

    @abstractmethod
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id")

    @abstractmethod
    def by_name(self, user_name: str) -> Dict[bool, List[Users]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_name")

    @abstractmethod
    def by_id_and_name(self, user_id: int, user_name: str) -> Dict[bool, List[Users]]:
        """Specific case"""
        raise NotImplementedError("Should implement method: by_id_name")
