import requests

# URLs de los endpoints
url_ADC = "http://127.0.0.1:8000/post_sensorADC"
url_Acelerometro = "http://127.0.0.1:8000/post_sensorAcelerometro"
url_BME = "http://127.0.0.1:8000/post_sensorBME"
url_Distancia = "http://127.0.0.1:8000/post_sensorDistancia"

# Función para enviar datos al servidor
def to_db(url, data):
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Datos enviados exitosamente:", response.json())
        else:
            print("Error al enviar datos:", response.status_code, response.text)
    except Exception as e:
        print("Error enviando a db:", e)

# Funciones para cada sensor
def read_and_send_ADC(json_ADC):
    to_db(url_ADC, json_ADC)

def read_and_send_Acelerometro(json_Acelerometro):
    to_db(url_Acelerometro, json_Acelerometro)

def read_and_send_BME(json_BME):
    to_db(url_BME, json_BME)

def read_and_send_Distancia(json_Distancia):
    to_db(url_Distancia, json_Distancia)
