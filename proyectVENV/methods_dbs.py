from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from dbs import SessionLocal, SensorADC, SensorDistancia, SensorAcelerometro, SensorBME

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class sensorADC_DTO(BaseModel):
    fecha: str
    voltaje: float
    valor_analogico: int

class sensorAcelerometro_DTO(BaseModel):
    fecha: str
    x_cor: float
    y_cor: float
    z_cor: float

class sensorBME_DTO(BaseModel):
    fecha: str
    temp: float
    presion: float
    altitud: float

class sensorDistancia_DTO(BaseModel):
    fecha: str
    dist_cm: float

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.delete("/delete_all_data")
async def delete_all_data(db: Session = Depends(get_db)):
    db.query(SensorADC).delete()
    db.query(SensorDistancia).delete()
    db.query(SensorAcelerometro).delete()
    db.query(SensorBME).delete()
    db.commit()
    return {"message": "All data deleted"}

@app.get("/get_sensorADC")
def get_datos_sensorADC(db: Session = Depends(get_db)):
    return db.query(SensorADC).all()

@app.get("/get_sensorAcelerometro")
def get_datos_sensorAcelerometro(db: Session = Depends(get_db)):
    return db.query(SensorAcelerometro).all()

@app.get("/get_sensorBME")
def get_datos_sensorBME(db: Session = Depends(get_db)):
    return db.query(SensorBME).all()

@app.get("/get_sensorDistancia")
def get_datos_sensorDistancia(db: Session = Depends(get_db)):
    return db.query(SensorDistancia).all()

@app.post("/post_sensorADC")
async def add_dato_sensorADC(sensor: sensorADC_DTO, db: Session = Depends(get_db)):
    sensor_data = SensorADC(fecha=sensor.fecha, voltaje=sensor.voltaje, valor_analogico=sensor.valor_analogico)
    db.add(sensor_data)
    db.commit()
    db.refresh(sensor_data)
    return sensor_data

@app.post("/post_sensorAcelerometro")
async def add_dato_sensorAcelerometro(sensor: sensorAcelerometro_DTO, db: Session = Depends(get_db)):
    sensor_data = SensorAcelerometro(fecha=sensor.fecha, x_cor=sensor.x_cor, y_cor=sensor.y_cor, z_cor=sensor.z_cor)
    db.add(sensor_data)
    db.commit()
    db.refresh(sensor_data)
    return sensor_data

@app.post("/post_sensorBME")
async def add_dato_sensorBME(sensor: sensorBME_DTO, db: Session = Depends(get_db)):
    sensor_data = SensorBME(fecha=sensor.fecha, temp=sensor.temp, presion=sensor.presion, altitud=sensor.altitud)
    db.add(sensor_data)
    db.commit()
    db.refresh(sensor_data)
    return sensor_data

@app.post("/post_sensorDistancia")
async def add_dato_sensorDistancia(sensor: sensorDistancia_DTO, db: Session = Depends(get_db)):
    sensor_data = SensorDistancia(fecha=sensor.fecha, dist_cm=sensor.dist_cm)
    db.add(sensor_data)
    db.commit()
    db.refresh(sensor_data)
    return sensor_data

@app.get("/find_by_fecha_sensorADC/{fecha}")
async def find_by_fecha_sensorADC(fecha: str, db: Session = Depends(get_db)):
    return db.query(SensorADC).filter(SensorADC.fecha == fecha).first()

@app.get("/find_by_fecha_sensorAcelerometro/{fecha}")
async def find_by_fecha_sensorAcelerometro(fecha: str, db: Session = Depends(get_db)):
    return db.query(SensorAcelerometro).filter(SensorAcelerometro.fecha == fecha).first()

@app.get("/find_by_fecha_sensorBME/{fecha}")
async def find_by_fecha_sensorBME(fecha: str, db: Session = Depends(get_db)):
    return db.query(SensorBME).filter(SensorBME.fecha == fecha).first()

@app.get("/find_by_fecha_sensorDistancia/{fecha}")
async def find_by_fecha_sensorDistancia(fecha: str, db: Session = Depends(get_db)):
    return db.query(SensorDistancia).filter(SensorDistancia.fecha == fecha).first()
