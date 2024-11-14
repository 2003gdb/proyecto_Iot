# Sistema de Control de Motores para Carrito

## Descripción
Este programa en Python permite controlar los motores de un carrito mediante 
una Raspberry Pi y la biblioteca GPIO.
El control se realiza mediante entradas de teclado para avanzar, retroceder, 
girar a la izquierda, girar a la derecha o detener el carrito.

## Requisitos
El programa utiliza las siguientes bibliotecas:
- `RPi.GPIO`: Para controlar los pines GPIO y manipular los motores.
- `keyboard`: Para capturar las entradas del teclado.
- `publish_MQTT`: Módulo para enviar comandos de control remoto vía MQTT 
(se asume que contiene la función `send_data`).

## Conexión de Hardware
Conecta los motores del carrito a la Raspberry Pi de la siguiente manera:
- **Rueda Derecha**: Pines GPIO 36, 38, y 40.
- **Rueda Izquierda**: Pines GPIO 29, 31, y 33.

## Instrucciones de Uso
1. **Ejecuta el programa**:
   ```bash
   sudo python <nombre_programa>.py
   ```
   Usa las siguientes teclas para controlar el carrito:
   - **w**: Adelante
   - **s**: Atrás
   - **a**: Izquierda
   - **d**: Derecha
   - **space**: Detener

2. **Modos de Control**:
   - **Control Local**: Utiliza `controlar_motores_local()` para manipular 
los motores directamente desde el teclado.
   - **Control Remoto**: Utiliza `controlar_motores_remoto()` para enviar comandos MQTT al carrito.

## Descripción de Funciones
- **Motores**:
  - `adelante()`: Activa los motores para avanzar.
  - `atras()`: Activa los motores para retroceder.
  - `turn_left()`: Gira el carrito hacia la izquierda.
  - `turn_right()`: Gira el carrito hacia la derecha.
  - `detener()`: Detiene todos los motores.
- **controlar_motores_local()**: Controla los motores localmente usando las teclas `w`, `s`, `a`, `d` y `space`.
- **controlar_motores_remoto()**: Envía comandos MQTT para controlar los motores remotamente.
