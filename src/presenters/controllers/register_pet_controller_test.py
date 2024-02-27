from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from src.infra.entities.pets import AnimalTypes
from .register_pet_controller import RegisterPetController

faker = Faker()


def test_route():
    """Testing RegisterPetController route method"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "pet_name": faker.name(),
        "specie": faker.random_element(list(AnimalTypes)).name,
        "user_id": faker.random_number(digits=5),
        "age": faker.random_number(digits=2),
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing inputs
    assert register_pet_use_case.register_param["pet_name"] == attributes["pet_name"]
    assert register_pet_use_case.register_param["specie"] == attributes["specie"]
    assert register_pet_use_case.register_param["age"] == attributes["age"]
    assert register_pet_use_case.register_param["user_id"] == attributes["user_id"]

    # Testing outputs
    assert response.status_code == 200
    assert response.body
    assert "error" not in response.body
