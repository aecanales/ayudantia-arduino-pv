# Ayudantia Arduino: Comunicación Serial
# IDI1015 - Pensamiento Visual @ PUC
# Alonso Canales(aecanales@uc.cl)
#
# Ejemplo 3: Interfaz simple para controlar Arduino

# Para crear la interfaz, usaremos la libreria pygame.
import serial
import pygame
from pygame.locals import Rect

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

done = False
while not done:
    # En cada instante, usamos "blit" para dibujar las imágenes "on" y "off" en sus posiciones correspondientes.
    ventana.blit(on, on_position)
    ventana.blit(off, off_position)
    
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
