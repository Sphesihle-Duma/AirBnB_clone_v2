from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"  # Set the table name to "cities"
    name = Column(String(128), nullable=False)  # Add the "name" column
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)  # Add the "state_id" column as a foreign key to states.id
