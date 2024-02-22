from typing import Type, Dict
from src.domain.use_cases import RemovePet as RemovePetInterface
from src.domain.models import Pets
from src.infra.repo import PetRepository


class RemovePet(RemovePetInterface):
    """RemovePet use case

    Args:
        RemovePetInterface (_type_): _description_
    """

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def remove(self, pet_id: int) -> Dict[bool, Pets]:
        """Delete pet use case

        Args:
            pet_id (int): Pet id

        Returns:
            Dict[bool, Pets]: Dictionary with information of the process
        """

        response = None

        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.delete_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}
