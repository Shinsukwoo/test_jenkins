from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TbAbnormal(models.Model):
    abnormal_code = models.CharField(primary_key=True, max_length=100)
    abnormal_name = models.CharField(max_length=100)
    kind = models.CharField(max_length=30)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_abnormal'


class TbAccessLog(models.Model):
    access_seq = models.AutoField(primary_key=True)
    access_date = models.DateTimeField(blank=True, null=True)
    access_flag = models.CharField(max_length=10)
    access_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_access_log'


class TbAuthorGroup(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tb_author_group'


class TbAuthorMenu(models.Model):
    author = models.OneToOneField(TbAuthorGroup, models.DO_NOTHING, primary_key=True)
    author_url = models.CharField(max_length=100)
    author_ordr = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_author_menu'
        unique_together = (('author', 'author_url'),)


class TbBom(models.Model):
    bom_code = models.CharField(primary_key=True, max_length=30)
    bom_name = models.CharField(max_length=50)
    item_code = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_bom'


class TbBomMaterial(models.Model):
    bom_code = models.CharField(primary_key=True, max_length=30)
    material_code = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bom_material'
        unique_together = (('bom_code', 'material_code'),)


class TbBomProcess(models.Model):
    bom_code = models.CharField(primary_key=True, max_length=30)
    process_code = models.CharField(max_length=100)
    ordr = models.IntegerField(db_column='ORDR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_bom_process'
        unique_together = (('bom_code', 'process_code'),)


class TbCustomer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_code = models.CharField(primary_key=True, max_length=30)
    homepage = models.CharField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=30, blank=True, null=True)
    representative_name = models.CharField(max_length=30, blank=True, null=True)
    representative_phone = models.CharField(max_length=30, blank=True, null=True)
    representative_email = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_customer'


class TbDocuCode(models.Model):
    docu_id = models.AutoField(primary_key=True)
    docu_div_cd = models.CharField(max_length=256, blank=True, null=True)
    docu_div_nm = models.CharField(max_length=256, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_docu_code'


class TbDocuInfo(models.Model):
    docu_div = models.PositiveIntegerField()
    docu_id = models.AutoField(primary_key=True)
    docu_div_cd = models.CharField(max_length=256, blank=True, null=True)
    docu_div_nm = models.CharField(max_length=256, blank=True, null=True)
    docu_nm = models.TextField()
    remark = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    mod_date = models.DateField()
    reg_id = models.CharField(max_length=30, blank=True, null=True)
    mod_id = models.CharField(max_length=30, blank=True, null=True)
    docu_no = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tb_docu_info'


class TbEquipfault(models.Model):
    fault_id = models.PositiveBigIntegerField()
    abnormal_date = models.DateTimeField()
    machine_code = models.CharField(max_length=100)
    machine_name = models.CharField(max_length=100)
    abnormal_code = models.CharField(max_length=100)
    abnormal_name = models.CharField(max_length=100)
    abnormal_cnt = models.PositiveBigIntegerField()
    abnormal_prc = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    input_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_equipfault'


class TbFile(models.Model):
    table_name = models.CharField(primary_key=True, max_length=50)
    board_id = models.CharField(max_length=50)
    org_file_name = models.TextField()
    save_file_name = models.CharField(max_length=50)
    file_size = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField()
    gubun = models.CharField(max_length=50)
    reg_id = models.CharField(max_length=30)
    ordr = models.CharField(max_length=10, blank=True, null=True)
    file_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_file'
        unique_together = (('table_name', 'board_id', 'gubun', 'ordr'), ('table_name', 'board_id', 'gubun'),)


class TbFile1(models.Model):
    file_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=50)
    board_id = models.CharField(max_length=50)
    org_file_name = models.TextField()
    save_file_name = models.CharField(max_length=50)
    file_size = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField()
    gubun = models.CharField(max_length=50, blank=True, null=True)
    reg_id = models.CharField(max_length=30)
    ordr = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_file1'
        unique_together = (('table_name', 'board_id', 'gubun', 'ordr'), ('file_id', 'table_name', 'board_id'),)


class TbFile2(models.Model):
    table_name = models.CharField(primary_key=True, max_length=50)
    board_id = models.CharField(max_length=50)
    org_file_name = models.TextField()
    save_file_name = models.CharField(max_length=50)
    file_size = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField()
    gubun = models.CharField(max_length=50)
    reg_id = models.CharField(max_length=30)
    ordr = models.CharField(max_length=10, blank=True, null=True)
    file_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_file_2'
        unique_together = (('table_name', 'board_id', 'gubun', 'ordr'), ('table_name', 'board_id', 'gubun'),)


class TbItem(models.Model):
    item_code = models.TextField(primary_key=True)
    item_name = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=30)
    sort = models.CharField(max_length=30)
    spec = models.CharField(max_length=30)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_item'


class TbItemBk(models.Model):
    item_code = models.CharField(primary_key=True, max_length=100)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=30)
    sort = models.CharField(max_length=30)
    spec = models.CharField(max_length=30)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_item_bk'


class TbMachine(models.Model):
    machine_code = models.CharField(primary_key=True, max_length=100)
    machine_name = models.CharField(max_length=100)
    line_name = models.CharField(max_length=100)
    manager_main = models.CharField(max_length=30, blank=True, null=True)
    manager_sub = models.CharField(max_length=30, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_machine'


class TbMaterial(models.Model):
    material_code = models.TextField(primary_key=True)
    material_name = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=30)
    sort = models.CharField(max_length=30)
    spec = models.CharField(max_length=30)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_material'


class TbMaterialBk(models.Model):
    material_code = models.CharField(primary_key=True, max_length=50)
    material_name = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=30)
    sort = models.CharField(max_length=30)
    spec = models.CharField(max_length=30)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_material_bk'


class TbMenu(models.Model):
    menu_seq = models.IntegerField(primary_key=True)
    menu_name = models.CharField(max_length=30)
    menu_url = models.CharField(max_length=50)
    menu_upper_flag = models.IntegerField()
    menu_upper_id = models.CharField(max_length=10)
    menu_icon_name = models.CharField(max_length=30, blank=True, null=True)
    menu_icon_feather = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_menu'


class TbNotice(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,auto_created=True)
    notice_subject = models.CharField(max_length=100)
    notice_content = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_notice'


class TbNoticeFile(models.Model):
    uuid = models.CharField(primary_key=True, max_length=100)
    uploadpath = models.CharField(db_column='uploadPath', max_length=200, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=100)  # Field name made lowercase.
    seq = models.ForeignKey(TbNotice, models.DO_NOTHING, db_column='seq')
    extension = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tb_notice_file'


class TbOrder(models.Model):
    order_code = models.CharField(primary_key=True, max_length=100)
    customer_code = models.CharField(max_length=30)
    item_code = models.CharField(max_length=100)
    quantity = models.IntegerField()
    representative_name = models.CharField(max_length=30, blank=True, null=True)
    order_date = models.DateField()
    due_date = models.DateField()
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_order'


class TbPlan(models.Model):
    flag = models.CharField(max_length=5)
    lot_num = models.CharField(max_length=30,primary_key=True)
    order_code = models.CharField(max_length=30, blank=True, null=True, default='')
    item_code = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True, default='')
    due_date = models.DateField()
    reg_date = models.DateField(auto_now_add=True)
    reg_id = models.CharField(max_length=30, default='')
    mod_date = models.DateField(auto_now_add=True)
    mod_id = models.CharField(max_length=30, default='')
    plan_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tb_plan'
        unique_together = (('flag', 'lot_num'),)


class TbProcess(models.Model):
    process_code = models.CharField(primary_key=True, max_length=100)
    process_name = models.CharField(max_length=100)
    sort = models.CharField(max_length=30)
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_process'


class TbProductInout(models.Model):
    product_seq = models.AutoField(primary_key=True)
    inout_flag = models.CharField(max_length=5)
    plan_flag = models.ForeignKey(TbPlan, models.DO_NOTHING, db_column='plan_flag', related_name='inout_flag')
    lot_num = models.ForeignKey(TbPlan, models.DO_NOTHING, db_column='lot_num', related_name='inout_num')
    quantity = models.IntegerField()
    inout_date = models.DateField()
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_product_inout'


class TbProductionLog(models.Model):
    curdatetime = models.CharField(db_column='curDateTime', primary_key=True, max_length=14)  # Field name made lowercase.
    linecode = models.SmallIntegerField(db_column='lineCode')  # Field name made lowercase.
    metalgoodcnt = models.IntegerField(db_column='metalGoodCnt', blank=True, null=True)  # Field name made lowercase.
    metalbadcnt = models.IntegerField(db_column='metalBadCnt', blank=True, null=True)  # Field name made lowercase.
    weightgoodcnt = models.IntegerField(db_column='weightGoodCnt', blank=True, null=True)  # Field name made lowercase.
    weighthighcnt = models.IntegerField(db_column='weightHighCnt', blank=True, null=True)  # Field name made lowercase.
    weightlowcnt = models.IntegerField(db_column='weightLowCnt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_production_log'
        unique_together = (('curdatetime', 'linecode'),)


class TbProgressHist(models.Model):
    plan_flag = models.ForeignKey(TbPlan, models.DO_NOTHING, db_column='plan_flag',related_name='hist_flag')
    lot_num = models.ForeignKey(TbPlan, models.DO_NOTHING, db_column='lot_num', related_name='hist_num')
    process_code = models.CharField(max_length=30)
    working_date = models.DateField()
    flag = models.CharField(max_length=5)
    quantity = models.IntegerField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)
    ordr = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tb_progress_hist'
        unique_together = (('ordr', 'plan_flag', 'lot_num', 'process_code', 'working_date'),)


class TbQc(models.Model):
    lot_num = models.CharField(primary_key=True, max_length=30)
    input_date = models.DateField()
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_qc'


class TbQcDetail(models.Model):
    lot_num = models.CharField(max_length=30)
    ordr = models.AutoField(primary_key=True)
    abnormal_date = models.DateTimeField()
    abnormal_code = models.CharField(max_length=100)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_qc_detail'
        unique_together = (('ordr', 'lot_num'),)


class TbResourceInout(models.Model):
    resource_seq = models.AutoField(primary_key=True)
    material_code = models.CharField(max_length=30)
    inout_flag = models.CharField(max_length=5)
    quantity = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    inout_date = models.DateField()
    note = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_resource_inout'


class TbStaff(models.Model):
    name = models.CharField(max_length=30)
    id = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=255)
    author = models.ForeignKey(TbAuthorGroup, models.DO_NOTHING)
    department = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    email_addr = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    error_cnt = models.IntegerField()
    status = models.CharField(max_length=5, blank=True, null=True)
    reg_date = models.DateField()
    reg_id = models.CharField(max_length=30)
    mod_date = models.DateField()
    mod_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tb_staff'


class TbStatus(models.Model):
    key1 = models.CharField(max_length=255, blank=True, null=True)
    key2 = models.CharField(max_length=255, blank=True, null=True)
    key3 = models.CharField(max_length=255, blank=True, null=True)
    key4 = models.CharField(max_length=255, blank=True, null=True)
    key5 = models.CharField(max_length=255, blank=True, null=True)
    value1 = models.CharField(max_length=255, blank=True, null=True)
    value2 = models.CharField(max_length=255, blank=True, null=True)
    value3 = models.CharField(max_length=255, blank=True, null=True)
    value4 = models.CharField(max_length=255, blank=True, null=True)
    value5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_status'
