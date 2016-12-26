from datetime import datetime as dt

from oriole.app import *
from oriole.log import Log


class ConnWebLogService(App):

    """
    Support all syslog.

    >>> from nameko.standalone.rpc import ClusterRpcProxy
    >>> CONFIG = {"AMQP_URI":"amqp://guest:guest@localhost"}
    >>> with ClusterRpcProxy(CONFIG) as services:
    >>>     result = services.conn_web_log_service.add_log({"content": "info"})
    """

    name = "conn_web_log_service"

    def __init__(self):
        super(ConnWebLogService, self).init()
        self.log = Log("connWebLog").get()

    @rpc
    def add_log(self, content):
        """ Add a log. """

        content["time"] = dt.now()
        result = self.log.insert_one(content)
        return str(result.inserted_id)
