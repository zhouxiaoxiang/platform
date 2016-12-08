from system.db import *


class ConnEvents(Base):
    __tablename__ = 'conn_events'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    user_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ip = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    category = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    action = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    data1 = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    data2 = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    data3 = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    data4 = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    data5 = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    time_recorded = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    time_updated = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    time_recorded_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    time_updated_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    state = Column(types.Unicode(255), nullable=True, unique=None, default=u'open')


class MachineStockEvents(Base):
    __tablename__ = 'machine_stock_events'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    fina_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    fina_cate_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    unit_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    action_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    action_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    type = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    notes = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    receipt_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    operator = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class MachineSysEvents(Base):
    __tablename__ = 'machine_sys_events'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    event_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    action = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    description = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class Users(Base):
    __tablename__ = 'users'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    user_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    role = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    mail_address = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    cell_phone = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    company = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    state = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    all_kiosks = Column(types.Integer(), nullable=True, unique=None, default=0)
    alert_same_kiosk = Column(types.Integer(), nullable=True, unique=None, default=1)
    alert_all_kiosk = Column(types.Integer(), nullable=True, unique=None, default=0)
    verify_code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class UserKiosk(Base):
    __tablename__ = 'user_kiosk'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    user_email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    type = Column(types.Integer(), nullable=True, unique=None, default=1)


class UserEvents(Base):
    __tablename__ = 'user_events'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ip = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    category = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sub_category = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    action = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    action_level = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    data1 = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    data2 = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    data3 = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    data4 = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    data5 = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class UserRole(Base):
    __tablename__ = 'user_role'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    role_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
