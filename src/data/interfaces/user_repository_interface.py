from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface to User Repository"""

    @classmethod
    @abstractmethod
    def insert_user(cls, user_name: str, password: str) -> Users:
        """Abstract method"""
        raise NotImplementedError("Should implement method: insert_user")

    @classmethod
    @abstractmethod
    def select_user(cls, user_id: int = None, user_name: int = None) -> List[Users]:
        """Abstract method"""
        raise NotImplementedError("Should implement method: select_user")

    @classmethod
    @abstractmethod
    def update_user(cls, user_id: int, user_name: str, password: str) -> List[Users]:
        """Abstract method"""
        raise NotImplementedError("Should implement method: select_user")

    @classmethod
    @abstractmethod
    def delete_user(cls, user_id: int) -> List[Users]:
        """Abstract method"""
        raise NotImplementedError("Should implement method: select_user")
