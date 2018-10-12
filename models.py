# coding: utf-8
from sqlalchemy import Column, Float, text
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



#cmd运行 sqlacodegen --tables （某一张表） --outfile ../../mappers/Found.py（输出文件目录） mysql+pymysql://root:123456@localhost：3306/welding_process
sqlusername = 'root'
sqlpassword = '123456'
sqlport = '3306'
sqldatabase = 'test'
url = 'mysql+pymysql://{}:{}@localhost:{}/{}?charset=utf8'.format(sqlusername,sqlpassword,sqlport,sqldatabase)

engine = create_engine(url,encoding='utf-8',echo=True)
#创建实例，连接test库，编码类型utf-8，echo=True显示信息

Base = declarative_base()   #生成orm基类

class BrazeWeld(Base):
    __tablename__ = 'braze_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255))
    brazing_filler_model = Column(VARCHAR(255), nullable=False)
    brazing_flux_model = Column(VARCHAR(255))
    temperature = Column(Float, nullable=False)
    shield_gas_type = Column(VARCHAR(255))
    shield_gas_flow = Column(Float)
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))

    __table_args__ = {
        'mysql_charset': 'utf8'    #定义类的编码类型为utf8

    }



class DMeltingPolarArcWeld(Base):
    __tablename__ = 'd_melting_polar_arc_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255), nullable=False)
    joint_clearance = Column(Float)
    groove_type = Column(VARCHAR(255))
    groove_deep = Column(Float)
    weld_position = Column(VARCHAR(255), nullable=False)
    double_wire_position = Column(VARCHAR(255))
    power_polarity = Column(VARCHAR(255))
    current_front = Column(Float)
    wire_feed_speed_f = Column(Float)
    current_back = Column(Float)
    wire_feed_speed_b = Column(Float)
    voltage_front = Column(Float)
    voltage_back = Column(Float)
    arc_length = Column(Float)
    arc_length_correction = Column(Float)
    weld_speed = Column(Float, nullable=False)
    wire_material = Column(VARCHAR(255), nullable=False)
    wire_model = Column(VARCHAR(255), nullable=False)
    wire_diameter = Column(Float, nullable=False)
    wire_extension_length = Column(Float, nullable=False)
    torch_angle = Column(VARCHAR(255))
    weave_type = Column(VARCHAR(255))
    weave_range = Column(Float)
    weave_length = Column(Float)
    weave_frequency = Column(Float)
    shield_gas_type = Column(VARCHAR(255), nullable=False)
    shield_gas_flow = Column(Float, nullable=False)
    gas_purity = Column(Float)
    pulse_peak_current = Column(Float)
    pulse_base_current = Column(Float)
    pulse_frequency = Column(Float)
    duty_cycle = Column(Float)
    weld_machine = Column(VARCHAR(255))
    robot = Column(VARCHAR(255))
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class ElectricResistanceWeld(Base):
    __tablename__ = 'electric_resistance_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255))
    current = Column(VARCHAR(255), nullable=False)
    weld_time = Column(VARCHAR(255), nullable=False)
    pressure = Column(VARCHAR(255), nullable=False)
    resistance_tip_diameter = Column(Float, nullable=False)
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class FrictionStirWeld(Base):
    __tablename__ = 'friction_stir_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255), nullable=False)
    weld_position = Column(VARCHAR(255), nullable=False)
    weld_speed = Column(Float, nullable=False)
    spin_speed = Column(Float, nullable=False)
    down_pressure_distance = Column(Float)
    down_pressure_num = Column(Float)
    back_tilt_angle = Column(VARCHAR(255))
    stir_head_type = Column(VARCHAR(255))
    stir_needle_shape = Column(VARCHAR(255))
    stir_needle_length = Column(Float)
    stir_needle_diameter = Column(Float)
    shaft_shoulder_shape = Column(VARCHAR(255))
    shaft_shoulder_diameter = Column(Float)
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class FrictionStudWeld(Base):
    __tablename__ = 'friction_stud_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    weld_type = Column(VARCHAR(255), nullable=False)
    spin_speed = Column(Float, nullable=False)
    friction_pressure = Column(Float, nullable=False)
    friction_time = Column(Float, nullable=False)
    upsetting_force = Column(Float, nullable=False)
    upsetting_time = Column(Float, nullable=False)
    axial_feed_speed = Column(Float, nullable=False)
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class LaserBeamWeld(Base):
    __tablename__ = 'laser_beam_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255), nullable=False)
    joint_clearance = Column(Float)
    groove_type = Column(VARCHAR(255))
    groove_deep = Column(Float)
    weld_position = Column(VARCHAR(255), nullable=False)
    laser_type = Column(VARCHAR(255))
    defocusing_amount = Column(Float, nullable=False)
    weld_speed = Column(Float, nullable=False)
    laser_power = Column(Float, nullable=False)
    laser_frequency = Column(Float)
    laser_tilt_type = Column(VARCHAR(255), nullable=False)
    laser_tilt_angle = Column(VARCHAR(255), nullable=False)
    laser_beam_position = Column(VARCHAR(255))
    laser_wire_distance = Column(Float)
    arc_current = Column(Float)
    arc_voltage = Column(Float)
    wire_feed_speed = Column(Float)
    wire_material = Column(VARCHAR(255))
    wire_model = Column(VARCHAR(255))
    wire_diameter = Column(Float)
    wire_feed_type = Column(VARCHAR(255))
    wire_feed_angle = Column(VARCHAR(255))
    shield_gas_type = Column(VARCHAR(255), nullable=False)
    shield_gas_flow = Column(Float, nullable=False)
    robot = Column(VARCHAR(255))
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class ManualWeldingRodWeld(Base):
    __tablename__ = 'manual_welding_rod_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255), nullable=False)
    joint_clearance = Column(Float)
    groove_type = Column(VARCHAR(255))
    groove_deep = Column(Float)
    weld_position = Column(VARCHAR(255), nullable=False)
    welding_rod_type = Column(VARCHAR(255), nullable=False)
    welding_rod_material = Column(VARCHAR(255))
    welding_rod_model = Column(VARCHAR(255))
    welding_rod_diameter = Column(Float, nullable=False)
    power_polarity = Column(VARCHAR(255))
    current = Column(Float, nullable=False)
    voltage = Column(Float, nullable=False)
    arc_length = Column(Float)
    weld_speed = Column(Float, nullable=False)
    torch_angle = Column(VARCHAR(255))
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class MeltingPolarArcWeld(Base):
    __tablename__ = 'melting_polar_arc_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255), nullable=False)
    joint_clearance = Column(Float)
    groove_type = Column(VARCHAR(255))
    groove_deep = Column(Float)
    weld_position = Column(VARCHAR(255), nullable=False)
    power_polarity = Column(VARCHAR(255))
    current = Column(Float)
    wire_feed_speed = Column(Float, nullable=False)
    voltage = Column(Float, nullable=False)
    arc_length = Column(Float)
    arc_length_correction = Column(Float)
    weld_speed = Column(Float, nullable=False)
    wire_material = Column(VARCHAR(255), nullable=False)
    wire_model = Column(VARCHAR(255), nullable=False)
    wire_diameter = Column(Float, nullable=False)
    wire_extension_length = Column(Float, nullable=False)
    torch_angle = Column(VARCHAR(255))
    weave_type = Column(VARCHAR(255))
    weave_range = Column(Float)
    weave_length = Column(Float)
    weave_frequency = Column(Float)
    shield_gas_type = Column(VARCHAR(255), nullable=False)
    shield_gas_flow = Column(Float, nullable=False)
    gas_purity = Column(Float)
    pulse_peak_current = Column(Float)
    pulse_base_current = Column(Float)
    pulse_frequency = Column(Float)
    duty_cycle = Column(Float)
    weld_machine = Column(VARCHAR(255))
    robot = Column(VARCHAR(255))
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class NonMeltingPolarArcWeld(Base):
    __tablename__ = 'non_melting_polar_arc_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255))
    workpiece_id_b = Column(VARCHAR(255))
    joint_form = Column(VARCHAR(255))
    joint_clearance = Column(Float)
    groove_type = Column(VARCHAR(255))
    groove_deep = Column(Float)
    weld_position = Column(VARCHAR(255), nullable=False)
    current = Column(Float, nullable=False)
    power_polarity = Column(VARCHAR(255))
    weld_speed = Column(Float, nullable=False)
    voltage = Column(Float, nullable=False)
    arc_length = Column(Float)
    wire_feed_speed = Column(Float)
    wire_material = Column(VARCHAR(255))
    wire_model = Column(VARCHAR(255))
    wire_diameter = Column(Float)
    wire_feed_angle = Column(VARCHAR(255))
    wire_feed_type = Column(VARCHAR(255))
    weave_type = Column(VARCHAR(255))
    weave_range = Column(Float)
    weave_length = Column(Float)
    weave_frequency = Column(Float)
    shield_gas_type = Column(VARCHAR(255), nullable=False)
    shield_gas_flow = Column(Float, nullable=False)
    plasma_gas_type = Column(VARCHAR(255))
    plasma_gas_flow = Column(Float)
    gas_purity = Column(Float)
    pulse_peak_current = Column(Float)
    pulse_base_current = Column(Float)
    pulse_frequency = Column(Float)
    duty_cycle = Column(Float)
    tungsten_electrode_diameter = Column(Float, nullable=False)
    tungsten_top_angle = Column(VARCHAR(255), server_default=text("'30'"))
    tungsten_electrode_extension = Column(Float)
    plasma_nozzle_diameter = Column(Float)
    weld_machine = Column(VARCHAR(255))
    robot = Column(VARCHAR(255))
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class ProductInfo(Base):
    __tablename__ = 'product_info'

    product_id = Column(VARCHAR(255), primary_key=True)
    product_name = Column(VARCHAR(255))
    product_code = Column(VARCHAR(255))
    industry = Column(VARCHAR(255))
    drawing_url = Column(VARCHAR(255))
    weld_number = Column(VARCHAR(255))
    weld_position = Column(VARCHAR(255))
    joint_type = Column(VARCHAR(255))
    cross_section_type = Column(VARCHAR(255))
    length_of_weld = Column(Float)
    welding_quality_grade = Column(VARCHAR(255))
    welding_quality_grade_remark = Column(VARCHAR(255))
    weld_performance_level = Column(VARCHAR(255))
    weld_performance_level_remark = Column(VARCHAR(255))
    stress_grade = Column(VARCHAR(255))
    safety_grade = Column(VARCHAR(255))
    imperfection_quality_level = Column(VARCHAR(255))
    imperfection_quality_level_remark = Column(VARCHAR(255))
    weld_inspection_level = Column(VARCHAR(255))
    weld_inspection_level_remark = Column(VARCHAR(255))
    volumetric_test = Column(VARCHAR(255))
    surface_test = Column(VARCHAR(255))
    visual_examination = Column(VARCHAR(255))
    weld_length_tolerance = Column(VARCHAR(255))
    weld_length_tolerance_remark = Column(VARCHAR(255))
    weld_shape_tolerance = Column(VARCHAR(255))
    weld_shape_tolerance_remark = Column(VARCHAR(255))
    weld_tolerance = Column(VARCHAR(255))
    weld_tolerance_remark = Column(VARCHAR(255))
    weld_method = Column(VARCHAR(255))
    weld_order = Column(VARCHAR(255))


class RobotAttitude(Base):
    __tablename__ = 'robot_attitude'

    work_id = Column(VARCHAR(255), primary_key=True)
    h = Column(Float, nullable=False)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)
    x1 = Column(Float, nullable=False)
    y1 = Column(Float, nullable=False)
    z1 = Column(Float, nullable=False)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    c = Column(Float, nullable=False)
    a1 = Column(Float, nullable=False)
    b1 = Column(Float, nullable=False)
    c1 = Column(Float, nullable=False)
    remark = Column(VARCHAR(255))
    Image_url = Column(VARCHAR(255))


class SubmergeArcWeld(Base):
    __tablename__ = 'submerge_arc_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255), nullable=False)
    joint_clearance = Column(Float)
    groove_type = Column(VARCHAR(255))
    groove_deep = Column(Float)
    weld_position = Column(VARCHAR(255), nullable=False)
    weld_speed = Column(Float, nullable=False)
    power_polarity = Column(VARCHAR(255))
    current = Column(Float)
    wire_feed_speed = Column(Float)
    voltage = Column(Float, nullable=False)
    flux_material = Column(VARCHAR(255))
    flux_model = Column(VARCHAR(255))
    wire_material = Column(VARCHAR(255))
    wire_model = Column(VARCHAR(255))
    wire_diameter = Column(Float, nullable=False)
    wire_feed_angle = Column(VARCHAR(255))
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class VacuumElectronBeamWeld(Base):
    __tablename__ = 'vacuum_electron_beam_weld'

    weld_method = Column(VARCHAR(255), primary_key=True)
    workpiece_id_a = Column(VARCHAR(255), nullable=False)
    workpiece_id_b = Column(VARCHAR(255), nullable=False)
    joint_form = Column(VARCHAR(255), nullable=False)
    joint_clearance = Column(Float)
    groove_type = Column(VARCHAR(255))
    groove_deep = Column(Float)
    weld_position = Column(VARCHAR(255), nullable=False)
    weld_speed = Column(Float, nullable=False)
    acceleration_voltage = Column(Float, nullable=False)
    electron_beam_flow = Column(Float, nullable=False)
    focus_current = Column(Float, nullable=False)
    work_distance = Column(Float, nullable=False)
    vacuum_degree = Column(Float)
    wire_feed_speed = Column(Float)
    wire_material = Column(VARCHAR(255))
    wire_model = Column(VARCHAR(255))
    wire_diameter = Column(Float)
    wire_feed_type = Column(VARCHAR(255))
    wire_feed_angle = Column(VARCHAR(255))
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class WorkpieceInfo(Base):
    __tablename__ = 'workpiece_info'

    workpiece_id = Column(VARCHAR(255), primary_key=True)
    material = Column(VARCHAR(255), nullable=False)
    material_brand = Column(VARCHAR(255), nullable=False)
    shape = Column(VARCHAR(255), nullable=False)
    thickness = Column(Float)
    diameter = Column(Float)
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


Base.metadata.create_all(engine)   #创建以上类对应的数据表结构，若已存在，则忽略


Session = sessionmaker(engine)     #创建与数据库的会话Session,注意,这里返回给session的是个class,不是实例
session = Session()                #生成Session实例，相当于游标
session.commit()                   #统一提交会话，执行操作