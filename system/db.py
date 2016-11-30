from sqlalchemy import Column, Integer, String, create_engine, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from system.conf import Config
from redis import StrictRedis
from sqlalchemy import and_, or_, distinct, func

Base = declarative_base()
BaseRegion = declarative_base()
BaseFiling = declarative_base()


class Db(object):

    """
    Create system db mechanics

    Examples
    --------
    Create database and datasets

    >>> from system.db import *
    >>> _db = Db()
    >>> db = _db.get_db()
    >>> isinstance(db, scoped_session)
    True
    >>> rs = _db.get_rs()
    >>> isinstance(rs, StrictRedis)
    True
    """

    def __init__(self):
        self.config = Config()

    def get_db(self):
        """
        Get a session
        For others, it's db.
        """

        self.engine = create_engine(self.config["database"])
        Base.metadata.create_all(self.engine)
        return scoped_session(sessionmaker(self.engine))

    def drop_db(self):
        """  Drop all db.  """

        Base.metadata.drop_all(self.engine)

    def get_rs(self):
        """ Support redis """

        return StrictRedis.from_url(self.config["datasets"])
