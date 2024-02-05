from typing import List
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel


class PetRepository(PetRepositoryInterface):
    """Class to manage Pet Repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Inser data in PetEntity entity

        Args:
            name (str): Pet's name
            specie (str): Pet's specie
            age (int): Pet's age
            user_id (int): Pet's id of owner

        Returns:
            Pets: Tuple with data of pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.name,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Slect data in PetsEntity entity by id and/or user_id

        Args:
            pet_id (int, optional): Id of the pet registry. Defaults to None.
            user_id (int, optional): Id of the owner. Defaults to None.

        Returns:
            List[Pets]: List with pets selected
        """

        try:

            query_data = None

            if pet_id and not user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id)
                        .one()
                    )
                    query_data = [data]

            elif not pet_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data

            elif pet_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetsModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise

        finally:
            db_connection.session.close()
