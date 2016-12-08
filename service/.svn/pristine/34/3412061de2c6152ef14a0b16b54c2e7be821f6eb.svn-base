#!/usr/bin/env python
# -*- coding: utf-8 -*-

from system.log import *
from logging import Logger
from pymongo.collection import Collection


def test_System_sysLog():
    log = System_sysLog().get()
    assert isinstance(log, Logger)

def test_System_sysEventLog():
    log = System_sysEventLog().get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

def test_System_userEventLog():
    log = System_userEventLog().get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

def test_System_stockEventLog():
    log = System_stockEventLog().get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None


def test_System_nopickedEventLog():
    log = System_nopickedEventLog().get()
    assert isinstance(log, Collection)
    assert log.insert_one({"test":1}) is not None

