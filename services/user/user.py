""" Maintain all user operations.  """

from system.app import *
import time
from datetime import date, datetime, timedelta


class UserService(object):

    """ Support all user operations.

    Examples::

        from nameko.standalone.rpc import ClusterRpcProxy
        with ClusterRpcProxy({"AMQP_URI":"amqp://guest:guest@localhost"}) as services:
            result = services.user_service.add(conn_id='10', user_name='', email="x@y", role='')
    """

    name = "user_service"

    def __init__(self, db=system_db):
        self.db = db

    @rpc
    def add_user(
        self, conn_id, user_name, email, role, client_name=None, cell_phone='',
            company='', all_kiosks=0, alert_same_kiosk=0, alert_all_kiosk=0):
        """ Add a user """

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

    @rpc
    def get_user_email(self, conn_ids, role=None):
        rows = self.db.query(Users).filter(Users.role == role)
        if conn_ids is not None:
            ore = None
            for m_ in conn_ids:
                ore = or_(ore, Users.conn_id == m_)
            rows = rows.filter(ore)
        return rows

    @rpc
    def get_user_info(self, email):
        return self.db.query(Users).filter(Users.mail_address == email).first()

    @rpc
    def update_users_conn_id(self, conn_id, old_conn_id):
        self.db.query(Users)\
            .filter(Users.conn_id == old_conn_id)\
                 .update({Users.conn_id: conn_id})

    @rpc
    def get_user_info_by_email(self, email):
        """ return user info by email
        @param email(str):
        """
        return self.db.query(Users)\
            .filter(Users.mail_address == email).first()

    @rpc
    def get_user_sadmins(self, conn_id):
        rows = self.db.query(Users).filter(Users.conn_id == conn_id)\
            .filter(Users.role == "sadmin").all()
        return [row.mail_address for row in rows] if rows else []

    @rpc
    def get_licence_version(self, email):
        user_info = self.db.query(Users.conn_id).filter(
            Users.mail_address == email).first()
        return self.db.query(ConnIds.license_id).filter(ConnIds.conn_id == user_info[0]).first()

    @rpc
    def get_user_role(self, email):
        user_info = self.db.query(Users.role).filter(
            Users.mail_address == email).first()
        if user_info[0] == "sadmin":
            return "sadmin"
        else:
            return self.db.query(UserRole.role_id).filter(UserRole.email == email).all()

    @rpc
    def get_users(self, conn_id, current_user_role=None, search_key=None,                                                                                                                             sort_key=None, sort_order=None, simit=None, offset=None):
        """ get the users by conn ID
        @param conn_id: str
        @param current_user_role: str
        @param search_key: str
        @return: user list
        @rtype: [], list with Users Object
        """
        rows = self.db.query(Users).filter(Users.conn_id == conn_id) 
        if current_user_role == "operator":
            return [] 

        if current_user_role == "admin":
            rows = rows.filter(Users.role != "sadmin")

        if search_key:
            key = "%%%s%%" % search_key
            rows = rows.filter(or_(Users.user_name.like(key),
                                   Users.name.like(key),
                                   Users.mail_address.like(key)))

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

        # sort by "role"
        if sort_key:
            if sort_key == "role":
                if str(sort_order).lower() == "desc":
                    # to compare the index of ('admin')
                    result.sort(
                        lambda x, y: cmp(x.role.find("admin"), y.role.find("admin")))
                else:
                    result.sort(
                        lambda x, y: cmp(y.role.find("admin"), x.role.find("admin")))
        return result

    @rpc
    def get_users_count(self, conn_id, current_user_role=None, search_key=None):
        """ get the users by conn ID

        @param conn_id: str
        @param current_user_role: str
        @param search_key: str
        @return: user count
        @rtype: int
        """
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
        """ edit the userinfo

        @param username: the username of the login user
        @param role: the role of the login user
        @param notes: the notes of the login user
        @param state: the state of the login user
        @param name: the name of the login user
        @return: return the object of Users(current editing).
        """
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
        self.db.query(Users).filter(Users.mail_address == email).delete()
        self.db.flush()

    @rpc
    def reactivate_user(self, user_email):
        user = self.db.query(Users).filter(
            Users.mail_address == user_email).first()
        user.state = 'active'
        self.db.flush()

    @rpc
    def get_user_role_msg(self, email):
        user_info = self.db.query(Users).filter(
            Users.mail_address == email).first()
        if user_info:
            return user_info.role
        else:
            return ""

    @rpc
    def save_user_role_msg(self, email, roles):
        user_info = self.db.query(Users).filter(
            Users.mail_address == email).first()
        if user_info:
            user_info.role = roles
        self.db.flush()

    @rpc
    def get_client_user_list_count(self, host_id, conn_id, search_key=None,
                                   role=None, state=None):
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
    def get_client_user_list(
        self, host_id, conn_id, search_key=None, role=None,
                             state=None, sort_key=None, sort_order=None,
                             limit=None, offset=None):
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
        if sort_key:
            sort = getattr(Users, sort_key, None)
            if sort is not None:
                if str(sort_order).lower() == "desc":
                    sql = sql.order_by(sort.desc())
                else:
                    sql = sql.order_by(sort)
        if limit:
            sql = sql.limit(limit)
        if offset:
            sql = sql.offset(offset)
        return sql.all()

    @rpc
    def delete_user_by_conn_id(self, conn_id):
        self.db.query(Users).filter(Users.conn_id == conn_id).delete()
