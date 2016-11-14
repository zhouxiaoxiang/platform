from sqlalchemy import Column, Integer, String, create_engine, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from system import conf
Base = declarative_base()
BaseRegion = declarative_base()
BaseFiling = declarative_base()

class System_db(object):
    def __init__(self):
        self.engine = create_engine(conf.DB_URL)

    def create_db(self):
        Base.metadata.create_all(self.engine)
        return sessionmaker(self.engine)()

    def drop_db(self):
        Base.metadata.drop_all(self.engine)


