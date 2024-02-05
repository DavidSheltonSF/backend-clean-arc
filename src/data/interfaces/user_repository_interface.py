from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface to User Repository"""

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """Abstract method"""
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, name: int = None) -> List[Users]:
        """Abstract method"""
        raise NotImplementedError("Method not implemented")
