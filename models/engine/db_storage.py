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

<<<<<<< HEAD
all_classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
                "Amenity": Amenity, "Place": Place, "Review": Review}



=======
all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}
                
    
>>>>>>> beffef56ea7fc479f1026670102ceb086638b627
class DBStorage:
    """This class storages in the database to instances
    Attributes:
        __engine: None
        __session: None
    """
    __engine = None
    __session = None

<<<<<<< HEAD
=======

>>>>>>> beffef56ea7fc479f1026670102ceb086638b627
    def __init__(self):
        """ Instantiation of DBStorage class """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv(HBNB_MYSQL_USER), os.getenv(HBNB_MYSQL_PWD),
            os.getenv(HBNB_MYSQL_HOST), os.getenv(HBNB_MYSQL_DB)),
            pool_pre_ping=True)
<<<<<<< HEAD
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
=======

        if os.getenv(HBNB_ENV) == "test":
            Base.metadata.drop_all(bind=self.__engine)
        
    def all(self, cls=None):
        """
        returns a dictionary with objects in database
        """
        bbsito = {}
        if cls is None:
            classes = [key for key, val in all_classes.items()]
        else:
            classes = [key for key, val in all_classes.items() if key == cls]
        for my_cls in classes:
            for var in self.__session.query(all_classes[my_cls]):
                bbsito[var.__class__.__name__ + "." + var.id] = var
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
        Base.metadata.create_all(self.engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
>>>>>>> beffef56ea7fc479f1026670102ceb086638b627
