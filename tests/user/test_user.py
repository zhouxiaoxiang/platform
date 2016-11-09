#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from services.user.user import *
from nameko.standalone.rpc import ClusterRpcProxy


@pytest.fixture
def newSession():
    engine = create_engine('mysql://root:root@localhost/test?charset=utf8')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session_cls = sessionmaker(engine)
    return session_cls()


def test_UserService(newSession):
    service = UserService(newSession)
    service.add(conn_id='9', user_name='', email="x@y", role='')
    assert newSession.query(Users.mail_address).one() == (u'x@y', )


#def test_UserService_from_client():
#    with ClusterRpcProxy(CONFIG) as cli:
#        result = cli.user_service.add(
#            conn_id='10', user_name='', email="x@y", role='')
#        assert result is True
