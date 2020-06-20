# Ayudantia Arduino: Comunicación Serial
# IDI1015 - Pensamiento Visual @ PUC
# Alonso Canales(aecanales@uc.cl)
#
# Ejemplo 2: Mandar mensaje a Arduino desde Python

import serial

arduino = serial.Serial("COM11", 9600, timeout=.1)

print('PROGRAMA CONTROLADOR DE LEDS')
while True:
    print('Que deseas hacer? 0=apagar LED, 1=prender LED')
    # Leemos lo que ingresa el usuario.
    respuesta = input() 
    # Para mandar la respuesta del usuario a Arduino, debemos codificarlo mediante encode.
    arduino.write(respuesta.encode('utf-8'))
