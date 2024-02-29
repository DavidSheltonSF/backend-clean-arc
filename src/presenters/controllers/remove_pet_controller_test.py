from faker import Faker
from src.data.test import RemovePetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .remove_pet_controller import RemovePetController

faker = Faker()


def test_route():
    """Testing RemovePetController route method"""

    remove_pet_use_case = RemovePetSpy(PetRepositorySpy())
    remove_pet_router = RemovePetController(remove_pet_use_case)

    view_arg = {"pet_id": faker.random_number(digits=2)}
    response = remove_pet_router.route(HttpRequest(view_arg=view_arg))

    # Testing inputs
    assert remove_pet_use_case.remove_param["pet_id"] == view_arg["pet_id"]

    # Testing outputs
    assert response.status_code == 200
    assert response.body
    assert "error" not in response.body
