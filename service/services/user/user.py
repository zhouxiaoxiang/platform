from system.app import *
import time
from datetime import date, datetime, timedelta


class UserService(App):

    """
    Support all user operations.

    >>> from nameko.standalone.rpc import ClusterRpcProxy
    >>> CONFIG = {"AMQP_URI":"amqp://guest:guest@localhost"}
    >>> with ClusterRpcProxy(CONFIG) as services:
    >>>     result = services.user_service.add_user(conn_id='10', 
    >>>              user_name='', mail_address="x@y", role='')
    """

    name = "user_service"

    def __init__(self):
        super(UserService, self).init()

    @rpc
    def add_user(self, conn_id, user_name, mail_address, 
                 role, name=None, cell_phone='', company='', 
                 all_kiosks=0, alert_same_kiosk=0, 
                 alert_all_kiosk=0):
        """ Add a user. """
        
        current_date = datetime.utcnow()
        current_time = int(time.time())

        user = Users()
        user.conn_id = conn_id
        user.user_name = user_name or mail_address
        user.role = role
        user.name = name
        user.mail_address = mail_address
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

    @rpc
    def update_users_conn_id(self, conn_id, old_conn_id):
        """ Update conn_id """

        self.db.query(Users).\
                filter(Users.conn_id == old_conn_id).\
                update({Users.conn_id: conn_id})

    @rpc
    def get_user_info_by_email(self, email):
        """ return user info by email """

        user = self.db.query(Users).\
                filter(Users.mail_address == email).\
                first()
        return self.obj2dict(user)

    @rpc
    def get_users(self, conn_id, current_user_role=None, 
            search_key=None, sort_key=None, sort_order=None, 
            limit=None, offset=None):
        """ get the users by conn ID """

        rows = self.db.query(Users).filter(Users.conn_id == conn_id)
        if current_user_role == "operator":
            return []

        if current_user_role == "admin":
            rows = rows.filter(Users.role != "sadmin")

        if search_key:
            key = "%%%s%%" % search_key
            rows = rows.filter(or_(Users.user_name.like(key),
                Users.name.like(key), Users.mail_address.like(key)))

        if sort_key:
            sort = getattr(Users, sort_key, None)
            if sort is not None:
                if str(sort_order).lower() == "desc":
                    rows = rows.order_by(sort.desc())
                else:
                    rows = rows.order_by(sort)
        if limit:
            rows = rows.limit(limit)

        if offset:
            rows = rows.offset(offset)

        result = rows.all()

        if sort_key:
            if sort_key == "role":
                if str(sort_order).lower() == "desc":
                    # to compare the index of ('admin')
                    result.sort(
                        lambda x, y: cmp(x.role.find("admin"), y.role.find("admin")))
                else:
                    result.sort(
                        lambda x, y: cmp(y.role.find("admin"), x.role.find("admin")))
        return [ self.obj2dict(user) for user in result ] if result else []

    @rpc
    def get_users_count(self, conn_id, current_user_role=None, search_key=None):
        """ get the users by conn ID """

        rows = self.db.query(Users).filter(Users.conn_id == conn_id)
        if current_user_role == "operator":
            return 0
        if current_user_role == "admin":
            rows = rows.filter(Users.role != "sadmin")

        if search_key:
            key = "%%%s%%" % search_key
            rows = rows.filter(or_(Users.user_name.like(key),
                                   Users.name.like(key),
                                   Users.mail_address.like(key)))

        return rows.count()

    @rpc
    def set_user_info(self, email, username=None, role=None,
                      notes=None, state=None, name=None,
                      cell_phone=None, company=None, all_kiosks=None,
                      same_assign=None, alert_all=None):
        """ edit the userinfo """

        user = self.db.query(Users).filter(
            Users.mail_address == email).first()
        if username is not None:
            user.username = username
        if role is not None:
            user.role = role
        if notes is not None:
            user.notes = notes
        if state is not None:
            user.state = state
        if name is not None:
            user.name = name
        if same_assign is not None:
            user.alert_same_kiosk = same_assign
        if alert_all is not None:
            user.alert_all_kiosk = alert_all
        if cell_phone:
            user.cell_phone = cell_phone
        if company:
            user.company = company
        if all_kiosks is not None:
            user.all_kiosks = all_kiosks
        user.last_update_time = datetime_utils.current_time()
        user.last_update_time_int = datetime_utils.get_interger_time()
        self.db.flush()

    @rpc
    def delete_user(self, email):
        """ Delete user """

        self.db.query(Users).filter(Users.mail_address == email).delete()
        self.db.flush()

    @rpc
    def reactivate_user(self, user_email):
        """ Reactivate user """

        user = self.db.query(Users).filter(
            Users.mail_address == user_email).first()
        user.state = 'active'
        self.db.flush()

    @rpc
    def get_user_role_msg(self, email):
        """ Get user's role """

        user_info = self.db.query(Users).filter(
            Users.mail_address == email).first()
        if user_info:
            return user_info.role
        else:
            return ""

    @rpc
    def save_user_role_msg(self, email, roles):
        """ Save user's role """

        user_info = self.db.query(Users).filter(
            Users.mail_address == email).first()
        if user_info:
            user_info.role = roles
        self.db.flush()

    @rpc
    def get_client_user_list_count(self, conn_id, search_key=None,
                                   role=None, state=None):
        """ Get user list count """

        sql = self.db.query(Users).filter(Users.conn_id == conn_id)
        if role:
            sql = sql.filter(Users.role == role)
        if state:
            sql = sql.filter(Users.state == state)
        if search_key:
            key = "%%%s%%" % search_key
            sql = sql.filter(or_(Users.user_name.like(key),
                                 Users.name.like(key),
                                 Users.notes.like(key)))
        return sql.count()

    @rpc
    def delete_user_by_conn_id(self, conn_id):
        """ Delete user """

        self.db.query(Users).filter(Users.conn_id == conn_id).delete()
