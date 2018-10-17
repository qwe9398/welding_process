 # coding: utf-8
from sqlalchemy import create_engine

#连接本地welding_process库
engine = create_engine("mysql+pymysql://root:123456@localhost/welding_process?charset=utf8")


#简单的sql语句查询
result = engine.execute("select * from workpiece_info")

for i in result.fetchall():
    print(i,end="\n")

result = engine.execute("select * from workpiece_info")
print(result.fetchall())

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Float,VARCHAR,INTEGER

Base = declarative_base()

class WorkpieceInfo(Base):

    __tablename__ = 'workpiece_info'#表名称

    workpiece_id = Column(VARCHAR(255), primary_key=True) #字段的名称和定义
    material = Column(VARCHAR(255), nullable=False)
    material_brand = Column(VARCHAR(255), nullable=False)
    shape = Column(VARCHAR(255), nullable=False)
    thickness = Column(Float)
    diameter = Column(Float)
    remark = Column(VARCHAR(255))
    image_url = Column(VARCHAR(255))

    def __repr__(self):   #sqlalchemy把返回的数据映射成一个对象,下面定义函数可直接将具体字段内容变为可读
        return "<WorkpieceInfo(workpiece_id='%s',  material='%s', material_brand='%s',shape='%s',thickness='%s'" \
               ",diameter='%s',remark='%s',image_url='%s')>" % \
               (self.workpiece_id, self.material,self.material_brand,self.shape,self.thickness,self.diameter,self.remark,self.image_url)


from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_     #查询条件可使用与或条件

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = sessionmaker(engine)  # 实例和engine绑定
mySession = session()           # 生成session实例，相当于游标

##############查询数据库数据#####################
Result1 = mySession.query(WorkpieceInfo).all()     #查询
print(Result1[0])                                       #sqlalchemy把返回的数据映射成一个对象
#未定义def __repr__(self)之前结果为<__main__.WorkpieceInfo object at 0x000001C62B16CE48> 是一个对象，不能直接读出字段具体内容，但可以单独调用字段(对象)属性
#定义def __repr__(self)之后的输出结果为
 # <WorkpieceInfo(workpiece_id='G00001_12',  material='Dual_phase_steel', material_brand='2205',shape='板',thickness='12.0',diameter='None',remark='DTIG',image_url='')>
print(Result1[1].workpiece_id)                          #调用每个字段就可以跟调用对象属性一样
#结果为G00001_4
for i in range(5):                   #通过for循环输出所有Result1中的数据，列表
   print(Result1[i])                 #输出Result1中前5组数据

Result2 = mySession.query(WorkpieceInfo).filter(WorkpieceInfo.thickness==9).first()#查询 filter后接条件，必须接类名称
print(Result2.workpiece_id,Result2.material,Result2.shape)                 #调用每个字段就可以跟调用对象属性一样

Result3 = mySession.query(WorkpieceInfo).filter_by(thickness=9).first()     #filter_by用法  可不接类名称
print(Result3.workpiece_id)

Result4 = mySession.query(WorkpieceInfo).filter_by(material="Mg_alloy").all()
for n in Result4:         #for循环遍历Result4中查询到的数据列表
    print(n)



##################################对数据库中的表的数据进行处理修改#####################################
class AbbreviateCompare(Base):
    __tablename__ = 'abbreviate_compare'

    id = Column(INTEGER(), primary_key=True,autoincrement=True)
    method_abbreviate = Column(VARCHAR(255))
    method_chinese_name = Column(VARCHAR(255))
    table_abbreviate = Column(VARCHAR(255))
    table_chinese_name = Column(VARCHAR(255))

    def __init__(self,id,method_abbreviate,method_chinese_name,table_abbreviate,table_chinese_name):
        self.id = id
        self.method_abbreviate = method_abbreviate
        self.method_chinese_name = method_chinese_name
        self.table_abbreviate = table_abbreviate
        self.table_chinese_name = table_chinese_name

Session1 = sessionmaker(bind=engine)
session1 = Session1()
Result5 =session1.query(AbbreviateCompare).filter().all()  #导出表中所有数据
for x in Result5:   #通过for循环，逐条删除method_abbreviate这一列数据中字符串的末尾的空格，再重新修改数据库中的数据
    print(x.method_abbreviate)     #原始数据
    y = x.method_abbreviate.rstrip()      #删除末尾空格，重新赋值新数据
    print(y)                              #修改之后的数据
    session1.query(AbbreviateCompare).filter(AbbreviateCompare.method_abbreviate==x.method_abbreviate).update({"method_abbreviate":y})
    #将修改后的数据y重新对表中数据进行修改——将y的字符串分别赋值到表method_abbreviate这一列对应的数据
    #session1.commit()             # 会话提交，执行数据库操作




