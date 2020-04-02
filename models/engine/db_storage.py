#!/usr/bin/python3
"""
This is the dbstorage class for AirBnB
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
import sqlalchemy
import os

all_classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
                "Amenity": Amenity, "Place": Place, "Review": Review}



class DBStorage:
    """This class storages in the database to instances
    Attributes:
        __engine: None
        __session: None
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv(HBNB_MYSQL_USER), os.getenv(HBNB_MYSQL_PWD),
            os.getenv(HBNB_MYSQL_HOST), os.getenv(HBNB_MYSQL_DB)),
            pool_pre_ping=True)
        if os.getenv(HBNB_ENV) == "test":
            Base.metadata.drop_all(bind=self.__engine)

        def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        
        bbsito = {}
        if cls is not None:
            if cls in all_classes:
                for var in self.__session.query(all_classes[cls]):
                    bbsito[var.__class__.__name__ + "." + var.id] = var

            return bbsito
