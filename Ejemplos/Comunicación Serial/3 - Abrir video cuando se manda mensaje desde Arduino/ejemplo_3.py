# Ayudantia Arduino: Comunicación Serial
# IDI1015 - Pensamiento Visual @ PUC
# Alonso Canales(aecanales@uc.cl)
#
# Ejemplo 4: Abrir video cuando se manda mensaje desde Arduino

# Se usará la libreria OpenCV para reproducir videos.
import serial
import cv2

arduino = serial.Serial("COM11", 9600, timeout=.1)

# Usaremos una variable de texto para guardar que video estamos tocando.
# 0 significa ningun video.
video_que_tocar = '0'

# Abrimos los dos videos que vamos a reproducir.
# Deben estar en la misma carpeta que el .py.
video_1 = cv2.VideoCapture('video_1.mp4')
video_2 = cv2.VideoCapture('video_2.mp4')
cv2.startWindowThread()

# Usaremos esta variable para llevar cuenta del progreso del
# video y reiniciarlo cuando llegue al final.
frame_counter = 0

while True:
    lectura = arduino.readline().decode('utf-8')

    # Solo cambiaremos el valor de video_que_tocar cuando llegue información del Arduino.
    if lectura != '':
        video_que_tocar = lectura

        # Cerramos la ventanas que esten abiertas.
        cv2.destroyAllWindows()
        # Reiniciamos el contador del progreso de video.
        frame_counter = 0

        # Si Arduino mandó '1', entonces reproduciremos el video_1.
        if video_que_tocar == '1':
            # Con este código creamos una ventana para el video y lo dejamos en pantalla completa.
            cv2.namedWindow('Video 1', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('Video 1', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Funciona de manera análoga para el video 2.
        if video_que_tocar == '2':
            cv2.namedWindow('Video 2', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('Video 2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Si estamos en el video 1, reproduciremos el video_1.
    if video_que_tocar == '1':
        # Leemos el archivo y avanzamos el contador de progreso.
        ret_val, frame = video_1.read()
        frame_counter += 1

        # Si vemos que estamos en el último frame del video, lo reiniciaremos.
        if frame_counter == video_1.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0
            video_1.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # Avanzamos el video al frame actual.
        cv2.imshow('Video 1', frame)

        # Esta sentencia es necesaria para que OpenCV no se quede pegado.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pass

    # Funciona de manera análoga para el video 2.
    if video_que_tocar == '2':
        ret_val, frame = video_2.read()
        frame_counter += 1

        if frame_counter == video_2.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0
            video_2.set(cv2.CAP_PROP_POS_FRAMES, 0)

        cv2.imshow('Video 2', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            pass
