from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class AlterUser(ABC):
    """AlterUser's interface use case"""

    @abstractmethod
    def alter(self, user_id: int, user_name: str, password: str) -> Dict[bool, Users]:
        """Case"""
        raise NotImplementedError("Should implement method: alter")
