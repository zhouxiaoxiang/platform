from system.app import *
from system.log import Log


class LogService(App):

    """
    Support all syslog.

    >>> from nameko.standalone.rpc import ClusterRpcProxy
    >>> CONFIG = {"AMQP_URI":"amqp://guest:guest@localhost"}
    >>> with ClusterRpcProxy(CONFIG) as services:
    >>>     result = services.log_service.add_log({"content": "info"})
    """

    name = "log_service"

    def __init__(self):
        super(LogService, self).init()

    @rpc
    def add_log(self, content):
        """ Add a log. """
        
        self.log = Log("sysLog").get()
        result = self.log.insert_one(content)
        return result.acknowledged
