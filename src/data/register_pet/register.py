from typing import Type, Dict
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets


class RegisterPet(RegisterPetInterface):
    """RegisterPet use case

    Args:
        RegisterPetInterface (_type_): _description_
    """

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def register(
        self, name: str, specie: str, age: int, user_id: int
    ) -> Dict[bool, Pets]:
        """Register pet

        Args:
            name (str): _description_
            specie (str): _description_
            age (int): _description_
            user_id (int): _description_

        Returns:
            Dict[bool, pets]: Dictionary with imformation of the process
        """

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(specie, str)
            and isinstance(age, int)
            and isinstance(user_id, int)
        )

        if validate_entry:
            response = self.pet_repository.insert_pet(name, specie, age, user_id)

        return {"Success": validate_entry, "Data": response}
