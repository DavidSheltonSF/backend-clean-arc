from typing import Type, Dict, List
from src.domain.use_cases import FindUser as FindUserInterface
from src.infra.repo import UserRepository
from src.domain.models import Users


class FindUser(FindUserInterface):
    """Class to define use case Find User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Find user by id

        Args:
            user_id (int): User's id

        Returns:
            Dict[bool, List[Users]]: _description_
        """

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Find user by name

        Args:
            user_id (int): User's id

        Returns:
            Dict[bool, List[Users]]: _description_
        """

        response = None

        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Find user by id and name

        Args:
            user_id (int): User's id

        Returns:
            Dict[bool, List[Users]]: _description_
        """

        response = None

        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(user_id, name)

        return {"Success": validate_entry, "Data": response}
