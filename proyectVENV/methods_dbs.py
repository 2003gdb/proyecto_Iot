# Metodos de la FastAPI
# Interactuar con la base de datos 
# Movimiento del carrito

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from dbs import SessionLocal, SensorADC, SensorDistancia, SensorAcelerometro, SensorBME
from carrito.send_data import send_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Instruccion(BaseModel):
    comando: str 

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
def get_datos_sensorADC(
    fecha_inicio: Optional[str] = None,
    fecha_fin: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(SensorADC)
    if fecha_inicio:
        query = query.filter(SensorADC.fecha >= fecha_inicio)
    if fecha_fin:
        query = query.filter(SensorADC.fecha <= fecha_fin)
    return query.all()

@app.get("/get_sensorAcelerometro")
def get_datos_sensorAcelerometro(
    fecha_inicio: Optional[str] = None,
    fecha_fin: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(SensorAcelerometro)
    if fecha_inicio:
        query = query.filter(SensorAcelerometro.fecha >= fecha_inicio)
    if fecha_fin:
        query = query.filter(SensorAcelerometro.fecha <= fecha_fin)
    return query.all()

@app.get("/get_sensorBME")
def get_datos_sensorBME(
    fecha_inicio: Optional[str] = None,
    fecha_fin: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(SensorBME)
    if fecha_inicio:
        query = query.filter(SensorBME.fecha >= fecha_inicio)
    if fecha_fin:
        query = query.filter(SensorBME.fecha <= fecha_fin)
    return query.all()

@app.get("/get_sensorDistancia")
def get_datos_sensorDistancia(
    fecha_inicio: Optional[str] = None,
    fecha_fin: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(SensorDistancia)
    if fecha_inicio:
        query = query.filter(SensorDistancia.fecha >= fecha_inicio)
    if fecha_fin:
        query = query.filter(SensorDistancia.fecha <= fecha_fin)
    return query.all()

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

@app.post("/Movimiento")
async def Mover_carrito(instruccion: Instruccion):
    comando = instruccion.comando
    print(comando, ",(methods_dbs)")
    if comando not in ["w", "a", "s", "d", "stop"]:
        return {"status": "Instrucción no válida", "comando": comando}
    # Send_data se encuentra dentro de la carpeta carrito
    send_data(comando, "ControlCarrito")
    return {"status": "Movimiento ejecutado", "comando": comando}





