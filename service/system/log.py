import logging
import mogo
from system.conf import Config


class Log(object):
    """ 
    Create log handler 

    Modules
    -------
    - sysLog
    - sysEventLog
    - userEventLog 
    - stockEventLog
    - nopickedEventLog

    Returns
    -------
    Collection

    Examples
    --------
    >>> from system.log import Log
    >>> log = Log("module").get()
    >>> result = log.insert_one({"count":1})
    >>> result.acknowledged
    True
    """ 

    def __init__(self, module=""):
        """ Require server info """

        conf = Config()['log'][module]
        self.host = conf['host']
        self.db = conf['db']
        self.tb = conf['tb']

    def get(self):
        """ Return log handler """

        self.conn = mogo.connect(self.db, self.host)
        self.log = self.conn[self.db][self.tb]
        return self.log
