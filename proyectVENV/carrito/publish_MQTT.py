import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_adxl34x
import adafruit_bmp280
import RPi.GPIO as GPIO #BIBLIOTECAS PARA SENSOR DISTANCIA 

from send_data import send_data

# Biblioteca controlar motores
import threading
import motores

# Biblioteca para Manejar JSON
import json

def main():
    # MENU de control de carrito
    print("\nMENU\n")
    print("1. Enviar Datos Sensores")
    print("2. Controlar Carrito Local")
    print("3. Controlar Carrito Remoto")
    opcion = input("\n::: ")

    # Envia datos de sensores
    if opcion == "1":
        # Inicializar los sensores
        global i2c
        global adc
        global adc_channel
        global acelerometro
        global bmp280

        i2c = busio.I2C(board.SCL, board.SDA)
        adc = ADS.ADS1115(i2c)
        adc_channel = AnalogIn(adc, ADS.P0)
        acelerometro = adafruit_adxl34x.ADXL345(i2c)
        bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
        bmp280.sea_level_pressure = 1013.25   

        # Ciclo principal
        while True:
            json_ADC_data = json.dumps(json_ADC())
            send_data(json_ADC_data, "ADC")
            time.sleep(2)

            json_Acelerometro_data = json.dumps(json_Acelerometro())
            send_data(json_Acelerometro_data, "Acelerometro")
            time.sleep(3)

            json_BME_data = json.dumps(json_BME())
            send_data(json_BME_data, "BME")
            time.sleep(3)

            json_Distancia_data = json.dumps(json_Distancia())
            send_data(json_Distancia_data, "Distancia")
            time.sleep(3)

    # Controlar Motores localmente
    elif opcion == "2":
        thread = threading.Thread(target=motores.controlar_motores_local)
        thread.start()
    
    # Controlar Motores Remotamente
    elif opcion == "3":
        thread = threading.Thread(target=motores.controlar_motores_remoto)
        thread.start()

# Obtener Datos del sensores y regresamos un json
def json_ADC():
    valor_analogico = adc_channel.value
    voltaje = adc_channel.voltage
    json_ADC = {
        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
        "voltaje": voltaje,
        "valor_analogico": valor_analogico
    }
    return json_ADC

def json_Acelerometro():
    x, y, z = acelerometro.acceleration
    json_Acelerometro = {
        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
        "x_cor": x,
        "y_cor": y,
        "z_cor": z
    }
    return json_Acelerometro

def json_BME():
    temperatura = bmp280.temperature
    presion = bmp280.pressure
    altitud = bmp280.altitude
    json_BME = {
        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
        "temp": temperatura,
        "presion": presion,
        "altitud": altitud
    }
    return json_BME

def json_Distancia():
    dist = medir_distancia()
    json_Distancia = {
        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
        "dist_cm": dist
    }
    return json_Distancia

# Setup para medir distancia
def medir_distancia(): 
    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24
    print("medición en progreso")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG,False)
    print("esperando datos")
    time.sleep(2)

    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
        
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
        
    pulso_dura=pulse_end - pulse_start

    dist = pulso_dura * 17150
    dist= round (dist, 2)
    return dist

main()
