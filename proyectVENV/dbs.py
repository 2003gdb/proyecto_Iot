from sqlalchemy import create_engine, Column, Integer, String, DateTime, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASEURL = "mysql+pymysql://root:carlos10@localhost/sensoresIot"

engine = create_engine(DATABASEURL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)
Base = declarative_base()

class SensorAcelerometro(Base):
    __tablename__ = "sensorAcelerometro"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    x_cor = Column(Double)
    y_cor = Column(Double)
    z_cor = Column(Double)

class SensorADC(Base):
    __tablename__ = "sensorADC"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    voltaje = Column(Double)
    valor_analogico = Column(Integer)

class SensorBME(Base):
    __tablename__ = "sensorBME"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    temp = Column(Double)
    presion = Column(Double)
    altitud = Column(Double)

class SensorDistancia(Base):
    __tablename__ = "sensorDistancia"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    dist_cm = Column(Double)

