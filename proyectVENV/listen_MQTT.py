import time
from post_to_mysql import *
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    topic = msg.topic 
    msg = msg.payload.decode()
    topic = topic.split("/")[1]

    if topic == "ADC":
        read_and_send_ADC(msg)
        print("Data sent to db, ADC")
    elif topic == "Acelerometro":
        read_and_send_Acelerometro(msg)
        print("Data sent to db, Ace")
    elif topic == "Distancia":
        read_and_send_Distancia(msg)
        print("Data sent to db, Dist")
    elif topic == "BME":
        read_and_send_BME(msg)
        print("Data sent to db, BME")
    else:
        print("Data error")
    

unacked_publish = set()
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqtt_client.on_message = on_message

mqtt_client.connect("broker.hivemq.com", 1883)
mqtt_client.loop_start()
mqtt_client.subscribe("SensoresIoT/ADC")
mqtt_client.subscribe("SensoresIoT/Acelerometro")
mqtt_client.subscribe("SensoresIoT/Distancia")
mqtt_client.subscribe("SensoresIoT/BME")

try:
    print("Esperando mensajes")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Proceso interrumpido por el usuario")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()