# coding=utf-8
from sqlalchemy import create_engine,Column,VARCHAR,Float,text,INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


sqlusername = 'root'
sqlpassword = '123456'
sqlport = '3306'
sqldatabase = 'welding_process'
url = 'mysql+pymysql://{}:{}@localhost:{}/{}?charset=utf8'.format(sqlusername,sqlpassword,sqlport,sqldatabase)

engine = create_engine(url,encoding='utf-8',echo=True)
Base = declarative_base(bind=engine)

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


