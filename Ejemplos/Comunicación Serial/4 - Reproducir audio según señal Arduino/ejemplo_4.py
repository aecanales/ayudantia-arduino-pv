# Ayudantia Arduino: Comunicación Serial
# IDI1015 - Pensamiento Visual @ PUC
# Alonso Canales(aecanales@uc.cl)
#
# Ejemplo 5: Reproducir audio según señal Arduino

# Importamos la libreria serial para poder comunicarnos con una placa Arduino.
import serial

# La libreria playsound nos da la funcionalidad para reproducir sonidos.
from playsound import playsound

# Creamos la conexión con la placa. Debemos tener en cuenta:
#  1- El puerto COM debe corresponde a dónde está conectado nuestra placa.
#     Se puede revisar en la IDE de Arduino.
#  2- La velocidad (9600) debe ser la MISMA que en el código Arduino.
arduino = serial.Serial("COM18", 9600, timeout=.1)

# Usamos la sentencia while True para crear un loop infinito.
while True:
    # Leemos una línea del Arduino y la decodificamos.
    lectura = arduino.readline().decode('utf-8')
    
    # Si no hay nada que leer, la función anterior retornará un string vacio.
    # Por lo tanto, sólo reproduciremos una sonido cuando la lectura cuando tenga algún contenido
    if lectura != '':
        print(f'Recibí un mensaje: {lectura}')
        playsound(lectura)
