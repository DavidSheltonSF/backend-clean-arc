from typing import Type, Dict, List
from src.domain.use_cases import FindPet as FindPetInterface
from src.infra.repo import PetRepository
from src.domain.models import Pets


class FindPet(FindPetInterface):
    """Class to define use case Find Pet"""

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Find pet by id

        Args:
            pet_id (int): Pet's id

        Returns:
            Dict[bool, List[Pets]]: _description_
        """

        response = None

        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: str) -> Dict[bool, List[Pets]]:
        """Find pet by pet's user id

        Args:
            user_id (int): Pet's user_id

        Returns:
            Dict[bool, List[Pets]]: _description_
        """

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Find pet by id and name

        Args:
            pet_id (int): Pet's id
            pet_id (int): Pet's user id

        Returns:
            Dict[bool, List[Pets]]: _description_
        """

        response = None

        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id, user_id)

        return {"Success": validate_entry, "Data": response}
