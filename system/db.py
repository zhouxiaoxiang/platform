from sqlalchemy import Column, Integer, String, create_engine, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from system.conf import System_config
from redis import StrictRedis

Base = declarative_base()
BaseRegion = declarative_base()
BaseFiling = declarative_base()


class System_db(object):
    """
    Create system db mechanics
    
    Examples
    --------
    Create database and datasets

    >>> from system.db import *
    >>> _db = System_db()
    >>> db = _db.get_db()
    >>> rs = _db.get_rs()
    """

    def __init__(self):
        config = System_config()
        self.datasets = config.get("system", "datasets")
        self.database = config.get("system", "database")
        self.engine = create_engine(self.database)

    def get_db(self):
        """ 
        Get a session 
        For others, it's db.

        """

        Base.metadata.create_all(self.engine)
        return sessionmaker(self.engine)()

    def drop_db(self):
        """  Drop all db.  """

        Base.metadata.drop_all(self.engine)

    def get_rs(self):
        """ Support redis """

        return StrictRedis.from_url(self.datasets)

