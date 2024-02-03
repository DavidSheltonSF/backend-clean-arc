from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository
from src.infra.entities import Users as UsersModel


faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Shold insert user"""

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    # SQL commands
    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute(
        f"""
        SELECT *
        FROM users
        WHERE id = {new_user.id}
        """
    ).fetchone()
    print(query_user)
    print(new_user)

    engine.execute(
        f"""
            DELETE FROM users
            WHERE ID = {new_user.id}
        """
    )

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """Should select a user in Users table and compare it"""
    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = UsersModel(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine()
    engine.execute(
        f"""
            INSERT INTO USERS (id, name, password)
            VALUES ('{user_id}', '{name}', '{password}')
        """
    )

    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(name=name)
    query_user3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    engine.execute(f"DELETE FROM users WHERE id='{user_id}'")
