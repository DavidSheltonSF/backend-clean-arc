from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class DeletePet(ABC):
    """DeletePet's interface use case"""

    @abstractmethod
    def delete(self, pet_id: int) -> Dict[bool, Pets]:
        """Case"""
        raise NotImplementedError("Should implement method: delete")
