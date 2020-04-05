#!/usr/bin/python3
"""
This is the dbstorage class for AirBnB
"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class storages in the database to instances
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"), os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"), os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary with objects in database
        """
        all_classes = {"User": User, "State": State, "City": City,
                       "Amenity": Amenity, "Place": Place, "Review": Review}
        bbsito = {}
        if type(cls) is str:
            for key, val in all_classes.items():
                if key == cls:
                    cls = val
        if cls is not None:
            objects = self.__session.query(cls)
            for obj in objects:
                bbsito[obj.__dict__['id']] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for my_class in classes:
                objects = self.__session.query(my_class).all()
                if objects:
                    for obj in objects:
                        bbsito[obj.__dict__['id']] = obj
        return bbsito

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database
            create the current database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ clean for new session"""
        if self.__session:
            self.__session.remove()
