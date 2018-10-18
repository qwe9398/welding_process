# coding: utf-8
from sqlalchemy import Column, Float, text ,INTEGER
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



#cmd运行 sqlacodegen --tables （某一张表） --outfile ../../mappers/Found.py（输出文件目录） mysql+pymysql://root:123456@localhost:3306/welding_process
sqlusername = 'root'
sqlpassword = '123456'
sqlport = '3306'
sqldatabase = 'test'
url = 'mysql+pymysql://{}:{}@localhost:{}/{}?charset=utf8'.format(sqlusername,sqlpassword,sqlport,sqldatabase)

engine = create_engine(url,encoding='utf-8',echo=True)
#创建实例，连接test库，编码类型utf-8，echo=True显示信息

Base = declarative_base()   #生成orm基类

class BrazeWeld(Base):#钎焊
    __tablename__ = 'braze_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255),comment='接头形式')
    brazing_filler_model = Column(VARCHAR(255), nullable=False,comment='钎料型号')
    brazing_flux_model = Column(VARCHAR(255),comment='钎剂型号')
    temperature = Column(Float, nullable=False,comment='温度  单位℃')
    shield_gas_type = Column(VARCHAR(255),comment='保护气类型')
    shield_gas_flow = Column(Float,comment='保护气流量  单位L/min')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))

    __table_args__ = {
        'mysql_charset': 'utf8'    #定义类的编码类型为utf8

    }



class DMeltingPolarArcWeld(Base):#双丝熔化极电弧气保焊
    __tablename__ = 'd_melting_polar_arc_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255), nullable=False,comment='接头形式')
    joint_clearance = Column(Float,comment='接头间隙  单位mm')
    groove_type = Column(VARCHAR(255),comment='焊接坡口形式')
    groove_deep = Column(Float,comment='坡口深度（深度为+ 钝边为-）  单位mm')
    weld_position = Column(VARCHAR(255), nullable=False,comment='焊接位置')
    double_wire_position = Column(VARCHAR(255),comment='双丝位置  前后or并列')
    power_polarity = Column(VARCHAR(255),comment='电源极性')
    current_front = Column(Float,comment='前丝电流  单位A')
    wire_feed_speed_f = Column(Float,comment='前丝 送丝速度  单位m/min')
    current_back = Column(Float,comment='后丝电流  单位A')
    wire_feed_speed_b = Column(Float,comment='后丝 送丝速度  单位m/min')
    voltage_front = Column(Float,comment='前丝电压  单位V')
    voltage_back = Column(Float,comment='后丝电压  单位V')
    arc_length = Column(Float,comment='弧长  单位mm')
    arc_length_correction = Column(Float,comment='弧长修正  单位%')
    weld_speed = Column(Float, nullable=False,comment='焊接速度  单位cm/min')
    wire_material = Column(VARCHAR(255), nullable=False,comment='焊丝材料')
    wire_model = Column(VARCHAR(255), nullable=False,comment='焊丝牌号')
    wire_diameter = Column(Float, nullable=False,comment='焊丝直径  单位mm')
    wire_extension_length = Column(Float, nullable=False,comment='焊丝干伸长  单位mm')
    torch_angle = Column(VARCHAR(255),comment='焊枪角度')
    weave_type = Column(VARCHAR(255),comment='摆动（焊）类型')
    weave_range = Column(Float,comment='摆动幅度  单位mm')
    weave_length = Column(Float,comment='摆长  单位mm')
    weave_frequency = Column(Float,comment='摆动频率  单位Hz')
    shield_gas_type = Column(VARCHAR(255), nullable=False,comment='保护气类型')
    shield_gas_flow = Column(Float, nullable=False,comment='保护气流量  单位L/min')
    gas_purity = Column(Float,comment='气体纯度  单位%')
    pulse_peak_current = Column(Float,comment='脉冲峰值电流  单位A')
    pulse_base_current = Column(Float,comment='脉冲基值电流  单位A')
    pulse_frequency = Column(Float,comment='脉冲频率  单位Hz')
    duty_cycle = Column(Float,comment='占空比')
    weld_machine = Column(VARCHAR(255),comment='焊机品牌')
    robot = Column(VARCHAR(255),comment='机器人品牌')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class ElectricResistanceWeld(Base):#电阻焊
    __tablename__ = 'electric_resistance_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255),comment='接头形式')
    current = Column(VARCHAR(255), nullable=False,comment='焊接电流  单位A')
    weld_time = Column(VARCHAR(255), nullable=False,comment='电阻焊时间  单位s')
    pressure = Column(VARCHAR(255), nullable=False,comment='压力大小  单位MPa')
    resistance_tip_diameter = Column(Float, nullable=False,comment='电阻顶端直径  单位mm')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class FrictionStirWeld(Base):#搅拌摩擦焊
    __tablename__ = 'friction_stir_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255), nullable=False,comment='接头形式')
    weld_position = Column(VARCHAR(255), nullable=False,comment='焊接位置')
    weld_speed = Column(Float, nullable=False,comment='焊接速度  单位cm/min')
    spin_speed = Column(Float, nullable=False,comment='旋转速度  单位r/min')
    down_pressure_distance = Column(Float,comment='下压量  单位mm')
    down_pressure_num = Column(Float,comment='下压力  单位MPa')
    back_tilt_angle = Column(VARCHAR(255),comment='搅拌头后倾角度  单位°')
    stir_head_type = Column(VARCHAR(255),comment='搅拌头类型')
    stir_needle_shape = Column(VARCHAR(255),comment='搅拌针形状')
    stir_needle_length = Column(Float,comment='搅拌针长度  单位mm')
    stir_needle_diameter = Column(Float,comment='搅拌针直径  单位mm')
    shaft_shoulder_shape = Column(VARCHAR(255),comment='轴肩形状')
    shaft_shoulder_diameter = Column(Float,comment='轴肩直径  单位mm')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class FrictionStudWeld(Base):#摩擦螺柱焊
    __tablename__ = 'friction_stud_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    weld_type = Column(VARCHAR(255), nullable=False,comment='焊接类型')
    spin_speed = Column(Float, nullable=False,comment='旋转速度  单位r/min')
    friction_pressure = Column(Float, nullable=False,comment='摩擦压力  单位MPa')
    friction_time = Column(Float, nullable=False,comment='摩擦时间  单位s')
    upsetting_force = Column(Float, nullable=False,comment='顶锻力  单位MPa')
    upsetting_time = Column(Float, nullable=False,comment='顶锻时间  单位s')
    axial_feed_speed = Column(Float, nullable=False,comment='轴向进给速度  单位mm/s')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class LaserBeamWeld(Base):#激光焊
    __tablename__ = 'laser_beam_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255), nullable=False,comment='接头形式')
    joint_clearance = Column(Float,comment='接头间隙  单位mm')
    groove_type = Column(VARCHAR(255),comment='坡口类型')
    groove_deep = Column(Float,comment='坡口深度（深度为+ 钝边为-）  单位mm')
    weld_position = Column(VARCHAR(255), nullable=False,comment='焊接位置')
    laser_type = Column(VARCHAR(255),comment='激光器类型')
    defocusing_amount = Column(Float, nullable=False,comment='离焦量  单位mm')
    weld_speed = Column(Float, nullable=False,comment='焊接速度  单位cm/min')
    laser_power = Column(Float, nullable=False,comment='激光功率  单位W')
    laser_frequency = Column(Float,comment='激光频率  单位Hz')
    laser_tilt_type = Column(VARCHAR(255), nullable=False,comment='激光倾斜类型（前倾or后倾）')
    laser_tilt_angle = Column(VARCHAR(255), nullable=False,comment='激光倾斜角度')
    laser_beam_position = Column(VARCHAR(255),comment='激光束位置')
    laser_wire_distance = Column(Float,comment='（送丝焊）光丝间距  单位mm')
    arc_current = Column(Float,comment='（激光电弧复合）电弧电流  单位A')
    arc_voltage = Column(Float,comment='（激光电弧复合）电弧电压  单位V')
    wire_feed_speed = Column(Float,comment='送丝速度  单位m/min')
    wire_material = Column(VARCHAR(255),comment='焊丝材料')
    wire_model = Column(VARCHAR(255),comment='焊丝牌号')
    wire_diameter = Column(Float,comment='焊丝直径  单位mm')
    wire_feed_type = Column(VARCHAR(255),comment='送丝类型（前送丝or后送丝）')
    wire_feed_angle = Column(VARCHAR(255),comment='送丝角度')
    shield_gas_type = Column(VARCHAR(255), nullable=False,comment='保护气类型')
    shield_gas_flow = Column(Float, nullable=False,comment='保护气流量  单位L/min')
    robot = Column(VARCHAR(255),comment='机器人品牌')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class ManualWeldingRodWeld(Base):#手工焊条焊
    __tablename__ = 'manual_welding_rod_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255), nullable=False,comment='接头形式')
    joint_clearance = Column(Float,comment='接头间隙  单位mm')
    groove_type = Column(VARCHAR(255),comment='坡口类型')
    groove_deep = Column(Float,comment='坡口深度（深度为+ 钝边为-）  单位mm')
    weld_position = Column(VARCHAR(255), nullable=False,comment='焊接位置')
    welding_rod_type = Column(VARCHAR(255), nullable=False,comment='焊条类型')
    welding_rod_material = Column(VARCHAR(255),comment='焊条材料')
    welding_rod_model = Column(VARCHAR(255),comment='焊条牌号')
    welding_rod_diameter = Column(Float, nullable=False,comment='焊条直径  单位mm')
    power_polarity = Column(VARCHAR(255),comment='电源极性')
    current = Column(Float, nullable=False,comment='电流  单位A')
    voltage = Column(Float, nullable=False,comment='电压  单位V')
    arc_length = Column(Float,comment='弧长  单位mm')
    weld_speed = Column(Float, nullable=False,comment='焊接速度  单位cm/min')
    torch_angle = Column(VARCHAR(255),comment='焊接角度')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class MeltingPolarArcWeld(Base):#熔化极电弧气保焊
    __tablename__ = 'melting_polar_arc_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255), nullable=False,comment='接头形式')
    joint_clearance = Column(Float,comment='接头间隙  单位mm')
    groove_type = Column(VARCHAR(255),comment='坡口类型')
    groove_deep = Column(Float,comment='坡口深度（深度为+ 钝边为-）  单位mm')
    weld_position = Column(VARCHAR(255), nullable=False,comment='焊接位置')
    power_polarity = Column(VARCHAR(255),comment='电源极性')
    current = Column(Float,comment='焊接电流  单位A')
    wire_feed_speed = Column(Float, nullable=False,comment='送丝速度  单位m/min')
    voltage = Column(Float, nullable=False,comment='电弧电压  单位V')
    arc_length = Column(Float,comment='弧长  单位mm')
    arc_length_correction = Column(Float,comment='弧长修正  单位%')
    weld_speed = Column(Float, nullable=False,comment='焊接速度  单位cm/min')
    wire_material = Column(VARCHAR(255), nullable=False,comment='焊丝材料')
    wire_model = Column(VARCHAR(255), nullable=False,comment='焊丝牌号')
    wire_diameter = Column(Float, nullable=False,comment='焊丝直径  单位mm')
    wire_extension_length = Column(Float, nullable=False,comment='焊丝干伸长  单位mm')
    torch_angle = Column(VARCHAR(255),comment='焊枪角度')
    weave_type = Column(VARCHAR(255),comment='摆动（焊）类型')
    weave_range = Column(Float,comment='摆幅  单位mm')
    weave_length = Column(Float,comment='摆长  单位mm')
    weave_frequency = Column(Float,comment='摆动频率  单位Hz')
    shield_gas_type = Column(VARCHAR(255), nullable=False,comment='保护气类型')
    shield_gas_flow = Column(Float, nullable=False,comment='保护气流量  单位L/min')
    gas_purity = Column(Float,comment='气体纯度  单位%')
    pulse_peak_current = Column(Float,comment='脉冲峰值电流  单位A')
    pulse_base_current = Column(Float,comment='脉冲基值电流  单位A')
    pulse_frequency = Column(Float,comment='脉冲频率  单位Hz')
    duty_cycle = Column(Float,comment='占空比')
    weld_machine = Column(VARCHAR(255),comment='焊机品牌')
    robot = Column(VARCHAR(255),comment='机器人品牌')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class NonMeltingPolarArcWeld(Base):#非熔化极电弧气保焊
    __tablename__ = 'non_melting_polar_arc_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255),comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255),comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255),comment='接头形式')
    joint_clearance = Column(Float,comment='接头间隙  单位mm')
    groove_type = Column(VARCHAR(255),comment='坡口类型')
    groove_deep = Column(Float,comment='坡口深度（深度为+ 钝边为-）  单位mm')
    weld_position = Column(VARCHAR(255), nullable=False,comment='焊接位置')
    current = Column(Float, nullable=False,comment='焊接电流  单位A')
    power_polarity = Column(VARCHAR(255),comment='电源极性')
    weld_speed = Column(Float, nullable=False,comment='焊接速度  单位cm/min')
    voltage = Column(Float, nullable=False,comment='电弧电压  单位V')
    arc_length = Column(Float,comment='弧长  单位mm')
    wire_feed_speed = Column(Float,comment='送丝速度  单位m/min')
    wire_material = Column(VARCHAR(255),comment='焊丝材料')
    wire_model = Column(VARCHAR(255),comment='焊丝牌号')
    wire_diameter = Column(Float,comment='焊丝直径  单位mm')
    wire_feed_angle = Column(VARCHAR(255),comment='送丝角度')
    wire_feed_type = Column(VARCHAR(255),comment='送丝类型（前送丝or后送丝）')
    weave_type = Column(VARCHAR(255),comment='摆动（焊）类型')
    weave_range = Column(Float,comment='摆幅  单位mm')
    weave_length = Column(Float,comment='摆长  单位mm')
    weave_frequency = Column(Float,comment='摆动频率  单位Hz')
    shield_gas_type = Column(VARCHAR(255), nullable=False,comment='保护气类型')
    shield_gas_flow = Column(Float, nullable=False,comment='保护气流量  单位L/min')
    plasma_gas_type = Column(VARCHAR(255),comment='离子气种类')
    plasma_gas_flow = Column(Float,comment='离子气流量  单位L/min')
    gas_purity = Column(Float,comment='气体纯度  单位%')
    pulse_peak_current = Column(Float,comment='脉冲峰值电流  单位A')
    pulse_base_current = Column(Float,comment='脉冲基值电流  单位A')
    pulse_frequency = Column(Float,comment='脉冲频率  单位Hz')
    duty_cycle = Column(Float,comment='占空比')
    tungsten_electrode_diameter = Column(Float, nullable=False,comment='钨极直径  单位mm')
    tungsten_top_angle = Column(VARCHAR(255), server_default=text("'30'"),comment='钨极尖端角度or形状')
    tungsten_electrode_extension = Column(Float,comment='钨极伸长（内缩）量 （TIG伸出为+ PAW内缩为-）  单位mm')
    plasma_nozzle_diameter = Column(Float,comment='等离子喷嘴直径  单位mm')
    weld_machine = Column(VARCHAR(255),comment='焊机品牌')
    robot = Column(VARCHAR(255),comment='机器人品牌')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class ProductInfo(Base):#产品信息
    __tablename__ = 'product_info'

    product_id = Column(VARCHAR(255), primary_key=True,comment='产品id=product_code+weld_number')
    product_name = Column(VARCHAR(255),comment='产品名称')
    product_code = Column(VARCHAR(255),comment='产品代码')
    industry = Column(VARCHAR(255),comment='所属行业')
    drawing_url = Column(VARCHAR(255),comment='图纸地址')
    weld_number = Column(VARCHAR(255),comment='焊缝编号')
    weld_position = Column(VARCHAR(255),comment='焊缝位置')
    joint_type = Column(VARCHAR(255),comment='接头形式')
    cross_section_type = Column(VARCHAR(255),comment='焊脚类型')
    length_of_weld = Column(Float,comment='焊缝长度  单位mm')
    welding_quality_grade = Column(VARCHAR(255),comment='焊接质量等级')
    welding_quality_grade_remark = Column(VARCHAR(255))
    weld_performance_level = Column(VARCHAR(255),comment='焊缝性能等级')
    weld_performance_level_remark = Column(VARCHAR(255))
    stress_grade = Column(VARCHAR(255),comment='应力等级')
    safety_grade = Column(VARCHAR(255),comment='安全性等级')
    imperfection_quality_level = Column(VARCHAR(255),comment='缺欠质量等级')
    imperfection_quality_level_remark = Column(VARCHAR(255))
    weld_inspection_level = Column(VARCHAR(255),comment='焊缝检查等级')
    weld_inspection_level_remark = Column(VARCHAR(255))
    volumetric_test = Column(VARCHAR(255),comment='内部试验RT or UT')
    surface_test = Column(VARCHAR(255),comment='表面试验MT or PT')
    visual_examination = Column(VARCHAR(255),comment='外观试验VT')
    weld_length_tolerance = Column(VARCHAR(255),comment='尺寸公差标准')
    weld_length_tolerance_remark = Column(VARCHAR(255))
    weld_shape_tolerance = Column(VARCHAR(255),comment='形位公差标准')
    weld_shape_tolerance_remark = Column(VARCHAR(255))
    weld_tolerance = Column(VARCHAR(255),comment='未标注焊接尺寸公差标准')
    weld_tolerance_remark = Column(VARCHAR(255))
    weld_method = Column(VARCHAR(255),comment='焊接方法编号')
    weld_order = Column(VARCHAR(255),comment='（焊缝）焊接顺序    焊接工序')


class RobotAttitude(Base):#机器人运动姿态
    __tablename__ = 'robot_attitude'

    work_id = Column(VARCHAR(255), primary_key=True,comment='工作id')
    h = Column(Float, nullable=False,comment='焊丝尖端与焊接起始点的高度')
    x = Column(Float, nullable=False,comment='焊丝尖端在三维空间的坐标x')
    y = Column(Float, nullable=False,comment='焊丝尖端在三维空间的坐标y')
    z = Column(Float, nullable=False,comment='焊丝尖端在三维空间的坐标z')
    x1 = Column(Float, nullable=False,comment='导电嘴尖端的三维空间坐标x1')
    y1 = Column(Float, nullable=False,comment='导电嘴尖端的三维空间坐标y1')
    z1 = Column(Float, nullable=False,comment='导电嘴尖端的三维空间坐标z1')
    a = Column(Float, nullable=False,comment='当前焊点的三维空间坐标X')
    b = Column(Float, nullable=False,comment='当前焊点的三维空间坐标Y')
    c = Column(Float, nullable=False,comment='当前焊点的三维空间坐标Z')
    a1 = Column(Float, nullable=False,comment='上一个焊点的三维空间坐标X1')
    b1 = Column(Float, nullable=False,comment='上一个焊点的三维空间坐标Y1')
    c1 = Column(Float, nullable=False,comment='上一个焊点的三维空间坐标Z1')
    remark = Column(VARCHAR(255))
    Image_url = Column(VARCHAR(255))


class SubmergeArcWeld(Base):#埋弧焊
    __tablename__ = 'submerge_arc_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255), nullable=False,comment='接头形式')
    joint_clearance = Column(Float,comment='接头间隙  单位mm')
    groove_type = Column(VARCHAR(255),comment='坡口类型')
    groove_deep = Column(Float,comment='坡口深度（深度为+ 钝边为-）  单位mm')
    weld_position = Column(VARCHAR(255), nullable=False,comment='焊接位置')
    weld_speed = Column(Float, nullable=False,comment='焊接速度  单位cm/min')
    power_polarity = Column(VARCHAR(255),comment='电源极性')
    current = Column(Float,comment='焊接电流  单位A')
    wire_feed_speed = Column(Float,comment='送丝速度  单位m/min')
    voltage = Column(Float, nullable=False,comment='电压  单位V')
    flux_material = Column(VARCHAR(255),comment='焊剂材料')
    flux_model = Column(VARCHAR(255),comment='焊剂牌号')
    wire_material = Column(VARCHAR(255),comment='焊丝材料')
    wire_model = Column(VARCHAR(255),comment='焊丝牌号')
    wire_diameter = Column(Float, nullable=False,comment='焊丝直径  单位mm')
    wire_feed_angle = Column(VARCHAR(255),comment='送丝角度')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class VacuumElectronBeamWeld(Base):#真空电子束焊
    __tablename__ = 'vacuum_electron_beam_weld'

    weld_method = Column(VARCHAR(255), primary_key=True,comment='焊接方法编号')
    workpiece_id_a = Column(VARCHAR(255), nullable=False,comment='a侧焊接工件')
    workpiece_id_b = Column(VARCHAR(255), nullable=False,comment='b侧焊接工件')
    joint_form = Column(VARCHAR(255), nullable=False,comment='接头形式')
    joint_clearance = Column(Float,comment='接头间隙  单位mm')
    groove_type = Column(VARCHAR(255),comment='坡口类型')
    groove_deep = Column(Float,comment='坡口深度（深度为+ 钝边为-）  单位mm')
    weld_position = Column(VARCHAR(255), nullable=False,comment='焊接位置')
    weld_speed = Column(Float, nullable=False,comment='焊接速度  单位cm/min')
    acceleration_voltage = Column(Float, nullable=False,comment='加速电压  单位V')
    electron_beam_flow = Column(Float, nullable=False,comment='电子束电流  单位A')
    focus_current = Column(Float, nullable=False,comment='聚焦电流（确定焦点位置）  单位A')
    work_distance = Column(Float, nullable=False,comment='工作距离（焊件与电子束枪距离）  单位mm')
    vacuum_degree = Column(Float,comment='真空度  单位%')
    wire_feed_speed = Column(Float,comment='送丝速度  单位m/min')
    wire_material = Column(VARCHAR(255),comment='焊丝材料')
    wire_model = Column(VARCHAR(255),comment='焊丝牌号')
    wire_diameter = Column(Float,comment='焊丝直径  单位mm')
    wire_feed_type = Column(VARCHAR(255),comment='送丝类型（前送丝or后送丝）')
    wire_feed_angle = Column(VARCHAR(255),comment='送丝角度')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))


class WorkpieceInfo(Base):#工件信息
    __tablename__ = 'workpiece_info'

    workpiece_id = Column(VARCHAR(255), primary_key=True,comment='工件id')
    material = Column(VARCHAR(255), nullable=False,comment='材料种类')
    material_brand = Column(VARCHAR(255), nullable=False,comment='材料牌号')
    shape = Column(VARCHAR(255), nullable=False,comment='工件形状')
    thickness = Column(Float,comment='工件厚度  单位mm')
    diameter = Column(Float,comment='工件直径（外径）  单位mm')
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))

class AbbreviateCompare(Base):#焊接方法英文缩写中文对照表
    __tablename__ = 'abbreviate_compare'

    id = Column(INTEGER(), primary_key=True,autoincrement=True)
    method_abbreviate = Column(VARCHAR(255),comment='焊接方法英文缩写')
    method_chinese_name = Column(VARCHAR(255),comment='焊接方法对应中文名称')
    table_abbreviate = Column(VARCHAR(255),comment='焊接方法所属表英文')
    table_chinese_name = Column(VARCHAR(255),comment='表名对应中文名称')


Base.metadata.create_all(engine)   #创建以上类对应的数据表结构，若已存在，则忽略


Session = sessionmaker(engine)     #创建与数据库的会话Session,注意,这里返回给session的是个class,不是实例
session = Session()                #生成Session实例，相当于游标
session.commit()                   #统一提交会话，执行操作