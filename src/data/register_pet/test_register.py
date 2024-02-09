from faker import Faker
from src.infra.test import PetRepositorySpy
from src.infra.entities import AnimalTypes
from .register import RegisterPet


faker = Faker()


def test_register():
    """Testing registry method"""
    pet_repo = PetRepositorySpy()
    register_pet = RegisterPet(pet_repo)

    # Intance fake data
    attributes = {
        "name": faker.name(),
        "specie": faker.random_element(list(AnimalTypes)).name,
        "age": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }

    # Insert fake data
    response = register_pet.register(
        attributes["name"],
        attributes["specie"],
        attributes["age"],
        attributes["user_id"],
    )

    print(response)

    # testing inputs
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]
    assert pet_repo.insert_pet_params["user_id"] == attributes["user_id"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]
