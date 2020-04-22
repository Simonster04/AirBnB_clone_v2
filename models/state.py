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
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""

    if os.getenv("HBNB_TYPE_STORAGE") == "db":       
        @property
        def cities(self):
            """ cities getter
            """
            objects = models.storage.all(City)
            city_list = []
            for key, val in objects.items():
                if val.state_id == self.id:
                    city_list.append(val)
            return city_list
