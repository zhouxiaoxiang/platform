from nameko.rpc import rpc, RpcProxy
from dao import *
from mockredis import *
from mock import *
from pytest import *
from mocksqlalchemy import scoped_sessionmaker_mock
import functools


class Mock_app(object):
    """
    Platform App for test
    """

    base = "system.app.App."
    base_methods = ["rs", "db", "init"]

    def start(self, patch):
        methods = [self.rs, self.db, self.init]
        methods_zip = zip(self.base_methods, methods)
        for base_method, method in methods_zip:
            patch.setattr(self.base + base_method, method())

    def rs(self):
        return mock_redis_client()

    def db(self):
        return MagicMock()

    def init(self):
        return lambda self: None


@fixture(autouse=True)
def service(monkeypatch):
    """
    Create platform App for test
    """

    mock_app = Mock_app()
    mock_app.start(monkeypatch)
