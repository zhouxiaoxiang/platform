import logging
import mogo
from mongolog.handlers import MongoHandler


class _log(object):
    """ Log based on mogo """

    host = "localhost"
    db = None
    tb = None


    def __init__(self, module="test"):
        """ Establish a connection to db.  """

        self.conn = mogo.connect(self.host)
        self.log = self.conn[self.db][self.tb]
        self.module = module


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

    db = "sysLog"
    tb = "log"

    def __init__(self, module="test"):
        self.log = logging.getLogger(module)
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
    >>> log = System_sysEventLog("my module").get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """

    db = "eventLog"
    tb = "sys"

    def __init__(self,  module="test"):
        super(System_sysEventLog, self).__init__()


class System_userEventLog(_log):
    """ Create user event log handler 

    Examples
    --------
    >>> from system.log import System_userEventLog
    >>> log = System_userEventLog("my module").get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """

    db = "eventLog"
    tb = "user"

    def __init__(self,  module="test"):
        super(System_userEventLog, self).__init__()


class System_stockEventLog(_log):
    """ Create stock event log handler 

    Examples
    --------
    >>> from system.log import System_stockEventLog
    >>> log = System_stockEventLog("my module").get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """

    db = "eventLog"
    tb = "stock"

    def __init__(self,  module="test"):
        super(System_stockEventLog, self).__init__()


class System_nopickedEventLog(_log):
    """ Create nopicked event log handler 

    Examples
    --------
    >>> from system.log import System_nopickedEventLog
    >>> log = System_nopickedEventLog("my module").get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """

    db = "eventLog"
    tb = "nopicked"

    def __init__(self,  module="test"):
        super(System_nopickedEventLog, self).__init__()

