import time
from post_to_mysql import *
from database_manager import DatabaseManager
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    msg = msg.payload.decode()
    topic = msg.topic()
    print(topic, msg)
    # msg_split = msg.split("_")
    # sensor = msg_split[0]
    # valor = msg_split[1]
    # db_manager.insert_value(valor)
    print(f"\nEl sensor es: {topic} valor: {msg}")

unacked_publish = set()
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqtt_client.on_message = on_message

mqtt_client.connect("broker.hivemq.com",1883)
mqtt_client.loop_start()
mqtt_client.subscribe("SensoresIoT/ADC")
mqtt_client.subscribe("SensoresIoT/Acelerometro")
mqtt_client.subscribe("SensoresIoT/Distancia")
mqtt_client.subscribe("SensoresIoT/BME")

try:
    print("Esperando mensajes")
    while True:
        time.sleep(1)
except:
    print(f"Ocurrio un error")
finally:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()