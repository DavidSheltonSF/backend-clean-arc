from typing import Type, Dict
from src.domain.use_cases import RemoveUser as RemoveUserInterface
from src.domain.models import Users
from src.infra.repo import UserRepository


class RemoveUser(RemoveUserInterface):
    """RemoveUser use case

    Args:
        RemoveUserInterface (_type_): _description_
    """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def remove(self, user_id: int) -> Dict[bool, Users]:
        """Delete user use case

        Args:
            user_id (int): User id

        Returns:
            Dict[bool, Users]: Dictionary with information of the process
        """

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.delete_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}
