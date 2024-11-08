import RPi.GPIO as GPIO
from inputs import get_gamepad
import threading

class Motores:
    def __init__(self) -> None:
        self.motor1 = 36  # Entrada
        self.motor2 = 38    # Entrada
        self.motor3 = 40   # Habilitar
        
        self.motor4 = 26  # Entrada
        self.motor5 = 24    # Entrada
        self.motor6 = 22   # Habilitar

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

    def go_right(self) -> None:
        # Activar motores para moverse hacia adelante
        GPIO.output(self.motor1, GPIO.HIGH)
        GPIO.output(self.motor2, GPIO.LOW)
        GPIO.output(self.motor3, GPIO.HIGH)
        
        GPIO.output(self.motor4, GPIO.LOW)
        GPIO.output(self.motor5, GPIO.LOW)
        GPIO.output(self.motor6, GPIO.LOW)

    def go_left(self) -> None:
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

def controlar_motores():
    motores = Motores()
    
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == 'Key' and event.code == 'BTN_SOUTH' and event.state == 1:  # Botón A
                motores.adelante()
            elif event.ev_type == 'Key' and event.code == 'BTN_EAST' and event.state == 1:  # Botón B
                motores.atras()
            elif event.ev_type == 'Key' and event.code == 'BTN_NORTH' and event.state == 1:  # Botón X
                motores.go_left()
            elif event.ev_type == 'Key' and event.code == 'BTN_WEST' and event.state == 1:  # Botón Y
                motores.go_right()
            elif event.ev_type == 'Key' and event.code == 'BTN_MODE' and event.state == 1:  # Botón central
                motores.detener()

if __name__ == '__main__':
    thread = threading.Thread(target=controlar_motores)
    thread.start()