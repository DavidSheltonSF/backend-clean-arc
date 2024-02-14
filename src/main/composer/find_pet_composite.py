from src.infra.repo import PetRepository
from src.data.find_pet import FindPet
from src.presenters.controllers import FindPetController


def find_pet_composer() -> FindPetController:
    """
    Composing Find Pet Route
    return - Object with Pet Route
    """

    repository = PetRepository()
    use_case = FindPet(repository)
    find_pet_route = FindPetController(use_case)

    return find_pet_route
