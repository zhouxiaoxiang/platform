#!/usr/bin/env python
# -*- coding: utf-8 -*-

from system.log import *
from logging import Logger
from pymongo.collection import Collection


def test_System_sysLog():
    log = System_sysLog("test_SysLog").get()
    assert isinstance(log, Logger)

def test_System_sysEventLog():
    log = System_sysEventLog("test_SysEventLog").get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

def test_System_userEventLog():
    log = System_userEventLog("test_UserEventLog").get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

def test_System_stockEventLog():
    log = System_stockEventLog("test_StockEventLog").get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None


def test_System_nopickedEventLog():
    log = System_nopickedEventLog("test_NopickedEventLog").get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

