import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Define Anymals Types

    Args:
        enum (Enum): _description_
    """

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
    TURTLE = "turtle"


class Pets(Base):
    """Pets Entity

    Inheritance:
        Base (alias): Sqlalchemy base for
        customized classes to access sqlalchemy resources
    """

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    @classmethod
    def row_to_pet(cls, row):
        """Convert a row into Pet a instance"""
        # Maybe it's necessary an error handling

        return Pets(
            id=row.id,
            name=row.name,
            specie=AnimalTypes(row.specie.lower()),
            age=row.age,
            user_id=row.user_id,
        )

    def __repr__(self):
        """Represents the instance of this class by a string

        Returns:
            (str): An string to represent the instance of this class
        """

        return f"""
        Pet [
            name={self.name},
            specie={self.specie},
            userId={self.user_id}
        ]
        """

    def __eq__(self, other):
        """Compare the current Pets instance
        with another Pets instance

        Args:
            other (Pets): Other Pets instance

        Returns:
            (bool): Return True if the instances
            are considered equal and False, else.
        """

        if isinstance(other, Pets):
            if (
                self.id == other.id
                and self.name == other.name
                and self.specie == other.specie
                and self.age == other.age
                and self.user_id == other.user_id
            ):
                return True
        return False
