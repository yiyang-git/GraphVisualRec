from django.db import models
import os

class FileRecord(models.Model):
    FILE_FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('doc', 'Word Document'),
        ('xls', 'Excel Spreadsheet'),
        ('txt', 'Text File'),
    ]
    FILE_TYPE_CHOICES = [
        ('time_series_structured', 'Structured data in a time-series'),
        ('detection_image_framed', 'Defect detection image with frame'),
        ('detection_image', 'Defect detection image'),
        ('detection_image_structured', 'Defect detection image'),
        ('audio_time_series_structured', 'Segmented audio data and corresponding structured data'),
        ('audio', 'Segmented audio data'),
        ('structured', 'Structured data'),
        ('text', 'Text data'),
        ('detection_image_less_features', 'Defect detection image with less features'),
        ('geodata', 'Geographic data'),
    ]

    file_name = models.CharField(max_length=255)
    file_name_chinese = models.CharField(max_length=255, null=True)
    file_format = models.CharField(max_length=255, choices=FILE_FORMAT_CHOICES)
    file_type = models.CharField(max_length=255, choices=FILE_TYPE_CHOICES)
    file_description = models.TextField()
    data_explanation = models.TextField()
    entities_json = models.JSONField(null=True)
    relations_json = models.JSONField(null=True)

    def __str__(self):
        return self.file_name
def welding_data_upload(instance, filename):

    return f'WeldingImages/{instance.label_number}/{filename}'

class WeldingData(models.Model):

    label_number = models.CharField(max_length=10)
    label = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100, verbose_name="ImageUrl", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 添加上传时间字段
    MotWorkSpeed = models.FloatField(verbose_name="MotWorkSpeed", null=True, blank=True)
    EndTime = models.TimeField(max_length=20, verbose_name="EndTime", null=True, blank=True)
    Stopped = models.BigIntegerField(verbose_name="Stopped", null=True, blank=True)
    WireSpeed = models.FloatField(verbose_name="WireSpeed", null=True, blank=True)
    CurrentStepNumber = models.CharField(max_length=100, verbose_name="CurrentStepNumber", null=True, blank=True)
    H2OFlow = models.FloatField(verbose_name="H2OFlow", null=True, blank=True)
    ProgramNumber = models.CharField(max_length=100, verbose_name="ProgramNumber", null=True, blank=True)
    WorkSpeed = models.FloatField(verbose_name="WorkSpeed", null=True, blank=True)
    JobNumber = models.CharField(max_length=100, verbose_name="JobNumber", null=True, blank=True)
    Voltage = models.FloatField(verbose_name="Voltage", null=True, blank=True)
    LatestMessageId = models.IntegerField(verbose_name="LatestMessageId", null=True, blank=True)
    OpMode = models.CharField(max_length=100, verbose_name="OpMode", null=True, blank=True)
    TPS5000IsRunning = models.BooleanField(verbose_name="TPS5000IsRunning", default=False)
    InAutomatic = models.BigIntegerField(verbose_name="InAutomatic", default=False)
    ToolIsRunning = models.BooleanField(verbose_name="ToolIsRunning", default=False)
    PowerSourceReady = models.BooleanField(verbose_name="PowerSourceReady", default=False)
    DrivesAreOn = models.BooleanField(verbose_name="DrivesAreOn", default=False)
    MaxMessageCount = models.IntegerField(verbose_name="MaxMessageCount", null=True, blank=True)
    StartTime = models.CharField(max_length=20, verbose_name="StartTime", null=True, blank=True)
    MovTCP = models.TextField(verbose_name="MovTCP", null=True, blank=True)  # Assuming this could be a JSON or similar
    Gas = models.FloatField(verbose_name="Gas", null=True, blank=True)
    Running = models.BigIntegerField(verbose_name="Running", default=False)
    MotorCurrent = models.FloatField(verbose_name="MotorCurrent", null=True, blank=True)
    CurrentProgram = models.CharField(max_length=100, verbose_name="CurrentProgram", null=True, blank=True)
    DrivesOn = models.BigIntegerField(verbose_name="DrivesOn", default=False)
    Online = models.BooleanField(verbose_name="Online", default=False)
    Current = models.FloatField(verbose_name="Current", null=True, blank=True)
    ErrorNumber = models.IntegerField(verbose_name="ErrorNumber", null=True, blank=True)
    MessageCount = models.IntegerField(verbose_name="MessageCount", null=True, blank=True)
    Siteinformation = models.CharField(max_length=255, null=True)
    Person = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.label
    class Meta:
        managed = True
        db_table = 'WeldingData'

class GearboxAudio(models.Model):
    audio_file = models.CharField(max_length=255)
    pca1 = models.FloatField(null=True)  # 允许为 null
    pca2 = models.FloatField(null=True)  # 允许为 null
    pca3 = models.FloatField(null=True)  # 允许为 null
    cluster_pca = models.IntegerField(null=True)  # 允许为 null
    data_file = models.CharField(max_length=255)
    fault = models.CharField(max_length=50, null=True)  # 允许为 null
    circulation = models.CharField(max_length=50, null=True)  # 允许为 null
    torque_nm = models.IntegerField(null=True)  # 允许为 null
    rpm = models.IntegerField(null=True)  # 允许为 null
    fault_degree = models.CharField(max_length=50, null=True)
    Siteinformation = models.CharField(max_length=255, null=True)
    Person = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.audio_file} - PCACluster {self.cluster_pca}"

class DefectImage(models.Model):
    image_url = models.CharField(max_length=255)
    defect_type = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    segmented = models.BooleanField()
    object_name = models.CharField(max_length=100)
    pose = models.CharField(max_length=100)
    truncated = models.BooleanField()
    difficult = models.BooleanField()
    bndbox_xmin = models.IntegerField()
    bndbox_ymin = models.IntegerField()
    bndbox_xmax = models.IntegerField()
    bndbox_ymax = models.IntegerField()
    Siteinformation = models.CharField(max_length=255, null=True)
    Person = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.image_url


class DetailedRailroadAccident(models.Model):
    reportingRailroadCode = models.CharField(max_length=100, null=True, blank=True)
    reportingRailroadName = models.CharField(max_length=255, null=True, blank=True)
    reportYear = models.IntegerField(null=True, blank=True)
    accidentNumber = models.CharField(max_length=100, null=True, blank=True)
    pdfLink = models.URLField(null=True, blank=True)
    accidentYear = models.IntegerField(null=True, blank=True)
    accidentMonth = models.IntegerField(null=True, blank=True)
    accidentType = models.CharField(max_length=255, null=True, blank=True)
    division = models.CharField(max_length=255, null=True, blank=True)
    stateName = models.CharField(max_length=255, null=True, blank=True)
    countyName = models.CharField(max_length=255, null=True, blank=True)
    weatherCondition = models.CharField(max_length=255, null=True, blank=True)
    trackType = models.CharField(max_length=255, null=True, blank=True)
    trainDirection = models.CharField(max_length=100, null=True, blank=True)
    trainSpeed = models.IntegerField(null=True, blank=True)
    primaryAccidentCause = models.CharField(max_length=255, null=True, blank=True)
    totalDamageCost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    narrative = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    otherRailroadCode = models.CharField(max_length=100, null=True, blank=True)
    otherRailroadName = models.CharField(max_length=255, null=True, blank=True)
    maintenanceRailroadCode = models.CharField(max_length=100, null=True, blank=True)
    maintenanceRailroadName = models.CharField(max_length=255, null=True, blank=True)
    maintenanceAccidentNumber = models.CharField(max_length=100, null=True, blank=True)
    maintenanceAccidentYear = models.IntegerField(null=True, blank=True)
    maintenanceAccidentMonth = models.IntegerField(null=True, blank=True)
    gradeCrossingID = models.CharField(max_length=100, null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    hazmatCars = models.IntegerField(null=True, blank=True)
    hazmatCarsDamaged = models.IntegerField(null=True, blank=True)
    hazmatReleasedCars = models.IntegerField(null=True, blank=True)
    personsEvacuated = models.IntegerField(null=True, blank=True)
    subdivision = models.CharField(max_length=255, null=True, blank=True)
    milepost = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    signalization = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.reportingRailroadName} {self.accidentNumber}"

class RailwayDetectImage(models.Model):
    image_name = models.CharField(max_length=255)
    image_url = models.TextField()
    mask_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.image_name


class CNCExperimentData(models.Model):
    X1_ActualPosition = models.FloatField(null=True)
    X1_ActualVelocity = models.FloatField(null=True)
    X1_ActualAcceleration = models.FloatField(null=True)
    X1_CommandPosition = models.FloatField(null=True)
    X1_CommandVelocity = models.FloatField(null=True)
    X1_CommandAcceleration = models.FloatField(null=True)
    X1_CurrentFeedback = models.FloatField(null=True)
    X1_DCBusVoltage = models.FloatField(null=True)
    X1_OutputCurrent = models.FloatField(null=True)
    X1_OutputVoltage = models.FloatField(null=True)
    X1_OutputPower = models.FloatField(null=True)
    Y1_ActualPosition = models.FloatField(null=True)
    Y1_ActualVelocity = models.FloatField(null=True)
    Y1_ActualAcceleration = models.FloatField(null=True)
    Y1_CommandPosition = models.FloatField(null=True)
    Y1_CommandVelocity = models.FloatField(null=True)
    Y1_CommandAcceleration = models.FloatField(null=True)
    Y1_CurrentFeedback = models.FloatField(null=True)
    Y1_DCBusVoltage = models.FloatField(null=True)
    Y1_OutputCurrent = models.FloatField(null=True)
    Y1_OutputVoltage = models.FloatField(null=True)
    Y1_OutputPower = models.FloatField(null=True)
    Z1_ActualPosition = models.FloatField(null=True)
    Z1_ActualVelocity = models.FloatField(null=True)
    Z1_ActualAcceleration = models.FloatField(null=True)
    Z1_CommandPosition = models.FloatField(null=True)
    Z1_CommandVelocity = models.FloatField(null=True)
    Z1_CommandAcceleration = models.FloatField(null=True)
    Z1_CurrentFeedback = models.FloatField(null=True)
    Z1_DCBusVoltage = models.FloatField(null=True)
    Z1_OutputCurrent = models.FloatField(null=True)
    Z1_OutputVoltage = models.FloatField(null=True)
    S1_ActualPosition = models.FloatField(null=True)
    S1_ActualVelocity = models.FloatField(null=True)
    S1_ActualAcceleration = models.FloatField(null=True)
    S1_CommandPosition = models.FloatField(null=True)
    S1_CommandVelocity = models.FloatField(null=True)
    S1_CommandAcceleration = models.FloatField(null=True)
    S1_CurrentFeedback = models.FloatField(null=True)
    S1_DCBusVoltage = models.FloatField(null=True)
    S1_OutputCurrent = models.FloatField(null=True)
    S1_OutputVoltage = models.FloatField(null=True)
    S1_OutputPower = models.FloatField(null=True)
    S1_SystemInertia = models.FloatField(null=True)
    M1_CURRENT_PROGRAM_NUMBER = models.IntegerField(null=True)
    M1_sequence_number = models.IntegerField(null=True)
    M1_CURRENT_FEEDRATE = models.FloatField(null=True)
    Machining_Process = models.CharField(max_length=100, null=True)
    experiment = models.CharField(max_length=100, null=True)
    material = models.CharField(max_length=100, null=True)
    feedrate = models.FloatField(null=True)
    clamp_pressure = models.FloatField(null=True)
    tool_condition = models.CharField(max_length=100, null=True)
    machining_finalized = models.CharField(max_length=100, null=True)
    passed_visual_inspection = models.CharField(max_length=100, null=True)
    Siteinformation = models.CharField(max_length=255, null=True)
    Person = models.CharField(max_length=255, null=True)

class CNCDataList(models.Model):
    experiment_id = models.CharField(max_length=50, unique=True)
    material = models.CharField(max_length=50)
    feedrate = models.FloatField()
    clamp_pressure = models.FloatField()
    tool_condition = models.CharField(max_length=50)
    machining_finalized = models.CharField(max_length=50)
    passed_visual_inspection = models.CharField(max_length=50)
    Siteinformation = models.CharField(max_length=255, null=True)
    Person = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.experiment_id

class MotorAudio(models.Model):
    audio_url = models.URLField(max_length=200)
    file_name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    Siteinformation = models.CharField(max_length=255, null=True)
    Person = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.file_name

class Data_uploaded(models.Model):
    Name = models.CharField(max_length=255, null=True)
    Description = models.TextField(null=True)
    Synonyms = models.CharField(max_length=255, null=True)
    Data_domain = models.CharField(max_length=255, null=True)
    Data_Type = models.CharField(max_length=255, null=True)

class Contract_desensitization_uploaded(models.Model):
    ContractID = models.CharField(max_length=255, null=True)
    ContractName = models.CharField(max_length=255, null=True)
    ContractType = models.CharField(max_length=255, null=True)
    Countryinformation = models.CharField(max_length=255, null=True)
    CountryCode = models.CharField(max_length=255, null=True)
    Clusterinformation = models.CharField(max_length=255, null=True)
    ClusterCode = models.CharField(max_length=255, null=True)
    Regioninformation = models.CharField(max_length=255, null=True)
    RegionCode = models.CharField(max_length=255, null=True)
    Currencyinformation = models.CharField(max_length=255, null=True)
    CurrencyCode = models.CharField(max_length=255, null=True)
    Customerinformation = models.CharField(max_length=255, null=True)
    CustomerID = models.CharField(max_length=255, null=True)
    Productinformation = models.CharField(max_length=255, null=True)
    ProductID = models.CharField(max_length=255, null=True)
    Segmentation = models.CharField(max_length=255, null=True)
    ProductFamilyinformation = models.CharField(max_length=255, null=True)
    ProductFamilyID = models.CharField(max_length=255, null=True)
    Platforminformation = models.CharField(max_length=255, null=True)
    PlatformID = models.CharField(max_length=255, null=True)
    ContractStartDate = models.DateTimeField(null=True)
    ContractFullyTradedDate = models.DateTimeField(null=True)



class Building_desensitization_uploaded(models.Model):
    Regioninformation = models.CharField(max_length=255, null=True)
    RegionCode = models.CharField(max_length=255, null=True)
    Clusterinformation = models.CharField(max_length=255, null=True)
    ClusterCode = models.CharField(max_length=255, null=True)
    Countryinformation = models.CharField(max_length=255, null=True)
    CountryCode = models.CharField(max_length=255, null=True)
    Siteinformation = models.CharField(max_length=255, null=True)
    SiteCode = models.CharField(max_length=255, null=True)
    BuildingCode = models.CharField(max_length=255, null=True)
    Buildinginformation = models.CharField(max_length=255, null=True)
    BuildingType = models.CharField(max_length=255, null=True)
    Activityinformation = models.CharField(max_length=255, null=True)
    CompanyName = models.CharField(max_length=255, null=True)
    CriticalBuilding = models.CharField(max_length=255, null=True)
    Street = models.CharField(max_length=255, null=True)
    ZipCode = models.CharField(max_length=255, null=True)
    State = models.CharField(max_length=255, null=True)
    FormerBuildingCode = models.CharField(max_length=255, null=True)
    WorkingDays = models.CharField(max_length=255, null=True)
    TimeZone = models.CharField(max_length=255, null=True)

class Application_desensitization_uploaded(models.Model):
    ApplicationId = models.IntegerField(null=True)
    ApplicationName = models.CharField(max_length=255, null=True)
    Description = models.TextField(null=True)
    AppStatus = models.CharField(max_length=255, null=True)
    Sub_Status = models.CharField(max_length=255, null=True)
    ComponentCriticality = models.CharField(max_length=255, null=True)
    ApplicationSupportLevel = models.CharField(max_length=255, null=True)
    HostingType = models.CharField(max_length=255, null=True)
    OperationOwnerinformation = models.CharField(max_length=255, null=True)
    OperationOwner_Id = models.FloatField(null=True)
    Architectinformation = models.CharField(max_length=255, null=True)
    Architect_Id = models.FloatField(null=True)
    BusinessOwnerinformation = models.CharField(max_length=255, null=True)
    BusinessOwner_Id = models.FloatField(null=True)
    SupportTower = models.CharField(max_length=255, null=True)
    ArchitectureAccountableTower = models.CharField(max_length=255, null=True)
    IS_TSupport = models.CharField(max_length=255, null=True)
    TypeofIS_TSupport = models.CharField(max_length=255, null=True)
    SupportVendor = models.CharField(max_length=255, null=True)
    TechnicalApproverinformation = models.CharField(max_length=255, null=True)
    TechnicalApprover_Id = models.FloatField(null=True)
    SupportGroup = models.CharField(max_length=255, null=True)
    ApplicativeLicensing_AIP = models.CharField(max_length=255, null=True)
    Client = models.CharField(max_length=255, null=True)
    ThickClientInstallationonWorkstation = models.CharField(max_length=255, null=True)
    Accessibility = models.CharField(max_length=255, null=True)
    Subcategory = models.CharField(max_length=255, null=True)
    GeoScope = models.CharField(max_length=255, null=True)
    UsageLocation = models.CharField(max_length=255, null=True)
    ActiveEndUsers = models.CharField(max_length=255, null=True)
    ClientInstalledonComputer = models.BooleanField(null=True)
    EndUserAuthMode = models.CharField(max_length=255, null=True)
    EndUserProtocol = models.CharField(max_length=255, null=True)
    ApplicativeAdminAuthmode = models.CharField(max_length=255, null=True)
    ApplicativeAdminProtocol = models.CharField(max_length=255, null=True)
    TechnicalAdminAuthmode = models.CharField(max_length=255, null=True)
    TechAdminProtocol = models.CharField(max_length=255, null=True)
    RoadmapRecommendation = models.CharField(max_length=255, null=True)
    TechnologyObsolescence = models.CharField(max_length=255, null=True)




class BankRepository_desensitization_uploaded(models.Model):
    RECORDKEY = models.CharField(max_length=255, null=True)
    COUNTRYNAMEinformation = models.CharField(max_length=255, null=True)
    COUNTRYNAME_CountryCode = models.CharField(max_length=255, null=True)
    NATIONALID = models.CharField(max_length=255, null=True)
    INSTITUTIONNAME = models.CharField(max_length=255, null=True)
    BRANCHINFORMATION = models.CharField(max_length=255, null=True)
    OFFICETYPE = models.CharField(max_length=255, null=True)
    STREETADDRESS1 = models.CharField(max_length=255, null=True)
    STREETADDRESS2 = models.CharField(max_length=255, null=True)
    CITY = models.CharField(max_length=255, null=True)
    ZIPCODE = models.CharField(max_length=255, null=True)
    Country_Province_State = models.CharField(max_length=255, null=True)
    CONNECTEDBIC = models.CharField(max_length=255, null=True)
    NETWORKCONNECTIVITY = models.CharField(max_length=255, null=True)
    TIMEZONE = models.CharField(max_length=255, null=True)
    NATIONALIDTYPE = models.CharField(max_length=255, null=True)



class desensitized_design_authority_uploaded(models.Model):
    Code = models.IntegerField(null=True)
    Name = models.CharField(max_length=255, null=True)
    ProductLineinformation = models.CharField(max_length=255, null=True)
    ProductStructureID = models.CharField(max_length=255, null=True)
    ProductLineID = models.CharField(max_length=255, null=True)
    Platforminformation = models.CharField(max_length=255, null=True)
    Referent_person1 = models.CharField(max_length=255, null=True)
    Referent_person2 = models.CharField(max_length=255, null=True)
    Referent_person3 = models.CharField(max_length=255, null=True)
    Referent_person4 = models.CharField(max_length=255, null=True)
    Designer_person1 = models.CharField(max_length=255, null=True)
    Designer_person2 = models.CharField(max_length=255, null=True)
    Designer_person3 = models.CharField(max_length=255, null=True)
    Designer_person4 = models.CharField(max_length=255, null=True)
    Designer_person5 = models.CharField(max_length=255, null=True)
    Designer_person6 = models.CharField(max_length=255, null=True)
    ManagementProcessCompliant = models.FloatField(null=True)
    PartsAuthoringEligibility = models.CharField(max_length=255, null=True)
    Siteinformation = models.CharField(max_length=255, null=True)
    SiteCode = models.CharField(max_length=255, null=True)

class desensitized_internal_supplier_large_uploaded(models.Model):
    InternalSupplierCode = models.CharField(max_length=255, null=True)
    Name = models.CharField(max_length=255, null=True)
    SecondaryName = models.CharField(max_length=255, null=True)
    AccountGroup = models.CharField(max_length=255, null=True)
    TradingPartnerinformation = models.CharField(max_length=255, null=True)
    TradingPartner_ReportingUnit = models.FloatField(null=True)
    Countryinformation = models.CharField(max_length=255, null=True)
    CountryCode = models.CharField(max_length=255, null=True)
    City = models.CharField(max_length=255, null=True)
    Street = models.CharField(max_length=255, null=True)
    PostalCode = models.CharField(max_length=255, null=True)

class InternationalCustomsCode_uploaded(models.Model):
    Level = models.CharField(max_length=255, null=True)
    Parentinformation = models.CharField(max_length=255, null=True)
    Parent_CustomsCode = models.FloatField(null=True)
    CustomsCode = models.IntegerField(null=True)
    Longdescription_English = models.TextField(null=True)
    Shortdescription_English = models.CharField(max_length=255, null=True)
    Source = models.CharField(max_length=255, null=True)


class JobLibrary_uploaded(models.Model):
    PositionID = models.CharField(max_length=255, null=True)
    PositionTitle = models.CharField(max_length=255, null=True)
    StandardJobTitle = models.CharField(max_length=255, null=True)
    JobCodeinformation = models.CharField(max_length=255, null=True)
    JobCode_JobCodeID = models.CharField(max_length=255, null=True)
    JobFunctioninformation = models.CharField(max_length=255, null=True)
    JobFunction_JobFunctionCode = models.CharField(max_length=255, null=True)
    IsStandardJob = models.BooleanField(null=True)
    StandardJobDifferentiators = models.TextField(null=True)

class LocalCustoms_uploaded(models.Model):
    Parentinformation = models.CharField(max_length=255, null=True)
    Parent_CustomsCode = models.CharField(max_length=255, null=True)
    Countryinformation = models.CharField(max_length=255, null=True)
    CountryCode = models.CharField(max_length=255, null=True)
    LocalCustomsCode = models.CharField(max_length=255, null=True)
    LongDescription_English = models.TextField(max_length=255, null=True)
    ShortDescription_English = models.TextField(max_length=255, null=True)

class Material_uploaded(models.Model):
    MaterialID = models.CharField(max_length=255, null=True)
    PCRMaterialFamily = models.CharField(max_length=255, null=True)
    MaterialName = models.CharField(max_length=255, null=True)
    DMADescription = models.CharField(max_length=255, null=True)
    MaterialFamily = models.CharField(max_length=255, null=True)
    Shape = models.CharField(max_length=255, null=True)
    Density_Kg_m3 = models.IntegerField(null=True)
    Standards = models.CharField(max_length=255, null=True)

class PartItem_BaselinePPL_PPLEN_NAMConnectors_uploaded(models.Model):
    PPLinformation = models.CharField(max_length=255, null=True)
    PPL_PPLID = models.IntegerField(null=True)
    MaterialName = models.CharField(max_length=255, null=True)
    CompanyAPartNumberinformation = models.CharField(max_length=255, null=True)
    CompanyAPartNumber_CompanyAPartNumber = models.CharField(max_length=255, null=True)
    PartShortDescriptioninformation = models.CharField(max_length=255, null=True)
    PartShortDescription_CompanyAPartNumber = models.CharField(max_length=255, null=True)
    PPLStatus = models.CharField(max_length=255, null=True)
    RevisionLevel = models.CharField(max_length=255, null=True)
    PPLClassificationinformation = models.CharField(max_length=255, null=True)
    PPLClassification_PPLClassificationID = models.IntegerField(null=True)
    FamilyClassificationAttributes = models.TextField(null=True)

class PartItem_BaselinePPL_Glue_Mastic_uploaded(models.Model):
    PPLinformation = models.CharField(max_length=255, null=True)
    PPL_PPLID = models.IntegerField(null=True)
    MaterialName = models.CharField(max_length=255, null=True)
    CompanyAPartNumberinformation = models.CharField(max_length=255, null=True)
    CompanyAPartNumber_CompanyAPartNumber = models.CharField(max_length=255, null=True)
    PartShortDescriptioninformation = models.CharField(max_length=255, null=True)
    PartShortDescription_CompanyAPartNumber = models.CharField(max_length=255, null=True)
    PPLStatus = models.CharField(max_length=255, null=True)
    RevisionLevel = models.CharField(max_length=255, null=True)
    PPLClassificationinformation = models.CharField(max_length=255, null=True)
    PPLClassification_PPLClassificationID = models.IntegerField(null=True)
    FamilyClassificationAttributes = models.TextField(null=True)

class PartItem_BaselinePPL_Oil_Grease_uploaded(models.Model):
    PPLinformation = models.CharField(max_length=255, null=True)
    PPL_PPLID = models.IntegerField(null=True)
    MaterialName = models.CharField(max_length=255, null=True)
    CompanyAPartNumberinformation = models.CharField(max_length=255, null=True)
    CompanyAPartNumber_CompanyAPartNumber = models.CharField(max_length=255, null=True)
    PartShortDescriptioninformation = models.CharField(max_length=255, null=True)
    PartShortDescription_CompanyAPartNumber = models.CharField(max_length=255, null=True)
    PPLStatus = models.CharField(max_length=255, null=True)
    RevisionLevel = models.CharField(max_length=255, null=True)
    PPLClassificationinformation = models.CharField(max_length=255, null=True)
    PPLClassification_PPLClassificationID = models.IntegerField(null=True)
    FamilyClassificationAttributes = models.TextField(null=True)

class PartItem_BaselinePPL_Partlink_uploaded(models.Model):
    PPLinformation = models.CharField(max_length=255, null=True)
    PPL_PPLID = models.IntegerField(null=True)
    MaterialName = models.CharField(max_length=255, null=True)
    CompanyAPartNumberinformation = models.CharField(max_length=255, null=True)
    CompanyAPartNumber_CompanyAPartNumber = models.CharField(max_length=255, null=True)
    PartShortDescriptioninformation = models.CharField(max_length=255, null=True)
    PartShortDescription_CompanyAPartNumber = models.CharField(max_length=255, null=True)
    PPLStatus = models.CharField(max_length=255, null=True)
    RevisionLevel = models.CharField(max_length=255, null=True)
    PPLClassificationinformation = models.CharField(max_length=255, null=True)
    PPLClassification_PPLClassificationID = models.IntegerField(null=True)
    FamilyClassificationAttributes = models.TextField(null=True)


class Plant_uploaded(models.Model):
    PlantCode = models.CharField(max_length=255, null=True)
    PlantName = models.CharField(max_length=255, null=True)
    System = models.CharField(max_length=255, null=True)
    PlantID = models.FloatField(null=True)
    Siteinformation = models.CharField(max_length=255, null=True)
    SiteCode = models.CharField(max_length=255, null=True)
    ManagingUnitinformation = models.CharField(max_length=255, null=True)
    ManagingUnitId = models.FloatField(null=True)
    ReportingUnitinformation = models.CharField(max_length=255, null=True)
    ReportingUnit_ReportingUnit = models.CharField(max_length=255, null=True)
    Businessinformation = models.CharField(max_length=255, null=True)
    Business_ProductStructureID = models.CharField(max_length=255, null=True)

class Services_Footprint_uploaded(models.Model):
    FootprintID = models.IntegerField(null=True)
    Buildinginformation = models.CharField(max_length=255, null=True)
    BuildingKey = models.FloatField(null=True)
    Siteinformation = models.CharField(max_length=255, null=True)
    SiteCode = models.CharField(max_length=255, null=True)
    SiteKeycontactinformation = models.CharField(max_length=255, null=True)
    SiteKeycontact_Id = models.IntegerField(null=True)
    Regioninformation = models.CharField(max_length=255, null=True)
    RegionCode = models.CharField(max_length=255, null=True)
    Clusterinformation = models.CharField(max_length=255, null=True)
    Cluster_ClusterCode = models.CharField(max_length=255, null=True)
    Countryinformation = models.CharField(max_length=255, null=True)
    CountryCode = models.CharField(max_length=255, null=True)
    SiteCityinformation = models.CharField(max_length=255, null=True)
    SiteCityCode = models.CharField(max_length=255, null=True)
    ExternalSiteCity = models.CharField(max_length=255, null=True)
    ReportingUnitinformation = models.CharField(max_length=255, null=True)
    ReportingUnit = models.CharField(max_length=255, null=True)
    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)
    Abilitytoinfluenceactivities = models.CharField(max_length=255, null=True)
    CompanyABlueCollarscount = models.FloatField(null=True)
    CompanyAWhiteCollarscount = models.FloatField(null=True)
    Joint_Venture = models.BooleanField(null=True)
    NameofPartner = models.CharField(max_length=255, null=True)
    APSYSUnitName = models.CharField(max_length=255, null=True)
    APSYSUnitScope = models.CharField(max_length=255, null=True)
    Legacy = models.CharField(max_length=255, null=True)
    AssetLifeManagement_ALM = models.BooleanField(null=True)
    RollingStockMaintenance_RSM = models.BooleanField(null=True)
    SystemMaintenance = models.BooleanField(null=True)
    TrainOperations_SystemMaintenance_TO_SM = models.BooleanField(null=True)
    TechnicalSupportandSparesSupplyAgreement_TSSSA = models.BooleanField(null=True)
    CrashRepair_CarBody = models.BooleanField(null=True)
    ComponentServiceCenter_CSC = models.BooleanField(null=True)
    ComponentRepairsOverhaul_CRO = models.BooleanField(null=True)
    CROSite_CROActivitywithmultipleCustomers_Products = models.FloatField(null=True)
    CRO_Bogies = models.FloatField(null=True)
    CRO_Wheelsets = models.FloatField(null=True)
    CRO_Motors = models.FloatField(null=True)
    CRO_Gearboxes = models.FloatField(null=True)
    CRO_Brakes = models.FloatField(null=True)
    CRO_Traction = models.FloatField(null=True)
    CRO_Electronics = models.FloatField(null=True)
    CRO_Pantograph = models.FloatField(null=True)
    CRO_Doors = models.FloatField(null=True)
    CRO_HVAC = models.FloatField(null=True)
    CRO_Battery = models.FloatField(null=True)
    ProductIntroduction_PI = models.BooleanField(null=True)
    MultipleContracts = models.BooleanField(null=True)
    Contractsinformation = models.CharField(max_length=255, null=True)
    Contracts_ContractID = models.CharField(max_length=255, null=True)
    ProductPlatform = models.CharField(max_length=255, null=True)
    RSplatform = models.CharField(max_length=255, null=True)
    NbVehicles_Cars = models.IntegerField(null=True)
    NTPDate = models.DateTimeField(null=True)
    ProjectDuration_years = models.FloatField(null=True)
    ServicesExecutionSystem_SES_DigitalWhiteBoard_DWB_implemented = models.BooleanField(null=True)
    MaintenanceManagementInformationSystem = models.CharField(max_length=255, null=True)
    EnterpriseResourcePlanning_ERP = models.CharField(max_length=255, null=True)
    DynamicMaintenancePlanning_DMP_DepotoftheFuture_DoF = models.CharField(max_length=255, null=True)
    RealEstateStatus = models.CharField(max_length=255, null=True)
    ServiceSiteSurface_excludingWhandRSC_m2 = models.FloatField(null=True)
    WarehouseSurface_m2 = models.FloatField(null=True)
    ServiceTrackLength_m = models.FloatField(null=True)
    NumberofServiceTracks = models.FloatField(null=True)
    ParkingTracks = models.BooleanField(null=True)
    MaxParkingTrackLength_m = models.IntegerField(null=True)
    RailwayNetworkConnection = models.BooleanField(null=True)
    Paintingbooth = models.BooleanField(null=True)
    PaintingLengthMaxCapacity_m = models.FloatField(null=True)
    Sandblasting = models.BooleanField(null=True)
    SteelWelding = models.BooleanField(null=True)
    AluminumWelding = models.BooleanField(null=True)
    StainlessWelding = models.BooleanField(null=True)
    WheelLathe = models.BooleanField(null=True)
    PitLathe = models.BooleanField(null=True)
    ElectricalStaticTesting = models.BooleanField(null=True)
    DynamicTesting = models.BooleanField(null=True)
    Wiringtesters = models.BooleanField(null=True)
    LiftingJacks = models.BooleanField(null=True)
    OverheadCranes = models.BooleanField(null=True)
    Trackonpit = models.BooleanField(null=True)
    DropTablepit = models.BooleanField(null=True)
    CleaningStation = models.BooleanField(null=True)
    Watertightness = models.BooleanField(null=True)
    Leveledtracks = models.BooleanField(null=True)
    WeighingandGauge = models.BooleanField(null=True)
    Printers = models.BooleanField(null=True)
    WorkwithAsbestos = models.BooleanField(null=True)
    Trainscanner_AVIS = models.BooleanField(null=True)


class UnitOfMeasure_uploaded(models.Model):
    UnitID = models.CharField(max_length=255, null=True)
    UnitName = models.CharField(max_length=255, null=True)
    Symbol = models.CharField(max_length=255, null=True)
    UnitType = models.CharField(max_length=255, null=True)

class Term_uploaded(models.Model):
    Label = models.CharField(max_length=255, null=True)
    Definition = models.TextField(null=True)
    Acronym = models.CharField(max_length=255, null=True)
    Businessinformation = models.CharField(max_length=255, null=True)
    Business_ProductStructureID = models.CharField(max_length=255, null=True)


# Create your models here.
