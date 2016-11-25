from services.user.user import *
from system.test import *


def test_service(app):
    service = app.create(UserService)
    app.get(service.db.add)
    service.add_user(conn_id='a', user_name='b', email="c", role='d')
    user = app.get_result
    assert user.conn_id == 'a'
    assert user.user_name == 'b'
    assert user.mail_address == 'c'
    assert user.role == 'd'
