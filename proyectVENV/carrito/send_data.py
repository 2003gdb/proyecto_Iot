import paho.mqtt.client as mqtt
import time

def on_publish(client, userdata, mid, reason_code, properties):
    try:
        userdata.remove(mid)
    except KeyError:
        print("No hay conexión")
        
# Envia los Datos en Json a un Topic "SensoresIoT/<sensor>"
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
    print("Espera publicando mensaje,(Send_data)")
    while len(unacked_publish):
        time.sleep(0.1)

    # En espera de la conexion y publicación segura
    msg_info.wait_for_publish()
    mqttc.disconnect()
    mqttc.loop_stop()
    print("sent,(Send_data)")