from faker import Faker
from src.domain.models import Users

faker = Faker()


def mock_users() -> Users:
    """Mocking users"""
    return Users(
        id=faker.random_number(digits=5), name=faker.name(), password=faker.name()
    )
