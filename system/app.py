from nameko.rpc import rpc, RpcProxy
from nameko.events import EventDispatcher, event_handler
from dao import *


class App(object):

    """
    Supply database and datasets.

    Returns
    -------
    - db : sqlalchemy.orm.session.Session
    - rs : redis.client.StrictRedis

    Examples
    --------
    Create a new application.

    >>> from system.app import App
    >>> app = App()
    >>> app.db
    ''
    >>> app.rs
    ''
    """

    db = ""
    rs = ""

    def init(self):
        data = Db()
        self.db = data.get_db()
        self.rs = data.get_rs()

    def obj2dict(self, obj):
        return dict((key, obj.__dict__[key])\
               for key in obj.__dict__ \
               if not key.startswith("_"))
