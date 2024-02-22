from typing import Type, Dict
from src.domain.use_cases import AlterPet as AlterPetInterface
from src.domain.models import Pets
from src.infra.repo import PetRepository


class AlterPet(AlterPetInterface):
    """AlterPet use case

    Args:
        RegisterPetInterface (_type_): _description_
    """

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def alter(
        self, pet_id: int, pet_name: str, specie: str, age: int
    ) -> Dict[bool, Pets]:
        """Alter pet use case

        Args:
            pet_id (int): Pet id
            pet_name (str): Pet name
            specie (str): Pet specie
            age (int): Pet age

        Returns:
            Dict[bool, Pets]: Dictionary with information of the process
        """

        response = None

        validate_entry = (
            isinstance(pet_id, int)
            and isinstance(pet_name, str)
            and isinstance(specie, str)
            and isinstance(age, int)
        )

        if validate_entry:
            response = self.pet_repository.update_pet(
                pet_id=pet_id,
                pet_name=pet_name,
                specie=specie,
                age=age,
            )

        return {"Success": validate_entry, "Data": response}
