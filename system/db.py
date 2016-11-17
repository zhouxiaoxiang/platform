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
    >>> system_db = System_db()
    >>> db = system_db.create_db()
    >>> rs = system_db.create_rs()
    """

    def __init__(self):
        config = System_config().get()
        self.datasets = config.get("system", "datasets")
        self.database = config.get("system", "database")
        self.engine = None

    def create_db(self):
        self.engine = create_engine(self.database)
        Base.metadata.create_all(self.engine)
        return sessionmaker(self.engine)()

    def drop_db(self):
        Base.metadata.drop_all(self.engine)

    def create_rs(self):
        return StrictRedis.from_url(self.datasets)

