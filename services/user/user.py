#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import date, datetime, timedelta
from sqlalchemy import Column, Integer, String, create_engine, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from nameko.rpc import rpc, RpcProxy

Base = declarative_base()
engine = create_engine('mysql://root:root@localhost/test?charset=utf8')


class Users(Base):
    __tablename__ = 'users'
    id_ai = Column(
        types.Integer(),
        nullable=False,
        unique=None,
        default=None,
        primary_key=True,
        autoincrement=True)
    conn_id = Column(
        types.Unicode(255), nullable=True, unique=None, default=u'')
    user_name = Column(
        types.Unicode(255), nullable=True, unique=None, default=u'')
    role = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    mail_address = Column(
        types.Unicode(255), nullable=True, unique=None, default=u'')
    cell_phone = Column(
        types.Unicode(20), nullable=True, unique=None, default=u'')
    company = Column(
        types.Unicode(255), nullable=True, unique=None, default=u'')
    notes = Column(
        types.Unicode(1024), nullable=True, unique=None, default=u'')
    state = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    all_kiosks = Column(types.Integer(), nullable=True, unique=None, default=0)
    alert_same_kiosk = Column(
        types.Integer(), nullable=True, unique=None, default=1)
    alert_all_kiosk = Column(
        types.Integer(), nullable=True, unique=None, default=0)
    verify_code = Column(
        types.Unicode(20), nullable=True, unique=None, default=u'')
    add_time = Column(
        types.DateTime(),
        nullable=True,
        unique=None,
        default=u'0000-00-00 00:00:00')
    last_update_time = Column(
        types.DateTime(),
        nullable=True,
        unique=None,
        default=u'0000-00-00 00:00:00')
    add_time_int = Column(
        types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(
        types.Integer(), nullable=True, unique=None, default=0)


Base.metadata.create_all(engine)
session = sessionmaker(engine)()

CONFIG = {'AMQP_URI': 'amqp://guest:guest@localhost/'}


class UserService(object):

    name = "user_service"

    def __init__(self, db=session):
        self.db = db

    @rpc
    def add(self,
            conn_id,
            user_name,
            email,
            role,
            client_name=None,
            cell_phone='',
            company='',
            all_kiosks=0,
            alert_same_kiosk=0,
            alert_all_kiosk=0):
        current_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        current_time = int(time.time())

        user = Users()
        user.conn_id = conn_id
        user.user_name = user_name or email
        user.role = role
        user.name = client_name
        user.mail_address = email
        user.state = "active"
        user.cell_phone = cell_phone
        user.company = company
        user.all_kiosks = all_kiosks
        user.alert_same_kiosk = alert_same_kiosk
        user.alert_all_kiosk = alert_all_kiosk
        user.add_time = current_date
        user.add_time_int = current_time
        user.last_update_time = current_date
        user.last_update_time_int = current_time

        self.db.add(user)
        self.db.commit()

        return True

    @rpc
    def delete(self, email):
        self.db.query(Users).filter(Users.mail_address == email).delete()
        self.db.flush()
