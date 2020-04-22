#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ cities getter
            """
            objects = models.storage.all(City)
            city_list = []
            for city in objects.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
