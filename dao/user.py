from system.db import *

class Users(Base):
    __tablename__ = 'users'
    id_ai = Column( types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column( types.Unicode(255), nullable=True, unique=None, default=u'')
    user_name = Column( types.Unicode(255), nullable=True, unique=None, default=u'')
    role = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    mail_address = Column( types.Unicode(255), nullable=True, unique=None, default=u'')
    cell_phone = Column( types.Unicode(20), nullable=True, unique=None, default=u'')
    company = Column( types.Unicode(255), nullable=True, unique=None, default=u'')
    notes = Column( types.Unicode(1024), nullable=True, unique=None, default=u'')
    state = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    all_kiosks = Column(types.Integer(), nullable=True, unique=None, default=0)
    alert_same_kiosk = Column( types.Integer(), nullable=True, unique=None, default=1)
    alert_all_kiosk = Column( types.Integer(), nullable=True, unique=None, default=0)
    verify_code = Column( types.Unicode(20), nullable=True, unique=None, default=u'')
    add_time = Column( types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column( types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column( types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column( types.Integer(), nullable=True, unique=None, default=0)

