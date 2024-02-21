from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class DeleteUser(ABC):
    """DeleteUser's interface use case"""

    @abstractmethod
    def delete(self, user_id: int) -> Dict[bool, Users]:
        """Case"""
        raise NotImplementedError("Should implement method: delete")
