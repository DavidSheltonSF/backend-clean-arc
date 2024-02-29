from faker import Faker
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.infra.entities import AnimalTypes
from src.data.test import FindUserSpy
from .register import RegisterPet


faker = Faker()


def test_register():
    """Testing registry method"""

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy)
    register_pet = RegisterPet(pet_repo, find_user)

    # Intance fake data
    attributes = {
        "pet_name": faker.name(),
        "specie": faker.random_element(list(AnimalTypes)).name,
        "age": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=5),
    }

    # Insert fake data
    response = register_pet.register(
        attributes["pet_name"],
        attributes["specie"],
        attributes["user_id"],
        attributes["age"],
    )

    # testing inputs
    assert pet_repo.insert_pet_params["pet_name"] == attributes["pet_name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]

    # Testing FindUser Inputs
    assert find_user.by_id_param["user_id"] == attributes["user_id"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]
