import RPi.GPIO as GPIO
import keyboard
from publish_MQTT import send_data


class Motores:
    def __init__(self) -> None:
        #right wheel
        self.motor1 = 36  # Entrada
        self.motor2 = 38    # Entrada
        self.motor3 = 40   # Habilitar
        
        #left wheel
        self.motor4 = 29  # Entrada
        self.motor5 = 31    # Entrada
        self.motor6 = 33   # Habilitar

        self.configurar_motores()
        self.detener()

    def configurar_motores(self) -> None:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motor1, GPIO.OUT)
        GPIO.setup(self.motor2, GPIO.OUT)
        GPIO.setup(self.motor3, GPIO.OUT)
        GPIO.setup(self.motor4, GPIO.OUT)
        GPIO.setup(self.motor5, GPIO.OUT)
        GPIO.setup(self.motor6, GPIO.OUT)

    def detener(self) -> None:
        #configura los motores en estado apagado
        GPIO.output(self.motor1, GPIO.LOW)
        GPIO.output(self.motor2, GPIO.LOW)
        GPIO.output(self.motor3, GPIO.LOW)
        GPIO.output(self.motor4, GPIO.LOW)
        GPIO.output(self.motor5, GPIO.LOW)
        GPIO.output(self.motor6, GPIO.LOW)
    
    def adelante(self) -> None:
        # Activar motores para moverse hacia adelante
        GPIO.output(self.motor1, GPIO.HIGH)
        GPIO.output(self.motor2, GPIO.LOW)
        GPIO.output(self.motor3, GPIO.HIGH)
        
        GPIO.output(self.motor4, GPIO.HIGH)
        GPIO.output(self.motor5, GPIO.LOW)
        GPIO.output(self.motor6, GPIO.HIGH)
    
    def atras(self) -> None:
        # Activar motores para moverse hacia adelante
        GPIO.output(self.motor1, GPIO.LOW)
        GPIO.output(self.motor2, GPIO.HIGH)
        GPIO.output(self.motor3, GPIO.HIGH)
        
        GPIO.output(self.motor4, GPIO.LOW)
        GPIO.output(self.motor5, GPIO.HIGH)
        GPIO.output(self.motor6, GPIO.HIGH)

    def turn_left(self) -> None:
        # Activar motores para moverse hacia adelante
        GPIO.output(self.motor1, GPIO.HIGH)
        GPIO.output(self.motor2, GPIO.LOW)
        GPIO.output(self.motor3, GPIO.HIGH)
        
        GPIO.output(self.motor4, GPIO.LOW)
        GPIO.output(self.motor5, GPIO.LOW)
        GPIO.output(self.motor6, GPIO.LOW)

    def turn_right(self) -> None:
        # Activar motores para moverse hacia adelante
        GPIO.output(self.motor1, GPIO.LOW)
        GPIO.output(self.motor2, GPIO.LOW)
        GPIO.output(self.motor3, GPIO.LOW)
        
        GPIO.output(self.motor4, GPIO.HIGH)
        GPIO.output(self.motor5, GPIO.LOW)
        GPIO.output(self.motor6, GPIO.HIGH)

    def __del__(self):
        # Limpiar la configuración GPIO al eliminar la instancia
        GPIO.cleanup()

def controlar_motores_local():
    motores = Motores()

    while True:
        if keyboard.is_pressed('w'):  # Adelante
            motores.adelante()
        elif keyboard.is_pressed('s'):  # Atrás
            motores.atras()
        elif keyboard.is_pressed('a'):  # Izquierda
            motores.turn_left()
        elif keyboard.is_pressed('d'):  # Derecha
            motores.turn_right()
        elif keyboard.is_pressed('space'):  # Detener
            motores.detener()

def controlar_motores_remoto():

    while True:
        if keyboard.is_pressed('w'):  # Adelante
            send_data("adelante", "ControlCarrito")
        elif keyboard.is_pressed('s'):  # Atrás
            send_data("atras", "ControlCarrito")
        elif keyboard.is_pressed('a'):  # Izquierda
            send_data("left", "ControlCarrito")
        elif keyboard.is_pressed('d'):  # Derecha
            send_data("right", "ControlCarrito")
        elif keyboard.is_pressed('space'):  # Detener
            send_data("stop", "ControlCarrito")
