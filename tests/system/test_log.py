#!/usr/bin/env python
# -*- coding: utf-8 -*-

from system.log import *
from logging import Logger
from pymongo.collection import Collection


def test_SysLog():
    log = SysLog("test_SysLog").get()
    assert isinstance(log, Logger)

def test_SysEventLog():
    log = SysEventLog("test_SysEventLog").get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

def test_UserEventLog():
    log = UserEventLog("test_UserEventLog").get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

def test_StockEventLog():
    log = StockEventLog("test_StockEventLog").get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None


def test_NopickedEventLog():
    log = NopickedEventLog("test_NopickedEventLog").get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

