from src.infra.repo import PetRepository
from src.data.alter_pet import AlterPet
from src.presenters.controllers import AlterPetController


def alter_pet_composer() -> AlterPetController:
    """
    Composing Alter Pet Route
    return - Object with Pet Route
    """
    repository = PetRepository()
    use_case = AlterPet(repository)
    alter_pet_route = AlterPetController(use_case)

    return alter_pet_route
