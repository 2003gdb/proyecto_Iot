import paho.mqtt.client as mqtt
import time
# import board
# import busio
# import adafruit_ads1x15.ads1115 as ADS
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_adxl34x
# import adafruit_bmp280
# import RPi.GPIO as GPIO #BIBLIOTECAS PARA SENSOR DISTANCIA

# Inicializar los sensores
# i2c = busio.I2C(board.SCL, board.SDA)
# adc = ADS.ADS1115(i2c)
# adc_channel = AnalogIn(adc, ADS.P0)
# acelerometro = adafruit_adxl34x.ADXL345(i2c)
# bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)
# bmp280.sea_level_pressure = 1013.25    

def main():
    # Ciclo principal
    while True:

        send_data("{hola:world}", "ADC")
        # send_data(json_ADC(), "ADC")
        time.sleep(2)

        # send_data(json_Acelerometro(), "Acelerometro")
        # time.sleep(3)

        # send_data(json_BME(), "BME")
        # time.sleep(3)

        # send_data(json_Distancia(), "Distancia")
        # time.sleep(3)

def send_data(json, sensor):
    #Establecer conexion
    unacked_publish = set()
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_publish = on_publish
    mqttc.user_data_set(unacked_publish)

    mqttc.connect("broker.hivemq.com", 1883)
    mqttc.loop_start()
    msg_info = mqttc.publish(f"SensoresIoT/{sensor}", json, qos=2)
    unacked_publish.add(msg_info.mid)

    # Espera publicando mensaje
    while len(unacked_publish):
        time.sleep(0.1)

    # En espera de la conexion y publicación segura
    msg_info.wait_for_publish()
    mqttc.disconnect()
    mqttc.loop_stop()
    
# Funciones para cada sensor
# def json_ADC():
#     valor_analogico = adc_channel.value
#     voltaje = adc_channel.voltage
#     json_ADC = {
#         "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
#         "voltaje": voltaje,
#         "valor_analogico": valor_analogico
#     }
#     return json_ADC

# def json_Acelerometro():
#     x, y, z = acelerometro.acceleration
#     json_Acelerometro = {
#         "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
#         "x_cor": x,
#         "y_cor": y,
#         "z_cor": z
#     }
#     return json_Acelerometro

# def json_BME():
#     temperatura = bmp280.temperature
#     presion = bmp280.pressure
#     altitud = bmp280.altitude
#     json_BME = {
#         "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
#         "temp": temperatura,
#         "presion": presion,
#         "altitud": altitud
#     }
#     return json_BME

# def json_Distancia():
#     dist = medir_distancia()
#     json_Distancia = {
#         "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
#         "dist_cm": dist
#     }
#     return json_Distancia

# def medir_distancia(): 
#     GPIO.setmode(GPIO.BCM)

#     TRIG = 23
#     ECHO = 24
#     print("medición en progreso")
#     GPIO.setup(TRIG,GPIO.OUT)
#     GPIO.setup(ECHO,GPIO.IN)

#     GPIO.output(TRIG,False)
#     print("esperando datos")
#     time.sleep(2)

#     GPIO.output(TRIG,True)
#     time.sleep(0.00001)
#     GPIO.output(TRIG,False)

#     while GPIO.input(ECHO)==0:
#         pulse_start=time.time()
        
#     while GPIO.input(ECHO)==1:
#         pulse_end=time.time()
        
#     pulso_dura=pulse_end - pulse_start

#     dist = pulso_dura * 17150
#     dist= round (dist, 2)
#     return dist

def on_publish(client, userdata, mid, reason_code, properties):
    try:
        userdata.remove(mid)
    except KeyError:
        print("No hay conexión")

main()
