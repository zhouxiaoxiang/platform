from nameko.rpc import rpc, RpcProxy
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
    """

    db = ""
    rs = ""

    def init(self):
        data = Db()
        self.db = data.get_db()
        self.rs = data.get_rs()
