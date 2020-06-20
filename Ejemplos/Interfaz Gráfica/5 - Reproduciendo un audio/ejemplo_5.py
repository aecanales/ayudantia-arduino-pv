# Ayudantia Arduino: Comunicación Serial
# IDI1015 - Pensamiento Visual @ PUC
# Alonso Canales(aecanales@uc.cl)
#
# Ejemplo 5: Reproduciendo un audio

# Para crear la interfaz, usaremos la libreria pygame.
import serial
import pygame
from pygame.locals import Rect

# La libreria playsound nos da la funcionalidad para reproducir sonidos.
from playsound import playsound

arduino = serial.Serial("COM9", 9600, timeout=.1)

# Inicializamos pygame.
pygame.init()
# Definimos una ventana de 400x400 pixeles.
ventana = pygame.display.set_mode((400, 400))

# Cargamos las imágenes que usaremos.
on = pygame.image.load('on.png')
off = pygame.image.load('off.png')

# Definimos la posición en que estará cada imagen mediante "Rect".
# Los parámetros tiene el siguiente orden: (x, y, ancho, altura)
on_position = Rect(100, 100, 64, 64)
off_position = Rect(200, 100, 64, 64)

# Usaremos este booleano para controlar cuando se puede reproducir el sonido o no.
puedeTocarSonido = True

done = False
while not done:
    # Boramos todo lo que está en la pantalla.
    ventana.fill((0, 0, 0))

    # En cada instante, usamos "blit" para dibujar las imágenes "on" y "off" en sus posiciones correspondientes.
    ventana.blit(on, on_position)
    ventana.blit(off, off_position)

    # Ahora leemos la información del sensor que envia el Arduino.
    # Ya que usamos "println", necesitamos strip para sacar el salto de línea.
    lectura = arduino.readline().decode('utf-8').strip()

    if lectura != '':
        # Definimos el color de nuestra barra usando código RGB.
        color = (255, 0, 0)
        # Creamos un rect para definir la posicion y tamaño de la barra.
        bar_position = Rect(100, 200, 100 * (int(lectura) / 1024), 10)
        # Lo dibujamos en la pantalla.
        pygame.draw.rect(ventana, color, bar_position)

        # Si el valor del sensor excede 900, reproducimos el sonido.
        if (int(lectura) > 900 and puedeTocarSonido):
            playsound("sonido.mp3", False)
            # Detenemos la reproducción de sonido cuando empezó a tocar el sonido.
            puedeTocarSonido = False

        # En mi caso, vuelvo a habilitar el sonido cuando el sensor baja a menos de 100.
        if (int(lectura) < 100):
            puedeTocarSonido = True
    
    # Luego, revisamos los eventos, lo que corresponde al input del usuario.
    for event in pygame.event.get():
        # Este evento corresponde a cuando el usuario aprieta la "X" de la aplicación.
        if event.type == pygame.QUIT:
            done = True
        
        # Este evento corresponde a cuando se apreta un botón del mouse.
        # El 1 nos dice que fue el botón izquierdo.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mpos = pygame.mouse.get_pos()  # Esto nos retorna la posición (x, y) del click.

            # La función colliderpoint(mpos) nos retorna verdadero si el
            # usuario hizo click dentro del botón respectivo.
            if on_position.collidepoint(mpos):
                arduino.write('1'.encode())
            if off_position.collidepoint(mpos):
                arduino.write('0'.encode()) 

    # Para dibujar lo que escribimos en pantalla, debemos usar flip().
    pygame.display.flip()
