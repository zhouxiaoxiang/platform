from services.log.user_event_log import *
from oriole.test import *


@fixture
def service(app):
    user_event_log_service = app.create(UserEventLogService)
    return user_event_log_service


@fixture
def service_for_get_log(app):
    user_event_log_service = app.create(UserEventLogService)
    logs = [
        {
            'client_id': 'cereson',
            'client_name': '华屹',
            'host_id': 'cerehost',
            'host_name': 'Cereson Inc.',
            'category': '机器/商品/活动',
            'sub_category': '市场营销',
            'action': '1111编辑游戏奖励',
            'email': 'vincent.chen@cereson.com',
            'action_level': 'client',
            'data1': 'pintu',
            'data5': '活动描述:拼图游戏2->拼图游戏2x',
            'data_key': '',
            'ip': '192.168.1.115',
            'conn_web_view_log_id': '585ccd4f1d41c827bfb37fa1'
        }, {
            'client_id': '',
            'client_name': '',
            'host_id': 'cerehost',
            'host_name': 'Cereson Inc.',
            'category': 'CONN访问',
            'sub_category': '登录/登出',
            'action': '登录账号',
            'email': 'tommey.li@cereson.com',
            'action_level': 'host',
            'data1': 'tommey.li@cereson.com登录',
            'data_key': 'tommey.li@cereson.com',
            'ip': '192.168.1.115',
            'conn_web_view_log_id': '585cd45d1d41c827bfb37fd9'
        }, {
            'client_id': 'cereson',
            'client_name': '华屹',
            'host_id': 'cerehost',
            'host_name': 'Cereson Inc.',
            'category': '机器/商品/活动',
            'sub_category': '市场营销',
            'action': '2222编辑促销活动',
            'email': 'kitch.huang@cereson.com',
            'action_level': 'master',
            'data1': '1d2ff896-1fd1-4435-a2e1-264f41520de2',
            'data2': '47258c47-9543-4da3-86cc-eb8c543a7923',
            'data_key': '',
            'ip': '192.168.1.115',
            'conn_web_view_log_id': '585cc2731d41c827bfb37ee1',
            'data3': 'R1S-A002,R1S-A006,R2-A019,R2S-A015'
        }
    ]
    for log in logs:
        user_event_log_service.add_log(log)
    return user_event_log_service


def test_add_log(service):
    log = {"content": "info"}
    service.add_log(log)
    result = service.log.find_one(log)
    assert result["content"] == "info" 


def test_get_log_count(service_for_get_log):
    result = service_for_get_log.get_log({"get_count": True, 'host_id': 'cerehost'})
    assert isinstance(result, int)
    assert result == 3


def test_get_log_for_client_id(service_for_get_log):
    result = service_for_get_log.get_log({"get_count": True, 'client_id': 'cereson'})
    assert result == 2


def test_get_log_for_date(service_for_get_log):
    result = service_for_get_log.get_log({
        "get_count": True,
        'start_date': '2016-12-22 00:00:00',
        'end_date': '2016888-1233334-30 23:59:59'
    })
    assert result == 3

    result = service_for_get_log.get_log({
        "get_count": True,
        'start_date': '2015-12-22 00:00:00',
        'end_date': '2015-12-28 23:59:59'
    })
    assert result == 0


def test_get_log_for_category(service_for_get_log):
    result = service_for_get_log.get_log({'category': 'CONN访问'})
    assert len(result) == 1
    result = service_for_get_log.get_log({'category': '机器/商品/活动'})
    assert len(result) == 2


def test_get_log_for_action_level(service_for_get_log):
    result = service_for_get_log.get_log({"get_count": True, 'action_level': 'master'})
    assert result == 3
    result = service_for_get_log.get_log({'action_level': 'host'})
    assert len(result) == 2
    result = service_for_get_log.get_log({"get_count": True, 'action_level': 'client'})
    assert result == 1


def test_get_log_for_sort(service_for_get_log):
    result = service_for_get_log.get_log({'category': '机器/商品/活动', 'sort_key': 'action', 'sort_order': 'asc'})
    assert result[0]['action'].startswith('11') is True
    result = service_for_get_log.get_log({'category': '机器/商品/活动', 'sort_key': 'action', 'sort_order': 'des'})
    assert result[0]['action'].startswith('22') is True


def test_get_log_for_offset(service_for_get_log):
    result = service_for_get_log.get_log({'offset': 2, 'limit': 10})
    assert len(result) == 1
