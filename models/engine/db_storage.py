#!/usr/bin/python3
"""This is the dbstorage class for AirBnB"""
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
        all
        """
        current = []
        objects = {}
        my_tables = {'cities': 'City', 'states': 'State', 'users': 'User',
                     'amenities': 'Amenity', 'places': 'Place',
                     'reviews': 'Review'}
        if cls:
            current = self.__session.query(eval(cls)).all()
        else:
            tables = self.__engine.table_names()
            for table in tables:
                current.append(self.__session.query(
                    eval(my_tables[table])).all())
        for obj in current:
            if type(obj) == list:
                for o in obj:
                    key = "{}.{}".format(o.__class__.__name__, o.id)
                    objects[key] = o
            else:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)
        self.save()

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ create all tables in the database
            create the current database session """
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
