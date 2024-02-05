from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Shold insert user user in User table"""

    # Instance the fake dada to insert into Users entity
    name = faker.name()
    password = faker.word()

    # Get the database's engine
    engine = db_connection_handler.get_engine()

    # Insert the user in database
    new_user = user_repository.insert_user(name, password)

    # Do a query to get the user's data from database
    query_user = engine.execute(
        f"""
        SELECT *
        FROM users
        WHERE id = {new_user.id}
        """
    ).fetchone()

    # print(query_user)
    # print(new_user)

    # Delete the user inserted
    engine.execute(
        f"""
            DELETE FROM users
            WHERE ID = {new_user.id}
        """
    )

    # Check if user's data inserted is
    # equal the user's data selected by the query
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """Should select a user in Users table and compare it"""

    # Intance fake data to read
    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()

    # Instance an User object
    data = UsersModel(id=user_id, name=name, password=password)

    # Get the database's engine
    engine = db_connection_handler.get_engine()

    # Insert a fake user to test the query selections
    engine.execute(
        f"""
            INSERT INTO USERS (id, name, password)
            VALUES ('{user_id}', '{name}', '{password}')
        """
    )

    # Do 3 query selections to test
    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(name=name)
    query_user3 = user_repository.select_user(user_id=user_id, name=name)

    # Check if User's data inserted
    # is in the data obtained in the queries
    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    # Delete the fake user from database
    engine.execute(f"DELETE FROM users WHERE id='{user_id}'")
