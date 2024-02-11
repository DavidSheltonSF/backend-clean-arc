from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUser(ABC):
    """RegisterUser's interface use case"""

    @abstractmethod
    def register(self, user_name: str, password: str) -> Dict[bool, Users]:
        """Case"""
        raise NotImplementedError("Should implement method: register")
