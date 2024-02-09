from faker import Faker
from src.domain.models import Pets
from src.infra.entities import AnimalTypes


faker = Faker()


def mock_pets() -> Pets:
    """Mocking pets"""
    return Pets(
        id=faker.random_number(digits=5),
        name=faker.name(),
        specie=faker.random_element(list(AnimalTypes)).name,
        age=faker.random_number(digits=2),
        user_id=faker.random_number(digits=5),
    )
