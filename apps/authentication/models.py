from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group, Permission
from django.utils import timezone
# Create your models here.

JOB_FUNCTION_CHOICES = [
    ('General & Transverse Management', '横向管理'),
    ('Installation & Field Operations', '安装与现场操作'),
    ('Digital Transformation', '数字化转型'),
    ('Commercial', '商业员工'),
    ('Procurement', '采购'),
    ('Strategy, Innovation, Integration', '战略与创新部门员工'),
    ('Quality', '质量管控'),
    ('Project & Bid', '项目与投标'),
    ('Human Resources', '人力资源'),
    ('Environment, Health & Safety', '环境、健康和安全'),
    ('Supply Chain & Planning', '供应链与规划'),
    ('Legal', '法律部门'),
    ('Industrial', '工业'),
    ('Finance', '金融'),
    ('Engineering', '工程师'),
    ('Communication', '通信'),
]


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class UserForm(AbstractBaseUser, PermissionsMixin):
#    id = models.AutoField(primary_key=True,verbose_name="ID")
    email = models.EmailField(max_length=32, verbose_name="email",unique=True)
    post = models.CharField(max_length=100, verbose_name="post",choices=JOB_FUNCTION_CHOICES)
    name = models.CharField(max_length=32, verbose_name="name")
    city = models.CharField(max_length=64, verbose_name="city",default='No city', null=True)
    department = models.CharField(max_length=100, verbose_name="Department", null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, verbose_name="Age")
    gender = models.IntegerField(null=True, blank=True, verbose_name="gender")
    experience_years = models.IntegerField(verbose_name="Years of Experience", null=True, blank=True)
    education = models.CharField(max_length=15, null=True, blank=True,verbose_name='education')
    equipmentSkillLevel = models.IntegerField(verbose_name="equipmentSkillLevel", null=True, blank=True)
    techSkillLevel=models.IntegerField(verbose_name="techSkillLevel", null=True, blank=True)
    workenvironment = models.CharField(max_length=15,null=True, blank=True, verbose_name="WorkEnvironment") #0现场工作，1非现场
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # 添加 related_name 参数
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # 添加 related_name 参数
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    POST_CHOICES = {
        "General & Transverse Management": "横向管理经理",
        "Installation & Field Operations": "安装与现场操作工人",
        "Digital Transformation": "数字化转型部门",
        "Commercial": "商业员工",
        "Procurement": "采购经理",
        "Strategy, Innovation, Integration": "战略与创新部门员工",
        "Quality": "质量管控经理",
        "Project & Bid": "项目与投标经理",
        "Human Resources": "人力资源管理",
        "Environment, Health & Safety": "环境、健康和安全",
        "Supply Chain & Planning": "供应链与规划项目经理",
        "Legal": "法律员工",
        "Industrial": "工业-现场负责人",
        "Finance": "金融部门员工",
        "Engineering": "工程师",
        "Communication": "通信员工",
        }
    GENDER_CHOICES = {
        1: "男",
        0: "女",
        }
    EDUCATION_CHOICES = {
        "highschool": "高中",
        "juniorcollege": "专科",
        "undergraduate": "本科",
        "master": "硕士",
        "doctor": "博士",
    }
    DEPARTMENT_CHOICES = {
        "Production": "生产部门",
        "Maintenance": "维修",
        "Service": "服务",
        "Commercial": "商业",
        "Executive": "行政",
        "Quality": "质量管控",
    }
    WORK_ENVIRONMENT_CHOICES = {
        "workshop": "生产车间",
        "office": "办公室",
    }
    TECH_SKILL_LEVEL_CHOICES = {
        1: "入门",
        2: "新手",
        3: "熟悉",
        4: "掌握",
        5: "精通",
    }
    EQUIPMENT_SKILL_LEVEL_CHOICES = {
        1: "入门",
        2: "新手",
        3: "熟悉",
        4: "掌握",
        5: "精通",
    }

    def __str__(self):
        return self.email
    def get_post_display(self):
        return self.POST_CHOICES.get(self.post, "未知职位")
    def get_gender_display(self):
        return self.GENDER_CHOICES.get(self.gender, "性别无数据")
    def get_education_display(self):
        return self.EDUCATION_CHOICES.get(self.education, "学历无数据")
    def get_department_display(self):
        return self.DEPARTMENT_CHOICES.get(self.department, "部门无数据")
    def get_workenvironment_display(self):
        return self.WORK_ENVIRONMENT_CHOICES.get(self.workenvironment, "工作环境无数据")
    def get_techSkillLevel_display(self):
        return self.TECH_SKILL_LEVEL_CHOICES.get(self.techSkillLevel, "技术熟练度无数据")
    def get_equipmentSkillLevel_display(self):
        return self.EQUIPMENT_SKILL_LEVEL_CHOICES.get(self.equipmentSkillLevel, "设备操作能力无数据")
    class Meta:
        managed = True
        db_table = 'logininterface_userform'

class DataUsage(models.Model):
    user = models.ForeignKey(UserForm, on_delete=models.CASCADE, related_name='data_usages') #如果收藏数据则加10
    count_footprint = models.IntegerField(default=0, verbose_name="Count Footprint")
    count_maintenance = models.IntegerField(default=0, verbose_name="Count Maintenance")
    count_manufacturing = models.IntegerField(default=0, verbose_name="Count Manufacturing")
    count_manufacturing_CNC = models.IntegerField(default=0, verbose_name="Count Manufacturing_CNC")
    count_examine = models.IntegerField(default=0, verbose_name="Count Examine") #唐车的巡检数据
    count_welding_image = models.IntegerField(default=0, verbose_name="Count Welding Image")
    count_surface_image = models.IntegerField(default=0, verbose_name="Count Contract Image")
    count_welding_data = models.IntegerField(default=0, verbose_name="Count Welding Data")
    count_supplier = models.IntegerField(default=0, verbose_name="Count Supplier")

    class Meta:
        db_table = 'data_usage'

class DashboardUsage(models.Model):
    user = models.ForeignKey(UserForm, on_delete=models.CASCADE, related_name='dashboard_usages') #如果收藏仪表盘则加10
    count_global_view = models.IntegerField(default=0, verbose_name="Count Global View")
    count_global_map = models.IntegerField(default=0, verbose_name="Count Global Map")
    count_site_info = models.IntegerField(default=0, verbose_name="Count Site Info")
    count_employee = models.IntegerField(default=0, verbose_name="Count Employee")
    count_country = models.IntegerField(default=0, verbose_name="Count Country")
    count_contract = models.IntegerField(default=0, verbose_name="Count Contract")  #项目详细信息
    count_projectIDCard = models.IntegerField(default=0, verbose_name="ProjectIDCard")#产品平台图
    count_facilities = models.IntegerField(default=0, verbose_name="Facilities")
    count_supplierGIS = models.IntegerField(default=0, verbose_name="SupplierGIS")


    class Meta:
        db_table = 'dashboard_usage'

class UserFeedback(models.Model):
    user = models.ForeignKey(UserForm, on_delete=models.CASCADE, related_name='feedbacks')
    feedbacktimes = models.IntegerField(default=0, verbose_name="FeedbackTimes")
    comment = models.TextField(verbose_name="Comment")
    datasatisfaction = models.IntegerField(default=5, verbose_name="Datasatisfaction") #数据推荐满意度
    visusatisfaction = models.IntegerField(default=5, verbose_name="Visusatisfaction") #可视化推荐满意度
    usersatisfaction = models.IntegerField(default=5, verbose_name="Usersatisfaction") #用户模型分析满意度
    dataPreference = models.IntegerField(default=0, verbose_name="DataPreference") #数据偏好
    dashPreference = models.IntegerField(default=0, verbose_name="DashPreference")#仪表盘偏好
    visuPreference = models.IntegerField(default=0, verbose_name="VisuPreference")

    DataPreference_Choice = {
        1: "维修数据",
        2: "服务Footprint",
        3: "制造数据",
        4: "CNC制造数据",
        5: "测试数据",
        6: "焊接监测图像",
        7: "表面检测图像",
        8: "焊接数据",
        9: "供应商数据",
    }
    DashPreference_Choice = {
        1: "维修站点关键数据概览",
        2: "全球站点数据",
        3: "场地管理",
        4: "员工信息",
        5: "维修站点地理信息系统（GIS）",
        6: "项目详细信息",
        7: "产品平台图",
        8: "设备分布图",
        9: "供应商GIS",
    }
    VisuPreference_Choice = {
        1: "直方图",
        2: "折线图",
        3: "柱线叠加图",
        4: "饼状图",
        5: "热力图",
        6: "散点图",
        7: "甘特图",
        8: "雷达图",
        9: "多映射联系图",
    }
    def get_DataPreference_display(self):
        return self.DataPreference_Choice.get(self.dataPreference, "维修数据")
    def get_techSkillLevel_display(self):
        return self.DashPreference_Choice.get(self.dashPreference, "维修站点关键数据概览")
    def get_equipmentSkillLevel_display(self):
        return self.VisuPreference_Choice.get(self.visuPreference, "直方图")

    class Meta:
        db_table = 'user_feedback'

class LoginFrequency(models.Model):
    user = models.ForeignKey(UserForm, on_delete=models.CASCADE, related_name='login_frequencies')
    count = models.IntegerField(default=0, verbose_name="Login Count")

    class Meta:
        db_table = 'login_frequency'

class JobFunction(models.Model):
    job_function_code = models.CharField(db_column='Job Function Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    job_function_description = models.CharField(db_column='Job Function Description', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.job_function_description

    class Meta:
        managed = True
        db_table = 'job function'
