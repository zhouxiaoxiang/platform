import pytest
from services.user.user import *


class DB:

    def __init__(self):
        self.objs = []

    def add(self, obj):
        self.objs.append(obj)

    def commit(self):
        pass

    def query(self):
        return self.objs

@pytest.fixture(scope="module")
def newSession():
    return DB()


def test_UserService(newSession):
    service = UserService()
    service.add_user(conn_id='9', user_name='', email="x@y", role='')

    user = service.db.query(Users).filter_by(mail_address = "x@y").first()
    assert user is not None
    assert user.mail_address == 'x@y'
