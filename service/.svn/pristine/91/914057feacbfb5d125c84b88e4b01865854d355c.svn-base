from services.log.log import *
from system.test import *


@fixture
def service(app):
    service = app.create(LogService)
    return service


def test_add_log(service):
    log = {"content": "info"}
    service.add_log(log)
    result = service.log.find_one(log)
    assert result["content"] == "info" 
