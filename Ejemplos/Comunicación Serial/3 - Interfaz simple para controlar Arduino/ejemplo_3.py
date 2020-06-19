# Ayudantia Arduino: Comunicación Serial
# IDI1015 - Pensamiento Visual @ PUC
# Alonso Canales(aecanales@uc.cl)
#
# Ejemplo 3: Interfaz simple para controlar Arduino

# Para crear la interfaz, usaremos la libreria pygame.
import serial
import pygame

arduino = serial.Serial("COM11", 9600, timeout=.1)

# Inicializamos pygame.
pygame.init()
# Definimos una ventana de 400x400 pixeles.
ventana = pygame.display.set_mode((400, 400))

done = False
while not done:
    # Primero, revisar los eventos (input del usuario).
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
            if on.collidepoint(mpos):
                arduino.write('1'.encode())
            if off.collidepoint(mpos):
                arduino.write('0'.encode())

    # Definimos dos botones. El primer parámetro es la ventana, el segundo es el color
    # en código RGB, y finalmente la forma de rectángulo con su posición X/Y y tamaño horizontal/vertical.  
    on = pygame.draw.rect(ventana, (0, 128, 255), pygame.Rect(100, 100, 100, 60))
    off = pygame.draw.rect(ventana, (255, 0, 0), pygame.Rect(200, 100, 100, 60))

    # Para dibujar lo que escribimos en pantalla, debemos usar flip().
    pygame.display.flip()
