from services.user.user import *
from system.test import *


@fixture
def service(app):
    service = app.create(UserService)
    service.add_user(conn_id='conn_id',
                     user_name='user_name',
                     mail_address='mail_address',
                     role='role',
                     name='name',
                     cell_phone='cell_phone',
                     company='company',
                     all_kiosks=0,
                     alert_same_kiosk=0,
                     alert_all_kiosk=0)
    return service


def test_add_user(service):
    user = service.db.query(Users).first()
    assert user.conn_id == 'conn_id'
    assert user.user_name == 'user_name'
    assert user.mail_address == 'mail_address'
    assert user.role == 'role'


def test_update_users_conn_id(service):
    service.update_users_conn_id('new_conn_id', 'conn_id')
    user = service.db.query(Users).first()
    assert user.conn_id == 'new_conn_id'


def test_get_user_info_by_email(service):
    user = service.get_user_info_by_email('mail_address')
    assert user["mail_address"] == 'mail_address'


def test_get_users(service):
    users = service.get_users('conn_id')
    assert users[0]['conn_id'] == 'conn_id'


def test_get_users_count(service):
    count = service.get_users_count('conn_id')
    assert count == 1
