from system.db import *


class AlertAttachment(Base):
    __tablename__ = 'alert_attachment'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    alert_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    attachment_name = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    attachment_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class AlertQueue(Base):
    __tablename__ = 'alert_queue'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    alert_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    alert_type = Column(types.Unicode(45), nullable=True, unique=None, default=u'email')
    alert_subject = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    alert_content = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    alert_from = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    alert_cc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    from_app = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    priority = Column(types.Integer(), nullable=True, unique=None, default=3)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class AlertReceivers(Base):
    __tablename__ = 'alert_receivers'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    alert_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    receivers = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    sent_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    sent_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    sent = Column(types.Integer(), nullable=True, unique=None, default=0)


class Cfile(Base):
    __tablename__ = 'cfile'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    file_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    file_md5 = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    file_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    file_size = Column(types.Integer(), nullable=True, unique=None, default=0)
    file_type = Column(types.Unicode(50), nullable=True, unique=None, default=u'image')
    is_local = Column(types.Integer(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class ClientAd(Base):
    __tablename__ = 'client_ad'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    form = Column(types.Unicode(255), nullable=True, unique=None, default=u'mainform')
    ad_status = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    ad_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ad_mode = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    resolution = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    position = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    target_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    target_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    target_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    view_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    click_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class MachineScreenSaverFile(Base):
    __tablename__ = 'machine_screen_saver_file'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    file_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    file_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'0')
    file_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    file_md5 = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class ClientAdCvHistory(Base):
    __tablename__ = 'client_ad_cv_history'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    publish_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    ad_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    cv_type = Column(types.Integer(), nullable=True, unique=None, default=0)
    cv_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class ClientAdKiosk(Base):
    __tablename__ = 'client_ad_kiosk'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    form = Column(types.Unicode(255), nullable=True, unique=None, default=u'mainform')
    element_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    publish_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    ad_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')


class ClientAdMedia(Base):
    __tablename__ = 'client_ad_media'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    ad_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    media_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    media_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'0')
    media_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    media_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    media_md5 = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    lang = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    sequence = Column(types.Integer(), nullable=True, unique=None, default=0)
    upload_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    upload_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class ClientAdPublish(Base):
    __tablename__ = 'client_ad_publish'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    form = Column(types.Unicode(255), nullable=True, unique=None, default=u'mainform')
    position = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    template_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    template_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ad_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    ad_name = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosks = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    status = Column(types.Unicode(20), nullable=True, unique=None, default=u'active')
    publish_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    end_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class ClientGroupMachines(Base):
    __tablename__ = 'client_group_machines'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    group_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class ClientGroups(Base):
    __tablename__ = 'client_groups'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    group_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')


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


class ConnIds(Base):
    __tablename__ = 'conn_ids'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    site_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    location = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    tel = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    fax = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    mail_address = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    company_name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    contact = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    license_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class CouponKiosks(Base):
    __tablename__ = 'coupon_kiosks'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    coupon_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class CouponProducts(Base):
    __tablename__ = 'coupon_products'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    coupon_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    category = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    price = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sale_price = Column(types.Unicode(50), nullable=True, unique=None, default=u'')


class CouponTemplate(Base):
    __tablename__ = 'coupon_template'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    short_description = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    kiosk_type = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    fields = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class Coupons(Base):
    __tablename__ = 'coupons'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    coupon_template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    coupon_code = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    random_code = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_data = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    total_usage_limit = Column(types.Integer(), nullable=True, unique=None, default=0)
    fee_limit = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0)
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    all_items = Column(types.Integer(), nullable=True, unique=None, default=0)
    status = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    random_coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_usage_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_except_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_des = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    coupon_short_des = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class FinaCategory(Base):
    __tablename__ = 'fina_category'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    fina_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    pid = Column(types.Unicode(50), nullable=True, unique=None, default=u'0')
    pic_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'0')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class GProduct(Base):
    __tablename__ = 'g_product'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    gpid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    name_s = Column(types.Unicode(2550), nullable=True, unique=None, default=None)
    fina_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    market_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    manufacturer = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    model = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    description = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    is_id_card_presented_item = Column(types.Integer(), nullable=True, unique=None, default=0)
    is_date_sensitive = Column(types.Integer(), nullable=True, unique=None, default=0)
    main_pic_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    main_pic_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class GProductPic(Base):
    __tablename__ = 'g_product_pic'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    gpid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    pic_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'0')
    main_pic = Column(types.Boolean(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class GProductSpec(Base):
    __tablename__ = 'g_product_spec'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    gpid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    lang = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    variable = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    value = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    sequence = Column(types.Integer(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class KioskAlertEmails(Base):
    __tablename__ = 'kiosk_alert_emails'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    category = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    action = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    sent_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    sent_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    email_alert_sent = Column(types.Boolean(), nullable=True, unique=None, default=0)


class KioskOfflineDelayEmails(Base):
    __tablename__ = 'kiosk_offline_delay_emails'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    machine_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    offline_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    sent_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    sent_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    sent = Column(types.Integer(), nullable=True, unique=None, default=0)


class KioskQueue(Base):
    __tablename__ = 'kiosk_queue'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    kiosk = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    type = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    api = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    params = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    sequence_sensitive = Column(types.Integer(), nullable=True, unique=None, default=1)
    version_required = Column(types.Unicode(45), nullable=True, unique=None, default=u'0.1.0')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    sync_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    sync_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    state = Column(types.Integer(), nullable=True, unique=None, default=0)


class LastInput(Base):
    __tablename__ = 'last_input'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    input_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    input_value = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class Layout(Base):
    __tablename__ = 'layout'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    kiosk_type = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class LayoutElementPlugin(Base):
    __tablename__ = 'layout_element_plugin'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    display_name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    package_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    icon = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    widget_type = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    fields = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    version = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    file_md5 = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    file_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class LayoutElementPluginData(Base):
    __tablename__ = 'layout_element_plugin_data'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    layout_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    screen_id = Column(types.Unicode(500), nullable=True, unique=None, default=u'')
    element_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    plugin_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    plugin_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    data = Column(types.Unicode(3000), nullable=True, unique=None, default=u'')


class LayoutTemplate(Base):
    __tablename__ = 'layout_template'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    kiosk_type = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    resolution = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class LayoutTemplateScreen(Base):
    __tablename__ = 'layout_template_screen'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    form_name = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    background_pic = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    required_plugin_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    required_plugin = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class LayoutTemplateScreenElement(Base):
    __tablename__ = 'layout_template_screen_element'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    screen_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    top = Column(types.Integer(), nullable=True, unique=None, default=0)
    left = Column(types.Integer(), nullable=True, unique=None, default=0)
    width = Column(types.Integer(), nullable=True, unique=None, default=0)
    height = Column(types.Integer(), nullable=True, unique=None, default=0)
    plugin_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    plugin = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    pic = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class MachineConfig(Base):
    __tablename__ = 'machine_config'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    key = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    value = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class MachineInfo(Base):
    __tablename__ = 'machine_info'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    key = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    value = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class MachineProducts(Base):
    __tablename__ = 'machine_products'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    name_s = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    fina_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    market_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    is_critical = Column(types.Integer(), nullable=True, unique=None, default=0)
    is_id_card_presented_item = Column(types.Integer(), nullable=True, unique=None, default=0)
    is_date_sensitive = Column(types.Integer(), nullable=True, unique=None, default=0)
    pre_alert_time = Column(types.Integer(), nullable=True, unique=None, default=30)
    is_virtual = Column(types.Integer(), nullable=True, unique=None, default=0)
    is_gift = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_channel = Column(types.Integer(), nullable=True, unique=None, default=3)
    pick_method = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    package_length = Column(types.Float(), nullable=True, unique=None, default=0)
    package_width = Column(types.Float(), nullable=True, unique=None, default=0)
    package_height = Column(types.Float(), nullable=True, unique=None, default=0)
    slot_max_count = Column(types.Unicode(500), nullable=True, unique=None, default=u'')
    fetch_style = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    manufacturer = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    supplier_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    supplier_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    model = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    is_show = Column(types.Integer(), nullable=True, unique=None, default=1)
    description = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    service_phone = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    mismatch_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    reserve_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    lock_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    outside_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    has_outside = Column(types.Integer(), nullable=True, unique=None, default=0)
    outside_exp_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    state = Column(types.Unicode(45), nullable=True, unique=None, default=u'active')
    rating = Column(types.Float(), nullable=True, unique=None, default=0)
    rating_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    eject_weight = Column(types.Integer(), nullable=True, unique=None, default=0)
    pic_3d = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class MachineShoppingCarts(Base):
    __tablename__ = 'machine_shopping_carts'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_no = Column(types.Unicode(45), nullable=True, unique=None, default=u'0000')
    trs_time = Column(types.DateTime(), nullable=False, unique=None, default=u'0000-00-00 00:00:00', primary_key=True)
    trs_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    lang = Column(types.Unicode(10), nullable=True, unique=None, default=u'en_US')
    receipt_email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    test_mode = Column(types.Integer(), nullable=True, unique=None, default=0)
    cc_display = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    subtotal = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    charge_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_code = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    pick_code = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_discount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    upg_type = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    upg_oid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_payment_method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_auth_num = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_merchant_ref = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_auth_date = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    upg_card_brand = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_card_num = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    time_zone = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    card_type = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    customer_picture = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    misvend_done = Column(types.Integer(), nullable=True, unique=None, default=0)
    phone_num = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    payment_rate = Column(types.Numeric(precision=20, scale=10), nullable=True, unique=None, default=0.0000000000)
    currency_symbol = Column(types.Unicode(20), nullable=True, unique=None, default=u'CNY')
    exchange_rate = Column(types.Numeric(precision=20, scale=10), nullable=True, unique=None, default=0.0000000000)
    is_receipt_printed = Column(types.Integer(), nullable=True, unique=None, default=0)
    receipt_print_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    transfer_status = Column(types.Integer(), nullable=True, unique=None, default=0)
    transfer_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class MachineSlots(Base):
    __tablename__ = 'machine_slots'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    mismatch_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    reserve_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    lock_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    state = Column(types.Unicode(45), nullable=True, unique=None, default=u'empty')
    slot_region = Column(types.Unicode(11), nullable=True, unique=None, default=u'')
    slot_type = Column(types.Unicode(11), nullable=True, unique=None, default=u'l')
    heavy_slot = Column(types.Integer(), nullable=True, unique=None, default=0)
    x_start = Column(types.Float(), nullable=True, unique=None, default=0)
    y_start = Column(types.Float(), nullable=True, unique=None, default=0)
    width = Column(types.Float(), nullable=True, unique=None, default=0)
    height = Column(types.Float(), nullable=True, unique=None, default=0)
    real_height = Column(types.Float(), nullable=True, unique=None, default=0)
    real_width = Column(types.Float(), nullable=True, unique=None, default=0)
    threshold = Column(types.Integer(), nullable=True, unique=None, default=10)
    mismatch_err_msg = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    marked_by = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    marked_msg = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    slot_hole = Column(types.Unicode(10), nullable=True, unique=None, default=u'0')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    fetch_style = Column(types.Unicode(50), nullable=True, unique=None, default=u'default')


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


class MachineTransactions(Base):
    __tablename__ = 'machine_transactions'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_no = Column(types.Unicode(45), nullable=True, unique=None, default=u'0000')
    test_mode = Column(types.Integer(), nullable=True, unique=None, default=0)
    cc_display = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    fina_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    fina_cate_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    supplier_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    supplier_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    unit_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    original_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    real_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    trs_time = Column(types.DateTime(), nullable=False, unique=None, default=u'0000-00-00 00:00:00', primary_key=True)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    trs_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    type = Column(types.Unicode(45), nullable=True, unique=None, default=u'sale')
    state = Column(types.Unicode(45), nullable=True, unique=None, default=u'proccessing')
    notes = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    refund_notes = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    enable_sale_tax = Column(types.Unicode(45), nullable=True, unique=None, default=u'on')
    unit_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    deliver_pics = Column(types.Unicode(3000), nullable=True, unique=None, default=u'')
    error_msgs = Column(types.Unicode(3000), nullable=True, unique=None, default=u'')
    error_type = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    operator = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    duration_time = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    coupon_code = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    pick_code = Column(types.Unicode(200), nullable=True, unique=None, default=u'')
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    phone_num = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    payment_method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    payment_rate = Column(types.Numeric(precision=10, scale=10), nullable=True, unique=None, default=0.0000000000)
    exchange_rate = Column(types.Numeric(precision=10, scale=10), nullable=True, unique=None, default=0.0000000000)
    currency_symbol = Column(types.Unicode(20), nullable=True, unique=None, default=u'CNY')
    is_transfered = Column(types.Integer(), nullable=True, unique=None, default=0)
    transfer_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    bank_insid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class Machines(Base):
    __tablename__ = 'machines'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'h1')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    warranty_start_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    warranty_end_date_host = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    warranty_end_date_client = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    serial = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    model = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    capacity = Column(types.Integer(), nullable=True, unique=None, default=0)
    location = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    country = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    state = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    city = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    district = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    zip = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    street = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    building = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    location_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    location_display_fields = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    lat = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    lng = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    mac = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    reg_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    reg_location = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    active = Column(types.Integer(), nullable=True, unique=None, default=1)
    oo_status = Column(types.Unicode(50), nullable=True, unique=None, default=u'offline')
    ai_status = Column(types.Unicode(50), nullable=True, unique=None, default=u'inactive')
    ai_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    notes_host = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    inventory = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    layout_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    is_wc_show = Column(types.Integer(), nullable=True, unique=None, default=0)
    logo_url = Column(types.Unicode(3000), nullable=True, unique=None, default=u'')
    icon_url = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    password = Column(types.Unicode(255), nullable=True, unique=None, default=u'howcute121')
    software_version = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    upgrade_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class NaviCategory(Base):
    __tablename__ = 'navi_category'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    navi_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    name_s = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    pid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    pic_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'0')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PProduct(Base):
    __tablename__ = 'p_product'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    ppid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    name_s = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    fina_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    market_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    manufacturer = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    supplier_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    supplier_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    model = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    description = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    service_phone = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    is_show = Column(types.Integer(), nullable=True, unique=None, default=1)
    is_critical = Column(types.Integer(), nullable=True, unique=None, default=0)
    is_id_card_presented_item = Column(types.Integer(), nullable=True, unique=None, default=0)
    is_date_sensitive = Column(types.Integer(), nullable=True, unique=None, default=0)
    pre_alert_time = Column(types.Integer(), nullable=True, unique=None, default=30)
    is_virtual = Column(types.Integer(), nullable=True, unique=None, default=0)
    is_gift = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_method = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sale_channel = Column(types.Integer(), nullable=True, unique=None, default=3)
    package_length = Column(types.Float(), nullable=True, unique=None, default=0)
    package_width = Column(types.Float(), nullable=True, unique=None, default=0)
    package_height = Column(types.Float(), nullable=True, unique=None, default=0)
    slot_max_count = Column(types.Unicode(500), nullable=True, unique=None, default=u'')
    fetch_style = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    eject_weight = Column(types.Integer(), nullable=True, unique=None, default=0)
    rating = Column(types.Float(), nullable=True, unique=None, default=0)
    rating_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    main_pic_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    main_pic_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    pic_3d = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PProduct3dPic(Base):
    __tablename__ = 'p_product_3d_pic'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    ppid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    pic_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'0')
    pic_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    pic_md5 = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PProductNaviCategory(Base):
    __tablename__ = 'p_product_navi_category'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    ppid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    navi_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PProductPic(Base):
    __tablename__ = 'p_product_pic'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    ppid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    pic_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    main_pic = Column(types.Boolean(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PProductSpec(Base):
    __tablename__ = 'p_product_spec'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    ppid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    lang = Column(types.Unicode(50), nullable=True, unique=None, default=u'en_US')
    variable = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    value = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    sequence = Column(types.Integer(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PProductRelatedRecommanded(Base):
    __tablename__ = 'p_product_related_recommanded'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    main_ppid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    related_ppid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    related_name = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    related_pic_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PVerifyPic(Base):
    __tablename__ = 'p_verify_pic'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    ppid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    pic_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class SiteConfig(Base):
    __tablename__ = 'site_config'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    variable = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    value = Column(types.Unicode(3000), nullable=True, unique=None, default=u'')


class TemplateFieldTypes(Base):
    __tablename__ = 'template_field_types'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    regular_expression = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    input = Column(types.Unicode(45), nullable=True, unique=None, default=u'')


class MachineRfids(Base):
    __tablename__ = 'machine_rfids'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rfid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    sale_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_convert_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    price_plan_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    price_plan_template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    price_plan_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    price_plan_data = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    state = Column(types.Unicode(20), nullable=True, unique=None, default=u'in')


class MachineRentalInfo(Base):
    __tablename__ = 'machine_rental_info'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_no = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    test_mode = Column(types.Integer(), nullable=True, unique=None, default=0)
    reader_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    cc_display = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rfid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    out_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    in_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    expire_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    price_plan_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    price_plan_template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    price_plan_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    price_plan_data = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    coupon_template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    coupon_code = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    coupon_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    coupon_plan_data = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    status = Column(types.Unicode(20), nullable=True, unique=None, default=u'open')
    type = Column(types.Unicode(255), nullable=True, unique=None, default=u'rental')


class KioskType(Base):
    __tablename__ = 'kiosk_type'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    flows = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    resolution = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


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


class PromotionPlanTemplate(Base):
    __tablename__ = 'promotion_plan_template'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    fields = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    package_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    version = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    file_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    version = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    file_md5 = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.Unicode(255), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PromotionPlan(Base):
    __tablename__ = 'promotion_plan'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    plan_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    plan_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    data = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    channel = Column(types.Integer(), nullable=True, unique=None, default=3)
    status = Column(types.Integer(), nullable=True, unique=None, default=1)
    kiosk_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    compatibility = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    repeatable = Column(types.Integer(), nullable=True, unique=None, default=0)
    repeat_interval = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PromotionKiosks(Base):
    __tablename__ = 'promotion_kiosks'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    plan_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class SimpleSurvey(Base):
    __tablename__ = 'simple_survey'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    question_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    type = Column(types.Integer(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class SimpleSurveyInstance(Base):
    __tablename__ = 'simple_survey_instance'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    survey_name = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    status = Column(types.Integer(), nullable=True, unique=None, default=1)
    question_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    random_question_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    type = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    awards_model = Column(types.Integer(), nullable=True, unique=None, default=0)
    awards_desc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    result_msg = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_code_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    show_fields = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    result_show_code = Column(types.Integer(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class SimpleSurveyInstanceCustomer(Base):
    __tablename__ = 'simple_survey_instance_customer'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_instance_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    open_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    cell_phone = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    gender = Column(types.Unicode(5), nullable=True, unique=None, default=u'')
    age_range = Column(types.Unicode(25), nullable=True, unique=None, default=u'')
    email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    complete_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    complete_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    pick_code_status = Column(types.Unicode(20), nullable=True, unique=None, default=u'open')
    pick_kiosk = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')


class SimpleSurveyInstanceAnswer(Base):
    __tablename__ = 'simple_survey_instance_answer'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_instance_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    customer_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    question_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    answer = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    answer_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    answer_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class SimpleSurveyInstanceProduct(Base):
    __tablename__ = 'simple_survey_instance_product'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_instance_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')


class SimpleSurveyInstanceCoupon(Base):
    __tablename__ = 'simple_survey_instance_coupon'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_instance_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    coupon_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    coupon_code = Column(types.Unicode(50), nullable=True, unique=None, default=u'')


class SimpleSurveyInstanceQuestion(Base):
    __tablename__ = 'simple_survey_instance_question'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_instance_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    title = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    options = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    options_img = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    q_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'single')
    is_required = Column(types.Integer(), nullable=True, unique=None, default=0)
    answer = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class SimpleSurveyQuestion(Base):
    __tablename__ = 'simple_survey_question'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    title = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    options = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    options_img = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    q_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'single')
    is_required = Column(types.Integer(), nullable=True, unique=None, default=0)
    answer = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class PromotionProducts(Base):
    __tablename__ = 'promotion_products'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    plan_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    category = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    market_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class Readers(Base):
    __tablename__ = 'readers'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    gender = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    nation = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    id_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    card_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    phone_no = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    balance = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    status = Column(types.Unicode(20), nullable=True, unique=None, default=u'active')
    notes = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    last_rent_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_rent_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class RfidBook(Base):
    __tablename__ = 'rfid_book'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    rfid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    title = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    isbn = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    release_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class MachineNopickedItems(Base):
    __tablename__ = 'machine_nopicked_items'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    transaction_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    unit_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    status = Column(types.Unicode(20), nullable=True, unique=None, default=u'open')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class Permissions(Base):
    __tablename__ = 'permissions'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    page = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ctrl = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    action = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    site_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    level = Column(types.Integer(), nullable=True, unique=None, default=3)
    sadmin = Column(types.Integer(), nullable=True, unique=None, default=1)
    admin = Column(types.Integer(), nullable=True, unique=None, default=0)


class Reservations(Base):
    __tablename__ = 'reservations'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    source = Column(types.Unicode(255), nullable=True, unique=None, default=u'wechat')
    transaction_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    arrival_notice_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    pick_code = Column(types.Unicode(10), nullable=True, unique=None, default=u'')
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    customer_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    customer_gender = Column(types.Integer(), nullable=True, unique=None, default=0)
    customer_age = Column(types.Integer(), nullable=True, unique=None, default=0)
    credit_card_brand = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    credit_card_num = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_auth_date = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    item_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    charge_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reserve_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    reserve_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    reserve_type = Column(types.Integer(), nullable=True, unique=None, default=1)
    status = Column(types.Integer(), nullable=True, unique=None, default=0)


class SimpleSurveyInstanceCustomerWechat(Base):
    __tablename__ = 'simple_survey_instance_customer_wechat'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_instance_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    open_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    wc_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    wc_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    cell_phone = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    company_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    position = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    complete_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    complete_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class WcSettings(Base):
    __tablename__ = 'wc_settings'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    wc_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    wc_original_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    wc_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    app_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    app_secret = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class WcPaymentRequests(Base):
    __tablename__ = 'wc_payment_requests'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    wc_appid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    wc_mch_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    wc_mch_pay_key = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    prepay_id = Column(types.Unicode(64), nullable=True, unique=None, default=u'')
    request_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    notify_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    result_code = Column(types.Unicode(16), nullable=True, unique=None, default=u'OPEN')
    err_code = Column(types.Unicode(32), nullable=True, unique=None, default=u'')
    err_code_des = Column(types.Unicode(128), nullable=True, unique=None, default=u'')
    openid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    is_subscribe = Column(types.Unicode(1), nullable=True, unique=None, default=u'')
    trade_type = Column(types.Unicode(16), nullable=True, unique=None, default=u'')
    bank_type = Column(types.Unicode(16), nullable=True, unique=None, default=u'')
    total_fee = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_fee = Column(types.Integer(), nullable=True, unique=None, default=0)
    fee_type = Column(types.Unicode(8), nullable=True, unique=None, default=u'')
    wc_transaction_id = Column(types.Unicode(32), nullable=True, unique=None, default=u'')
    out_trade_no = Column(types.Unicode(32), nullable=True, unique=None, default=u'')
    attach = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    time_end = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class Members(Base):
    __tablename__ = 'members'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    cellphone = Column(types.Unicode(25), nullable=True, unique=None, default=u'')
    first_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    last_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    nickname = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    gender = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    birthday = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    country = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    state = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    city = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    district = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    status = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    credits = Column(types.Integer(), nullable=True, unique=None, default=0)
    source = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_login_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    wc_openid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    wc_subscribe_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    wc_nickname = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    wc_headimgurl = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class KioskVersion(Base):
    __tablename__ = 'kiosk_version'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    version = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    manual_upgrade_date = Column(types.Date(), nullable=True, unique=None, default=u'0000-00-00')
    auto_upgrade_date = Column(types.Date(), nullable=True, unique=None, default=u'0000-00-00')
    release_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class GiftActivity(Base):
    __tablename__ = 'gift_activity'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    act_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    act_description = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    status = Column(types.Integer(), nullable=True, unique=None, default=1)
    kiosk_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_code_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    wc_keywords = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class GiftKiosks(Base):
    __tablename__ = 'gift_kiosks'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    act_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class GiftPickCode(Base):
    __tablename__ = 'gift_pick_code'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    act_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    pick_code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_kiosk = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    open_id = Column(types.Unicode(100), nullable=True, unique=None, default=u'')
    send_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    use_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class GiftProducts(Base):
    __tablename__ = 'gift_products'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    act_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class KioskLoginCode(Base):
    __tablename__ = 'kiosk_login_code'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    kiosk_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    login_code = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    login_email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    login_ip = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    login_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class ClientProductClickHistory(Base):
    __tablename__ = 'client_product_click_history'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    click_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class CouponCode(Base):
    __tablename__ = 'coupon_code'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    coupon_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    code = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    total_usage_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_usage_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class MachineResultAdCodes(Base):
    __tablename__ = 'machine_result_ad_codes'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ad_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    is_used = Column(types.Integer(), nullable=True, unique=None, default=0)
    use_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class MachineResultAd(Base):
    __tablename__ = 'machine_result_ad'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    notes = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    always_show = Column(types.Integer(), nullable=True, unique=None, default=0)
    status = Column(types.Integer(), nullable=True, unique=None, default=1)
    pic_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    pic_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    min_fee = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class PProductSupplier(Base):
    __tablename__ = 'p_product_supplier'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    supplier_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    company_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    registration_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    location = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    contact = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    tel = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    fax = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    qq = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    bank_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    bank_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    account_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    billing_cycle = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    billing_day = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class ScPromotionPlan(Base):
    __tablename__ = 'sc_promotion_plan'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(500), nullable=True, unique=None, default=u'')
    plan_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    plan_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    channel = Column(types.Integer(), nullable=True, unique=None, default=3)
    status = Column(types.Integer(), nullable=True, unique=None, default=1)
    condition = Column(types.Integer(), nullable=True, unique=None, default=1)
    condition_value = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    reward_type = Column(types.Integer(), nullable=True, unique=None, default=1)
    reward_value = Column(types.Numeric(precision=20, scale=10), nullable=True, unique=None, default=0.0000000000)
    kiosk_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class ScPromotionProducts(Base):
    __tablename__ = 'sc_promotion_products'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    plan_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    market_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    type = Column(types.Integer(), nullable=True, unique=None, default=1)


class ScPromotionKiosks(Base):
    __tablename__ = 'sc_promotion_kiosks'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    plan_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    kiosk_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class MachineExpress(Base):
    __tablename__ = 'machine_express'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    operator_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    operator = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    express_no = Column(types.Unicode(25), nullable=True, unique=None, default=u'')
    receiver_cell_phone = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    receiver_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    receiver_location = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    digital_sign = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    put_pics = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    put_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    put_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    fetch_pics = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    fetch_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    fetch_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class CouponProductsExcept(Base):
    __tablename__ = 'coupon_products_except'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    coupon_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    price = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_price = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class UserKiosk(Base):
    __tablename__ = 'user_kiosk'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    user_email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    type = Column(types.Integer(), nullable=True, unique=None, default=1)


class WcAutoReply(Base):
    __tablename__ = 'wc_auto_reply'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    keywords = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    message_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    content = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class ClientCustomReport(Base):
    __tablename__ = 'client_custom_report'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    report_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    report_passcode = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    kiosk_ids = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class SupplierRefundFeeRecords(Base):
    __tablename__ = 'supplier_refund_fee_records'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    refund_fee_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    used_fee = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    used_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class SupplierRefundFee(Base):
    __tablename__ = 'supplier_refund_fee'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    supplier_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    supplier_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    refund_item = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    refund_fee = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    remained_fee = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_used_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class SimpleSurveyInstanceKiosk(Base):
    __tablename__ = 'simple_survey_instance_kiosk'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_instance_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class ClientFaceRecCvHistory(Base):
    __tablename__ = 'client_face_rec_cv_history'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    media_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    cv_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    cv_type = Column(types.Integer(), nullable=True, unique=None, default=0)


class ArrivalNotice(Base):
    __tablename__ = 'arrival_notice'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    member_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    member_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    product_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    source = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    reserve_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    noticed_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    online_order_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    reservation_order_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    is_charged = Column(types.Integer(), nullable=True, unique=None, default=0)
    payment_method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    payment_oid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    notice_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    notice_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.Unicode(2550), nullable=True, unique=None, default=u'')


class KioskNotes(Base):
    __tablename__ = 'kiosk_notes'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    notes = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    operator = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ip = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class OnlineOrder(Base):
    __tablename__ = 'online_order'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    order_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    source = Column(types.Unicode(50), nullable=True, unique=None, default=u'wechat')
    machine_shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_transaction_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    arrival_notice_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_names = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    pick_code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    member_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    customer_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    payment_method = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    payment_oid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    charge_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    coupon_code = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    is_paid = Column(types.Integer(), nullable=True, unique=None, default=0)
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    reserve_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    reserve_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    charge_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    expire_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    cancel_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    cancel_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')


class OnlineOrderDetail(Base):
    __tablename__ = 'online_order_detail'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    source = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    machine_shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_transaction_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    arrival_notice_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    member_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    customer_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    picked_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    item_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    charge_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    payment_method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    type = Column(types.Unicode(20), nullable=True, unique=None, default=u'sale')
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    reserve_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    reserve_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    charge_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    cancel_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    cancel_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')


class OnlineOrderPickRecord(Base):
    __tablename__ = 'online_order_pick_record'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    order_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_detail_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')


class GiftMembers(Base):
    __tablename__ = 'gift_members'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True)
    act_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    member_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    cell_phone = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    validation_code = Column(types.Unicode(10), nullable=True, unique=None, default=u'')
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    request_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class SettlementRecords(Base):
    __tablename__ = 'settlement_records'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    company_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    settle_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    trs_period = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    trs_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    trs_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    pending_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    pending_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    other_settled_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    other_settled_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    settlement_rate = Column(types.Numeric(precision=10, scale=10), nullable=True, unique=None, default=0.0000000000)
    bank_charges = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    settle_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    settle_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    bank_serial_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    bank_insid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    bank_err_msg = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    status = Column(types.Integer(), nullable=True, unique=None, default=2)


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


class ClientStore(Base):
    __tablename__ = 'client_store'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    store_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    state = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    city = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    district = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    street = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    building = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    contact = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    tel = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    nearby_kiosk_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    daily_limitation = Column(types.Integer(), nullable=True, unique=None, default=0)
    is_show = Column(types.Integer(), nullable=True, unique=None, default=1)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class ClientStoreKiosk(Base):
    __tablename__ = 'client_store_kiosk'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True)
    store_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')


class ClientStoreReservation(Base):
    __tablename__ = 'client_store_reservation'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    act_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    store_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    store_city = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    store_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    cell_phone = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    validation_code = Column(types.Unicode(10), nullable=True, unique=None, default=u'')
    request_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    reserve_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class ClientStoreActivity(Base):
    __tablename__ = 'client_store_activity'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    act_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    act_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    pick_date = Column(types.Integer(), nullable=True, unique=None, default=1)
    start_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    end_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    reward_type = Column(types.Integer(), nullable=True, unique=None, default=0)
    store_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    code_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class ClientStoreActStores(Base):
    __tablename__ = 'client_store_act_stores'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    act_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    store_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    store_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class ClientStoreActProducts(Base):
    __tablename__ = 'client_store_act_products'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    act_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class ClientStoreActCode(Base):
    __tablename__ = 'client_store_act_code'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    act_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    is_used = Column(types.Integer(), nullable=True, unique=None, default=0)
    used_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class ClientKioskAudio(Base):
    __tablename__ = 'client_kiosk_audio'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    audio_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    file_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    file_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upload_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    upload_user = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    review_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    review_status = Column(types.Integer(), nullable=True, unique=None, default=0)
    review_notes = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    review_user = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    file_type = Column(types.Integer(), nullable=True, unique=None, default=0)


class GameTemplate(Base):
    __tablename__ = 'game_template'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    fields = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    resolution = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    version = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    form_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    valid = Column(types.Integer(), nullable=True, unique=None, default=1)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class GameActivity(Base):
    __tablename__ = 'game_activity'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    act_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    act_description = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    game_template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    game_name = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    reward_type = Column(types.Integer(), nullable=True, unique=None, default=0)
    reward_value = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    status = Column(types.Integer(), nullable=True, unique=None, default=1)
    data = Column(types.Unicode(2000), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class GameActCoupon(Base):
    __tablename__ = 'game_act_coupon'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    act_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    coupon_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')


class GamePlayHistory(Base):
    __tablename__ = 'game_play_history'
    id_ai = Column(types.Integer(), nullable=False,unique=None,default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True,unique=None,default=u'')
    machine_id = Column(types.Unicode(50), nullable=True,unique=None,default=u'')
    machine_name = Column(types.Unicode(255), nullable=True,unique=None,default=u'')
    act_id = Column(types.Unicode(50), nullable=True,unique=None,default=u'')
    act_name = Column(types.Unicode(255), nullable=True,unique=None,default=u'')
    game_template_id = Column(types.Unicode(50), nullable=True,unique=None,default=u'')
    game_name = Column(types.Unicode(1000), nullable=True,unique=None,default=u'')
    play_time = Column(types.DateTime(), nullable=True,unique=None,default=u'0000-00-00 00:00:00')
    score = Column(types.Numeric(precision=20, scale=3), nullable=True,unique=None,default=0.000)
    unit = Column(types.Unicode(10), nullable=True,unique=None,default=u'')
    phone = Column(types.Unicode(20), nullable=True,unique=None,default=u'')
    coupon_code = Column(types.Unicode(50), nullable=True,unique=None,default=u'')
    item_sku = Column(types.Unicode(50), nullable=True,unique=None,default=u'')
    item_name = Column(types.Unicode(255), nullable=True,unique=None,default=u'')
    pick_code = Column(types.Unicode(50), nullable=True,unique=None,default=u'')
    gift_code_3rd = Column(types.Unicode(50), nullable=True,unique=None,default=u'')
    points = Column(types.Integer(), nullable=True,unique=None,default=0)
    is_stat = Column(types.Integer(), nullable=True,unique=None,default=0)


class SwyfPaymentRequests(Base):
    __tablename__ = 'swyf_payment_requests'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    partner = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    out_trade_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    request_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    notify_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    return_code = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    trade_mode = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    trade_state = Column(types.Integer(), nullable=True, unique=None, default=3)
    pay_info = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    trans_channel = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    swyf_transaction_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    bank_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    bank_transno = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    batch_num = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_fee_request = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_fee_notify = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    discount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    fee_type = Column(types.Integer(), nullable=True, unique=None, default=1)
    notify_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    time_end = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    buyer_alias = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    attach = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class ClientFiling(Base):
    __tablename__ = 'client_filing'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    location = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    version = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    start_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    end_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    file_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    kiosk_items_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    survey_report_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    store_activity_report_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rpt_income_hourly_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rpt_income_daily_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rpt_income_item_daily_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rpt_income_payment_daily_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rpt_product_inventory_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rpt_client_product_click_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rpt_client_face_rec_url = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class UserRole(Base):
    __tablename__ = 'user_role'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    role_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')


class LicensePage(Base):
    __tablename__ = 'license_page'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    license_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    page_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    ctrl = Column(types.Unicode(50), nullable=True, unique=None, default=u'')


class License(Base):
    __tablename__ = 'license'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    license_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class RolePage(Base):
    __tablename__ = 'role_page'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    role_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    page_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    ctrl = Column(types.Unicode(50), nullable=True, unique=None, default=u'')


class Role(Base):
    __tablename__ = 'role'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    role_name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    login_conn = Column(types.Integer(), nullable=True, unique=None, default=0)
    login_kiosk = Column(types.Integer(), nullable=True, unique=None, default=0)
    email_alert = Column(types.Integer(), nullable=True, unique=None, default=0)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class Page(Base):
    __tablename__ = 'page'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    category = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ctrl = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    description = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    site_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    level = Column(types.Integer(), nullable=True, unique=None, default=3)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class RptClientFaceRec(Base):
    __tablename__ = 'rpt_client_face_rec'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    media_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    view_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    click_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    date_hour = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


# Report
class RptIncomeDaily(Base):
    __tablename__ = 'rpt_income_daily'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    start_date = Column(types.DateTime(), nullable=False, unique=None, default=u'0000-00-00', primary_key=True)
    end_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    sale_date = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_date_range = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptIncomeItemDaily(Base):
    __tablename__ = 'rpt_income_item_daily'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    item_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    item_sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    item_name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    item_market_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    item_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    start_date = Column(types.DateTime(), nullable=False, unique=None, default=u'0000-00-00', primary_key=True)
    end_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    sale_date = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_date_range = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptIncomeWeekly(Base):
    __tablename__ = 'rpt_income_weekly'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    start_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    end_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    sale_date = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_date_range = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptIncomeMonthly(Base):
    __tablename__ = 'rpt_income_monthly'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    start_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    end_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    sale_date = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_date_range = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptIncomeYearly(Base):
    __tablename__ = 'rpt_income_yearly'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    start_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    end_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    sale_date = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_date_range = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptIncomePaymentDaily(Base):
    __tablename__ = 'rpt_income_payment_daily'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    payment_method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    start_date = Column(types.DateTime(), nullable=False, unique=None, default=u'0000-00-00', primary_key=True)
    end_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    sale_date = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_date_range = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptClientAds(Base):
    __tablename__ = 'rpt_client_ads'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    publish_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    publish_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    publish_kiosks = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    publish_status = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    element_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    resolution = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ad_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    ad_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    target_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    target_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    target_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    effective_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    expiration_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    stat_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    view_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    click_count = Column(types.Integer(), nullable=True, unique=None, default=0)


class RptMostPopularItem(Base):
    __tablename__ = 'rpt_most_popular_item'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    conn_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    item_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    item_sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    item_name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptMostPopularKiosk(Base):
    __tablename__ = 'rpt_most_popular_kiosk'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    conn_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_location = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptProductInventory(Base):
    __tablename__ = 'rpt_product_inventory'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    product_upc = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_model = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_navi_cate_ids = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_navi_cate_names = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    product_default_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    product_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    product_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_mismatch_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_reserve_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_outside_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_total_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    stat_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    stat_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class RptProductMachineInventory(Base):
    __tablename__ = 'rpt_product_machine_inventory'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    product_upc = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_model = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_navi_cate_ids = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_navi_cate_names = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    product_default_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    product_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    product_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_mismatch_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_reserve_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_outside_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    product_total_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    stat_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    stat_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class RptUpdateTime(Base):
    __tablename__ = 'rpt_update_time'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    rpt_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class RptMachineGenTime(Base):
    __tablename__ = 'rpt_machine_gen_time'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    table_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    last_gen_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time = Column(types.Unicode(255), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class RptMachineHostClientChange(Base):
    __tablename__ = 'rpt_machine_host_client_change'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class RptInactiveLogs(Base):
    __tablename__ = 'rpt_inactive_logs'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    inactive_duration = Column(types.Integer(), nullable=True, unique=None, default=0)
    inactive_from = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    inactive_to = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    inactive_type = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    inactive_by = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    active_by = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class RptInactiveOverview(Base):
    __tablename__ = 'rpt_inactive_overview'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    today_rate = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    week_rate = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    month_rate = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    year_rate = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    today_inactive_duration = Column(types.Integer(), nullable=True, unique=None, default=0)
    week_inactive_duration = Column(types.Integer(), nullable=True, unique=None, default=0)
    month_inactive_duration = Column(types.Integer(), nullable=True, unique=None, default=0)
    year_inactive_duration = Column(types.Integer(), nullable=True, unique=None, default=0)
    today_all_duration = Column(types.Integer(), nullable=True, unique=None, default=0)
    week_all_duration = Column(types.Integer(), nullable=True, unique=None, default=0)
    month_all_duration = Column(types.Integer(), nullable=True, unique=None, default=0)
    year_all_duration = Column(types.Integer(), nullable=True, unique=None, default=0)


class RptClientProductClick(Base):
    __tablename__ = 'rpt_client_product_click'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    click_date = Column(types.DateTime(), nullable=False, unique=None, default=u'0000-00-00', primary_key=True)
    click_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    trs_count = Column(types.Integer(), nullable=True, unique=None, default=0)


class RptIncomeHourly(Base):
    __tablename__ = 'rpt_income_hourly'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    start_date = Column(types.DateTime(), nullable=False, unique=None, default=None, primary_key=True)
    end_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    sale_date = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_date_range = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sale_hour = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    reservation_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    kiosk_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_sale_income_without_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    kiosk_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    reservation_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    refund_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_sale_orders = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)


class RptClientGameActivity(Base):
    __tablename__ = 'rpt_client_game_activity'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    act_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    act_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    game_template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    game_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    played_times = Column(types.Integer(), nullable=True, unique=None, default=0)
    played_person = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_code_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_code_used_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_code_3rd_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_points = Column(types.Integer(), nullable=True, unique=None, default=0)
    accumulated_days = Column(types.Integer(), nullable=True, unique=None, default=0)


class RptClientGameActivityHourly(Base):
    __tablename__ = 'rpt_client_game_activity_hourly'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    host_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    host_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    act_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    act_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    game_template_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    game_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    play_date = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00')
    play_hour = Column(types.Integer(), nullable=True, unique=None, default=0)
    played_times = Column(types.Integer(), nullable=True, unique=None, default=0)
    played_person = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    item_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_code_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    gift_code_3rd_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_points = Column(types.Integer(), nullable=True, unique=None, default=0)


# Region
class AllCities(BaseRegion):
    __tablename__ = 'all_cities'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    country_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    city_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    city_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    population = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    latitude = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    longitude = Column(types.Unicode(255), nullable=True, unique=None, default=None)


class AllStates(BaseRegion):
    __tablename__ = 'all_states'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    country_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_short_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)


class Cities(BaseRegion):
    __tablename__ = 'cities'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    country_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    city_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    city_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    population = Column(types.Integer(), nullable=True, unique=None, default=None)
    latitude = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    longitude = Column(types.Unicode(255), nullable=True, unique=None, default=None)


class Countries(BaseRegion):
    __tablename__ = 'countries'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    country_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    country_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    available = Column(types.Integer(), nullable=True, unique=None, default=None)


class States(BaseRegion):
    __tablename__ = 'states'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    country_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_short_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)


class PaymentCallback(Base):
    __tablename__ = 'payment_callback'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    shopping_cart_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    notify_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    notify_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    notify_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sign_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sign = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    subject = Column(types.Unicode(256), nullable=True, unique=None, default=u'')
    trade_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    trade_status = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    trade_create_gmt = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    trade_payment_gmt = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    seller_account = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ali_partner = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ali_key = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    buyer_account = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    seller_account_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    buyer_account_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    total_fee = Column(types.Float(), nullable=True, unique=None, default=0)
    body = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    payment_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    full_data = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class AlipaySettings(Base):
    __tablename__ = 'alipay_settings'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    conn_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    seller_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    seller_email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ali_partner = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    ali_key = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class VPProductMainPics(BaseRegion):
    __tablename__ = 'v_pproduct_main_pics'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    pic_url = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    ppid = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    pic_md5 = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    pic_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    pic_size = Column(types.Integer(), nullable=True, unique=None, default=None)


class Districts(BaseRegion):
    __tablename__ = 'districts'
    id = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    country_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    state_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    city_code = Column(types.Unicode(255), nullable=True, unique=None, default=None)
    district_name = Column(types.Unicode(255), nullable=True, unique=None, default=None)


class MachineShoppingCartsFiling(BaseFiling):
    __tablename__ = 'machine_shopping_carts'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_no = Column(types.Unicode(45), nullable=True, unique=None, default=u'0000')
    trs_time = Column(types.DateTime(), nullable=False, unique=None, default=u'0000-00-00 00:00:00', primary_key=True)
    trs_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    lang = Column(types.Unicode(10), nullable=True, unique=None, default=u'en_US')
    receipt_email = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    test_mode = Column(types.Integer(), nullable=True, unique=None, default=0)
    cc_display = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    subtotal = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    total_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    charge_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    refund_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_code = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    pick_code = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    coupon_count = Column(types.Integer(), nullable=True, unique=None, default=0)
    coupon_discount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    upg_type = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    upg_oid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_payment_method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_auth_num = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_merchant_ref = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_auth_date = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    upg_card_brand = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    upg_card_num = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    time_zone = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    card_type = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    customer_picture = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    misvend_done = Column(types.Integer(), nullable=True, unique=None, default=0)
    phone_num = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    payment_rate = Column(types.Numeric(precision=10, scale=10), nullable=True, unique=None, default=0.0000000000)
    currency_symbol = Column(types.Unicode(20), nullable=True, unique=None, default=u'CNY')
    exchange_rate = Column(types.Numeric(precision=20, scale=10), nullable=True, unique=None, default=0.0000000000)
    is_receipt_printed = Column(types.Integer(), nullable=True, unique=None, default=0)
    receipt_print_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    transfer_status = Column(types.Integer(), nullable=True, unique=None, default=0)
    transfer_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')


class MachineStockEventsFiling(BaseFiling):
    __tablename__ = 'machine_stock_events'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
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


class MachineSysEventsFiling(BaseFiling):
    __tablename__ = 'machine_sys_events'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    event_type = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    action = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    description = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    add_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    add_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)


class MachineTransactionsFiling(BaseFiling):
    __tablename__ = 'machine_transactions'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    transaction_no = Column(types.Unicode(45), nullable=True, unique=None, default=u'0000')
    test_mode = Column(types.Integer(), nullable=True, unique=None, default=0)
    cc_display = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    upc = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    name = Column(types.Unicode(1024), nullable=True, unique=None, default=u'')
    fina_cate_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    fina_cate_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    supplier_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    supplier_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    unit_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    original_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    real_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    sale_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    trs_time = Column(types.DateTime(), nullable=False, unique=None, default=u'0000-00-00 00:00:00', primary_key=True)
    last_update_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    trs_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    last_update_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    create_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    create_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    type = Column(types.Unicode(45), nullable=True, unique=None, default=u'sale')
    state = Column(types.Unicode(45), nullable=True, unique=None, default=u'proccessing')
    notes = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    refund_notes = Column(types.UnicodeText(), nullable=True, unique=None, default=None)
    enable_sale_tax = Column(types.Unicode(45), nullable=True, unique=None, default=u'on')
    unit_tax = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    sale_tax_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    deliver_pics = Column(types.Unicode(3000), nullable=True, unique=None, default=u'')
    error_msgs = Column(types.Unicode(3000), nullable=True, unique=None, default=u'')
    error_type = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    operator = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    duration_time = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    coupon_code = Column(types.Unicode(45), nullable=True, unique=None, default=u'')
    pick_code = Column(types.Unicode(200), nullable=True, unique=None, default=u'')
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    phone_num = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    payment_method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    payment_rate = Column(types.Numeric(precision=10, scale=10), nullable=True, unique=None, default=0.0000000000)
    exchange_rate = Column(types.Numeric(precision=20, scale=10), nullable=True, unique=None, default=0.0000000000)
    currency_symbol = Column(types.Unicode(20), nullable=True, unique=None, default=u'CNY')
    is_transfered = Column(types.Integer(), nullable=True, unique=None, default=0)
    transfer_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    bank_insid = Column(types.Unicode(255), nullable=True, unique=None, default=u'')


class OnlineOrderFiling(BaseFiling):
    __tablename__ = 'online_order'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    source = Column(types.Unicode(50), nullable=True, unique=None, default=u'wechat')
    machine_shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_transaction_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    arrival_notice_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_no = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_names = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')
    pick_code = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    member_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    customer_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    payment_method = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    payment_oid = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    total_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    charge_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    coupon_code = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    is_paid = Column(types.Integer(), nullable=True, unique=None, default=0)
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    reserve_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    reserve_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    charge_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    expire_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    cancel_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    cancel_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')


class OnlineOrderDetailFiling(BaseFiling):
    __tablename__ = 'online_order_detail'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    client_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    client_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    source = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    machine_shopping_cart_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_transaction_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    arrival_notice_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_no = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    member_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    customer_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    sku = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    picked_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_quantity = Column(types.Integer(), nullable=True, unique=None, default=0)
    item_price = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    discount_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    charge_amount = Column(types.Numeric(precision=20, scale=3), nullable=True, unique=None, default=0.000)
    payment_method = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    type = Column(types.Unicode(20), nullable=True, unique=None, default=u'sale')
    status = Column(types.Integer(), nullable=True, unique=None, default=0)
    reserve_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    reserve_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    charge_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    charge_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    cancel_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    cancel_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')


class OnlineOrderPickRecordFiling(BaseFiling):
    __tablename__ = 'online_order_pick_record'
    id_ai = Column(types.Integer(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    file_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    order_detail_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    machine_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    product_id = Column(types.Unicode(50), nullable=True, unique=None, default=u'')
    product_name = Column(types.Unicode(255), nullable=True, unique=None, default=u'')
    slot_id = Column(types.Unicode(20), nullable=True, unique=None, default=u'')
    pick_time = Column(types.DateTime(), nullable=True, unique=None, default=u'0000-00-00 00:00:00')
    pick_time_int = Column(types.Integer(), nullable=True, unique=None, default=0)
    notes = Column(types.Unicode(1000), nullable=True, unique=None, default=u'')

