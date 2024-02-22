from faker import Faker
from src.infra.test import PetRepositorySpy
from src.infra.entities import AnimalTypes
from .alter import AlterPet


faker = Faker()


def test_alter():
    """Testing alter method"""
    pet_repo = PetRepositorySpy()
    alter_pet = AlterPet(pet_repo)

    # Intance fake data
    attributes = {
        "pet_id": faker.random_number(digits=5),
        "pet_name": faker.name(),
        "specie": faker.random_element(list(AnimalTypes)).name,
        "age": faker.random_number(digits=2),
    }

    # Update fake pet with fake data
    response = alter_pet.alter(
        attributes["pet_id"],
        attributes["pet_name"],
        attributes["specie"],
        attributes["age"],
    )

    print(pet_repo.update_pet_params)

    # testing inputs
    assert pet_repo.update_pet_params["pet_id"] == attributes["pet_id"]
    assert pet_repo.update_pet_params["pet_name"] == attributes["pet_name"]
    assert pet_repo.update_pet_params["specie"] == attributes["specie"]
    assert pet_repo.update_pet_params["age"] == attributes["age"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_alter_fail():
    """Testing alter method"""
    pet_repo = PetRepositorySpy()
    alter_pet = AlterPet(pet_repo)

    # Intance fake data
    attributes = {
        "pet_id": "invalid ID",
        "pet_name": faker.name(),
        "specie": faker.random_element(list(AnimalTypes)).name,
        "age": faker.random_number(digits=2),
    }

    # Update fake pet with fake data
    response = alter_pet.alter(
        attributes["pet_id"],
        attributes["pet_name"],
        attributes["specie"],
        attributes["age"],
    )

    # testing inputs
    assert not pet_repo.update_pet_params

    # testing outputs
    assert response["Success"] is False
    assert not response["Data"]
