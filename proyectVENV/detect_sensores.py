import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS #biblioteca del ADC
from adafruit_ads1x15.analog_in import AnalogIn #biblioteca del ADC
import adafruit_adxl34x #biblioteca del acelerómetro
import adafruit_bmp280 # biblioteca del BME280

from distancia import medir_distancia

i2c = busio.I2C(board.SCL, board.SDA)

adc = ADS.ADS1115(i2c)
adc_channel = AnalogIn(adc, ADS.P0)

acelerometro = adafruit_adxl34x.ADXL345(i2c)

# probar address con 0x76
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)
bmp280.sea_level_pressure = 1013.25

# Lectura continua
while True:
    #Sensor Distancia
    dist = medir_distancia()
    print("La distancia medida es:",dist,"cm")

    #Sensor ADC
    print("Valor analogico: ", adc_channel.value, "Volts: ", adc_channel.voltage)
    time.sleep(0.5)

    #Sensor Acelerometro
    print("%f %f %f"%acelerometro.acceleration)
    time.sleep(1)

    #Sensor BME280
    print("\nTemperatura: %0.1f C" % bmp280.temperature)
    print("Presioón: %0.1f hPa" % bmp280.pressure)
    print("Altitud = %0.2f metros" % bmp280.altitude)
    time.sleep(2)
