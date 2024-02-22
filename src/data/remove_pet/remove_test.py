from faker import Faker
from src.infra.test import PetRepositorySpy
from .remove import RemovePet


faker = Faker()


def test_alter():
    """Testing registry method"""
    pet_repo = PetRepositorySpy()
    remove_pet = RemovePet(pet_repo)

    # Intance fake data
    attributes = {
        "pet_id": faker.random_number(digits=5),
    }

    # Update fake pet with fake data
    response = remove_pet.remove(attributes["pet_id"])

    # testing inputs
    assert pet_repo.delete_pet_params["pet_id"] == attributes["pet_id"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_alter_fail():
    """Testing registry method"""
    pet_repo = PetRepositorySpy()
    remove_pet = RemovePet(pet_repo)

    # Intance fake data
    attributes = {"pet_id": "invalid ID"}

    # Update fake pet with fake data
    response = remove_pet.remove(attributes["pet_id"])

    # testing inputs
    assert not pet_repo.delete_pet_params  # test if it is {}

    # testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
