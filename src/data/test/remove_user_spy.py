from typing import Dict
from src.domain.test import mock_users
from src.domain.models import Users


class RemoveUserSpy:
    """Clss to define usecase: Remove User"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository

        self.remove_param = {}

    def remove(
        self,
        user_id: int,
    ) -> Dict[bool, Users]:
        """RemoveUser use case"""

        self.remove_param["user_id"] = user_id

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = mock_users()

        return {"Success": validate_entry, "Data": response}
