from src.infra.repo import UserRepository
from src.data.find_user import FindUser
from src.presenters.controllers import FindUserController


def find_user_composer() -> FindUserController:
    """
    Composing Find User Route
    return - Object with User Route
    """

    repository = UserRepository()
    use_case = FindUser(repository)
    find_user_route = FindUserController(use_case)

    return find_user_route
