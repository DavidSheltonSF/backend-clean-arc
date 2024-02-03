from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Users(Base):
    """Users Entity

    Args:
        Base (alias): _description_
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    # Inform that there is an relationship with Pets table
    id_pet = relationship("Pets")  # Yes, "Pets" is right!

    def __rep__(self):
        """Represents the instance of this class with a string

        Returns:
            _type_: _description_
        """
        return f"User [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.password == other.password
        ):
            return True
        return False
