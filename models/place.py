#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table

association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade="delete", backref="place")
        amenities = relationship("Amenity",
                                 secondary=association_table,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            self.amenity_ids = obj.id
            if obj.__class__.__name__ != "Amenity":
                return
            amenity_dict = models.storage.all(obj)
            place_id = self.id
            for key, value in amenity_dict.items():
                if self.id == value.place_id:
                    self.amenity_ids.append(value.id)
