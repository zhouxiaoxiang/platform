from nameko.rpc import rpc, RpcProxy
from dao import *
from mockredis import *
from mock import *
from pytest import *

class Mock_app(object):
    """
    Platform App for test

    Examples
    --------
    >>> from system.test import *
    >>> app = Mock_app()
    >>> app.base
    'system.app.App.'
    >>> app.base_methods
    ['rs', 'db', 'init']
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

    def create(self, name):
        self.service = name()
        return self.service

    def get(self, attr):
        attr.side_effect = self.get_service

    def get_service(self, args):
        self.get_result = args
        
    def set(self, attr, value):
        attr.return_value = value

@fixture
def app(monkeypatch):
    """
    Create platform App for test
    """

    mock_app = Mock_app()
    mock_app.start(monkeypatch)

    return mock_app
