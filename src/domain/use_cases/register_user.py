from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUser(ABC):
    """Interface do RegisterUser use case"""

    @classmethod
    @abstractmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """Case"""
        raise NotImplementedError("Shold implement method: register")
