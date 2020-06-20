# Ayudantia Arduino: Comunicación Serial
# IDI1015 - Pensamiento Visual @ PUC
# Alonso Canales(aecanales@uc.cl)
#
# Ejemplo 1: Leer Arduino desde Python

# Importamos la libreria serial para poder comunicarnos con una placa Arduino.
import serial

# Creamos la conexión con la placa. Debemos tener en cuenta:
#  1- El puerto COM debe corresponde a dónde está conectado nuestra placa.
#     Se puede revisar en la IDE de Arduino.
#  2- La velocidad (9600) debe ser la MISMA que en el código Arduino.
arduino = serial.Serial("COM11", 9600, timeout=.1)

# Usamos la sentencia while True para crear un loop infinito.
while True:
    # Leemos una línea del Arduino y la decodificamos.
    lectura = arduino.readline().decode('utf-8')
    # Si no hay nada que leer, la función anterior retornará un string vacio.
    # Por lo tanto, sólo imprimiremos la lectura cuando tenga algun contenido
    if lectura != '':
        print(lectura)
