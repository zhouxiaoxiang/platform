from services.log.conn_web_log import *
from oriole.test import *


@fixture
def service(app):
    web_service = app.create(ConnWebLogService)
    return web_service


def test_add_log(service):
    log = {"content": "info"}
    service.add_log(log)
    result = service.log.find_one(log)
    assert result["content"] == "info" 
