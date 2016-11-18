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

    >>> from system.app import *
    >>> class UserService(App):
    >>>     @rpc
    >>>     def test(self):
    >>>         self.db.query(Users).all()
    >>>         self.rs.set("foo", 1)
    """

    _db = System_db()
    db = _db.get_db()
    rs = _db.get_rs()

