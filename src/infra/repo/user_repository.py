from typing import List
from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel


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

        # Open database connection and try to add a new user
        with DBConnectionHandler() as db_connection:
            # Try add new user
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """Select data in user entity by id and/or name

        Args:
            user_id (int, optional): Id of the registry. Defaults to None.
            name (str, optional): User's name. Defaults to None.

        Returns:
            List[Users]: List with Users selected
        """

        query_data = None

        # Try select users in database
        try:
            # Check if has id but has not name
            if user_id and not name:

                # Open database connection,
                # select user by id and get one
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

            # Check if has not id but has name
            elif not user_id and name:

                # Open database connection,
                # select user by name and get one
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            # Check if has id and name
            elif user_id and name:

                # Open database connection,
                # select user by id and by name, and get one
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise

        finally:
            db_connection.session.close()
