from src.infra.repo import UserRepository
from src.data.remove_user import RemoveUser
from src.presenters.controllers import RemoveUserController


def remove_user_composer() -> RemoveUserController:
    """
    Composing Remove User Route
    return - Object with User Route
    """
    repository = UserRepository()
    use_case = RemoveUser(repository)
    remove_user_route = RemoveUserController(use_case)

    return remove_user_route
