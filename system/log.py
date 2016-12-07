import logging
import mogo
from mongolog.handlers import MongoHandler
from system.conf import Config
from abc import *


class _log(object):
    """ Log based on mogo """
    
    def __init__(self):
        raise "Abstractmethod"

    def connect(self):
        """ Establish a connection to db.  """

        self.conn = mogo.connect(self.db, self.host)
        self.log = self.conn[self.db][self.tb]

    def config(self, logType=""):
        """ Get host/db/tb """

        conf = Config()['log'][logType]
        self.host = conf['host']
        self.db = conf['db']
        self.tb = conf['tb']
        self.connect()

    def get(self):
        """ Return log handler """

        return self.log


class System_sysLog(_log):
    """ 
    Create syslog handler 

    Examples
    --------
    >>> import logging
    >>> from system.log import System_sysLog 
    >>> log = System_sysLog("my module").get()
    >>> log.debug("foo")
    >>> log.error("foo")
    >>> log.fatal("foo")
    >>> log.info("foo")
    >>> log.log(logging.DEBUG, "foo")
    """

    def __init__(self, module="test"):
        self.module = module
        self.config("sysLog")

    def connect(self):
        self.log = logging.getLogger(self.module)
        self.log.setLevel(logging.DEBUG)
        self.log.addHandler(MongoHandler.to(self.tb, self.db, self.host))

    def get(self):
        """ Return logging.Logger """

        return self.log


class System_sysEventLog(_log):
    """ 
    Create event log handler 

    Returns
    -------
    Collection

    Examples
    --------
    >>> from system.log import System_sysEventLog
    >>> log = System_sysEventLog().get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """

    def __init__(self, logType="sysEventLog"):
        self.config(logType)


class System_userEventLog(_log):
    """ Create user event log handler 

    Examples
    --------
    >>> from system.log import System_userEventLog
    >>> log = System_userEventLog().get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """

    def __init__(self, logType="userEventLog"):
        self.config(logType)


class System_stockEventLog(_log):
    """ Create stock event log handler 

    Examples
    --------
    >>> from system.log import System_stockEventLog
    >>> log = System_stockEventLog().get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """

    def __init__(self, logType="stockEventLog"):
        self.config(logType)


class System_nopickedEventLog(_log):
    """ Create nopicked event log handler 

    Examples
    --------
    >>> from system.log import System_nopickedEventLog
    >>> log = System_nopickedEventLog().get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """

    def __init__(self, logType="nopickedEventLog"):
        self.config(logType)
