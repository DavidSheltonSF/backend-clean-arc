from src.infra.repo import PetRepository
from src.infra.repo import UserRepository
from src.data.register_pet import RegisterPet
from src.data.find_user import FindUser
from src.presenters.controllers import RegisterPetController


def register_pet_composer() -> RegisterPetController:
    """
    Composing Register Pet Route
    return - Object with User Route
    """

    repository = PetRepository()
    find_user_use_case = FindUser(UserRepository())
    use_case = RegisterPet(repository, find_user_use_case)
    register_pet_route = RegisterPetController(use_case)

    return register_pet_route
