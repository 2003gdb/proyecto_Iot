import time
import paho.mqtt.client as mqtt
from motores import *

def on_message(client, userdata, msg):
    topic = msg.topic 
    msg = msg.payload.decode()
    topic = topic.split("/")[1]
    print(msg)
    
    if topic == "ControlCarrito":
        controlar_motores(msg)
        print("Data sent to function controlar carrito", msg)
    else:
        print("Data error")
    
    print("Volviendo a esperar mensajes")
    

unacked_publish = set()
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqtt_client.on_message = on_message

mqtt_client.connect("broker.hivemq.com", 1883)
mqtt_client.loop_start()
mqtt_client.subscribe("SensoresIoT/ControlCarrito")

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
