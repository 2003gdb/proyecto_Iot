
# Sistema de Monitoreo y Control de Carrito

## Descripción
Este programa en Python permite recolectar datos de múltiples sensores conectados a una Raspberry Pi 
y controlar un carrito motorizado. 

A través de un menú, el usuario puede:

1. Enviar datos de los sensores a un broker MQTT.
2. Controlar el carrito de forma local.
3. Controlar el carrito de forma remota.

## Requisitos
El programa utiliza las siguientes bibliotecas:
- `paho-mqtt`: Para conexión y publicación en MQTT.
- `board`, `busio`: Para habilitar la comunicación I2C.
- `adafruit_ads1x15`, `adafruit_adxl34x`, `adafruit_bmp280`: Bibliotecas de Adafruit para 
interactuar con los sensores ADC, acelerómetro y BMP280.
- `RPi.GPIO`: Para controlar los pines GPIO y medir distancia con el sensor ultrasónico.

- `threading`: Para controlar los motores en hilos separados.
- `motores`: Archivo de python con clase para controlar el carrito

## Conexión de Hardware
Conecta los siguientes sensores y motores a la Raspberry Pi:
1. **ADS1115 (ADC)**: Lee señales analógicas.
2. **ADXL345 (Acelerómetro)**: Mide la aceleración en los ejes x, y, z.
3. **BMP280 (Barómetro)**: Mide la temperatura, presión y altitud.
4. **Sensor ultrasónico (HC-SR04)**: Mide la distancia.
5. **Motores**: Controlados a través del módulo `motores`.

## Instrucciones de Uso
1. **Ejecuta el programa**:
   ```bash
   python publish_MQTT.py
   ```
   En el menú, selecciona una opción:
   - **1**: Enviar datos de los sensores al broker MQTT en el tópico `SensoresIoT/<nombre_sensor>`.
   - **2**: Controlar el carrito localmente usando los motores.
   - **3**: Controlar el carrito remotamente, enviando instrucciones a traves de MQTT.
   
2. **Publicación de Datos**:
   Los datos de cada sensor se publican en un tópico MQTT específico, con el prefijo `SensoresIoT/<nombre_sensor>`.

## Descripción de Funciones
- **main()**: Muestra el menú y ejecuta la opción seleccionada por el usuario.
- **send_data(json, sensor)**: Publica datos en formato JSON en el tópico MQTT correspondiente para cada sensor.
- **json_ADC()**: Lee el valor y voltaje del ADC y devuelve los datos en JSON.
- **json_Acelerometro()**: Lee la aceleración en los ejes x, y, z del acelerómetro y devuelve los datos en JSON.
- **json_BME()**: Lee temperatura, presión y altitud del BMP280 y devuelve los datos en JSON.
- **json_Distancia()**: Lee la distancia medida por el sensor ultrasónico y devuelve los datos en JSON.
- **medir_distancia()**: Calcula la distancia usando el sensor ultrasónico.
- **controlar_motores_local()** y **controlar_motores_remoto()**: Funciones en el módulo `motores` para controlar 
los motores local y remotamente.

## Ejemplo de Salida en JSON
Cada sensor incluye una marca de tiempo y sus lecturas relevantes:
```json
{
    "fecha": "YYYY-MM-DD HH:MM:SS",
    "voltaje": 3.3,
    "valor_analogico": 512
}
```
