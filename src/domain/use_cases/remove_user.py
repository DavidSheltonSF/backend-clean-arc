from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RemoveUser(ABC):
    """RemoveUser's interface use case"""

    @abstractmethod
    def remove(self, user_id: int) -> Dict[bool, Users]:
        """Case"""
        raise NotImplementedError("Should implement method: remove")
