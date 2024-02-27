from typing import Type, Dict, List
from src.data.find_user import FindUser
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets, Users


class RegisterPet(RegisterPetInterface):
    """RegisterPet use case

    Args:
        RegisterPetInterface (_type_): _description_
    """

    def __init__(self, pet_repository: Type[PetRepository], find_user: Type[FindUser]):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def register(
        self,
        pet_name: str,
        specie: str,
        user_id: int,
        age: int = None,
    ) -> Dict[bool, Pets]:
        """Register pet

        Args:
            pet_name (str): Pet's name
            specie (str): Pet's specie
            age (int): Pet's age
            user_id (int): User's id
            user_id and/or name

        Returns:
            Dict[bool, pets]: Dictionary with imformation of the process
        """

        response = None

        validate_entry = (
            isinstance(pet_name, str)
            and isinstance(specie, str)
            and (isinstance(age, int) or age is None)
            and isinstance(user_id, int)
        )

        user = self.__find_user_information(user_id)

        # Check validate_entry and user found
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                pet_name, specie, age, user["Data"][0].id
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(self, user_id: int) -> Dict[bool, List[Users]]:
        """Check user infos and select user

        Args:
            user_information (Dict[int, str]): Dictionary with
            user_id and/or name

        Returns:
            Dict[bool, List[Users]]: Dictionary with the response
            of find_user use case
        """

        if user_id:
            user_founded = self.find_user.by_id(user_id)

        # In last case
        else:
            return {"Success": False, "Data": None}

        return user_founded
