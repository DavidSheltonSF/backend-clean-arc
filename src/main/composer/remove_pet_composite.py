from src.infra.repo import PetRepository
from src.data.remove_pet import RemovePet
from src.presenters.controllers import RemovePetController


def remove_pet_composer() -> RemovePetController:
    """
    Composing Remove Pet Route
    return - Object with Pet Route
    """
    repository = PetRepository()
    use_case = RemovePet(repository)
    remove_pet_route = RemovePetController(use_case)

    return remove_pet_route
