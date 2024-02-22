from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Users(Base):
    """Users Entity

    Inheritance:
        Base (alias): Sqlalchemy base for
        customized classes to access sqlalchemy resources
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    # Inform that there is an relationship with Pets table
    id_pet = relationship("Pets", cascade="all, delete-orphan")  # Yes, "Pets" is right!

    def __rep__(self):
        """Represents the instance of this class by a string

        Returns:
            (str): An string to represent the instance of this class
        """
        return f"User [name={self.name}]"

    def __eq__(self, other):
        """Compare the current Users instance
        with another Users instance

        Args:
            other (Users): Other Users instance

        Returns:
            (bool): Return True if the instances
            are considered equal and False, else.
        """

        if isinstance(other, Users):
            if (
                self.id == other.id
                and self.name == other.name
                and self.password == other.password
            ):
                return True

        return False
