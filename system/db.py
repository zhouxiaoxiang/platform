from sqlalchemy import Column, Integer, String, create_engine, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from system.conf import System_config
Base = declarative_base()
BaseRegion = declarative_base()
BaseFiling = declarative_base()


class System_db(object):

    def __init__(self):
        config = System_config().get()
        db_url = config.get("system", "db")
        self.engine = create_engine(db_url)

    def create_db(self):
        Base.metadata.create_all(self.engine)
        return sessionmaker(self.engine)()

    def drop_db(self):
        Base.metadata.drop_all(self.engine)
