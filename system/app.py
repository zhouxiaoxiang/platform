from nameko.rpc import rpc, RpcProxy
from dao import *

        
class App(object):
    """
    Supply database and datasets.

    Examples
    --------
    Create a new application.

    >>> from system.app import *
    >>> class UserService(App):
    >>>     @rpc
    >>>     def test(self):
    >>>         print(self.db)
    >>>         print(self.rs)
    """

    system_db = System_db()
    db = system_db.create_db()
    rs = system_db.create_rs()

