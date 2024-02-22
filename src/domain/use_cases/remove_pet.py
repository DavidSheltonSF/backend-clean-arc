from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class RemovePet(ABC):
    """RemovePet's interface use case"""

    @abstractmethod
    def remove(self, pet_id: int) -> Dict[bool, Pets]:
        """Case"""
        raise NotImplementedError("Should implement method: remove")
