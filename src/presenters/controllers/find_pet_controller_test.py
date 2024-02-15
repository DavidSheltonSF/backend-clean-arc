from faker import Faker
from src.infra.test import PetRepositorySpy
from src.data.test import FindPetSpy
from src.presenters.helpers import HttpRequest
from .find_pet_controller import FindPetController


faker = Faker()


def test_route():
    """Testing FindPetController route method"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    # Make a request
    http_request = HttpRequest(
        query={
            "pet_id": faker.random_number(digits=2),
            "user_id": faker.random_number(digits=5),
        }
    )

    response = find_pet_controller.route(http_request)

    # Testing inputs
    assert (
        find_pet_use_case.by_pet_id_and_user_id_param["pet_id"]
        == http_request.query["pet_id"]
    )

    assert (
        find_pet_use_case.by_pet_id_and_user_id_param["user_id"]
        == http_request.query["user_id"]
    )

    # Testing outputs
    assert response.status_code == 200
    assert response.body
