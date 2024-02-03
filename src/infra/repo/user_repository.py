from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """Insert data in user entity

        Args:
            name (str): user name
            password (str): user password

        Return:
        """

        InsertData = namedtuple("Users", "id, name, password")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return InsertData(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
