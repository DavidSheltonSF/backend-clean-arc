from faker import Faker
from src.data.test import AlterPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from src.infra.entities.pets import AnimalTypes
from .alter_pet_controller import AlterPetController

faker = Faker()


def test_route():
    """Testing AlterPetController route method"""

    alter_pet_use_case = AlterPetSpy(PetRepositorySpy())
    alter_pet_router = AlterPetController(alter_pet_use_case)

    view_args = {"pet_id": faker.random_number(digits=2)}
    attributes = {
        "pet_name": faker.name(),
        "specie": faker.random_element(list(AnimalTypes)).name,
        "age": faker.random_number(digits=2),
    }

    response = alter_pet_router.route(HttpRequest(body=attributes, view_args=view_args))
    print(response)

    # Testing inputs
    assert alter_pet_use_case.alter_param["pet_id"] == view_args["pet_id"]
    assert alter_pet_use_case.alter_param["pet_name"] == attributes["pet_name"]
    assert alter_pet_use_case.alter_param["specie"] == attributes["specie"]
    assert alter_pet_use_case.alter_param["age"] == attributes["age"]

    # Testing outputs
    assert response.status_code == 200
    assert response.body
    assert "error" not in response.body
