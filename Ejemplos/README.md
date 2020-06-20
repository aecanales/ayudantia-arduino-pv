# Ejemplos
## Básicos
Ejemplos que demuestran los comandos básicos para interactuar con un Arduino.
1. **Blink:** Mediante el comando ``digitalWrite`` y ``delay``, enciende y apaga el LED *on-board* del Arduino.
2. **Servo:** Controla un motor servo mediante un potenciómetro, además de demostrar el uso del monitor serial.

## Comunicación serial
Ejemplos de como comunicar Arduino con un computador al cual esta conectado con `Python.`

Estos ejemplos requieren tener [Python 3+ instalado](https://www.python.org/downloads/) y las librerias ``pygame``, ``pyserial``, ``opencv-python`` y `` playsound``. Para instalar las librerias, se debe ejecutar ``cmd.exe`` (o el terminal en el caso de Mac) como administrador e ingresar el comando ``pip install pygame pyserial opencv-python playsound`` escribiendolo y presionando Enter. Si no reconoce el comando `pip`, [deberán instalarlo manualmente](https://www.liquidweb.com/kb/install-pip-windows/) y reiniciar su computador.

Para correrlos, deben primero conectar el Arduino y subirle el código en el archivo ``.ino`` y una vez subida, correr el archivo de Python ``.py`` en IDLE o su programa de preferencia. Ojo que la conexión serial es exclusiva, por lo que al establecer una conexión entre Arduino y Python, no se podrá abrir el monitor serial desde la IDE de Arduino. Por otro lado, si tienen abierto el monitor serial, al correr el archivo Python probablemente tire un error ya que el Arduino ya está conectado al monitor serial.
1. **Leer Arduino desde Python:** Se envia un mensaje desde Arduino a Python, el cuál Python imprime en pantalla.
2. **Mandar mensaje a Arudino desde Python:** Se envia un mensaje desde Python a Arduino para controlar un LED.
3. **Abrir video cuando se manda mensaje desde Arduino:** Mediante un mensaje mandado periodicamente por el Arduino se abren 2 videos en Python con ``opencv``.
4. **Reproducir audio según señal Arduino:** Con la libreria ``playsound`` se reproduce un audio cada vez que el Arduino envia una señal.

## Interfaz Gráfica
Estos ejemplos muestran paso a paso como armar una interfaz gráfica en `Python` para comunicarse con Arduino. Esta interfaz podrá
* controlar un LED del Arduino mediante unos botones en la interfaz
* controlar el tamaño de una barra de la interfaz según la lectura de un sensor
* reproducir un audio cuando el sensor excede cierto valor

Estos ejemplos requieren tener [`Python` 3+ instalado](https://www.python.org/downloads/) y las librerias `pygame`, `pyserial`,  y `playsound`. Para instalar estas librerias, debe ejecutar `cmd.exe` (o el terminal en el caso de Mac) como administrador e escribir el comando: 
```
pip install pygame pyserial playsound
```
y luego presionar Enter. Si no se reconoce el comando `pip`, probablemente no lo instalaron al instalar Python, por lo que recomiendo que lo descarguen y instalen de nuevo.

Para correrlos, deben primero conectar el Arduino y subirle el código en el archivo `.ino` y una vez subida, correr el archivo de Python `.py` en IDLE o su programa de preferencia. Ojo que la conexión serial es exclusiva, por lo que al establecer una conexión entre Arduino y Python, no se podrá subir más codigo al Arduino hasta que cierren el programa Python. Por otro lado, si tienen abierto el monitor serial de Arduino, al correr el archivo Python probablemente tire un error ya que el Arduino ya está conectado al monitor serial.

Los ejemplos son:
1. **Arduino a Python:** Se envia un mensaje desde Arduino a Python, el cuál Python imprime en pantalla.
2. **Python a Arduino:** Se envia un mensaje desde Python a Arduino para controlar un LED.
3. **Agregando una interfaz:** Mediante `pygame` se crea una interfaz con dos botones para encender y apagar un LED.
4. **Visualizando un sensor:** Tomando como base la interfaz anterior, se agrega una barra que cambia de tamaño según el valor de un sensor que envia Arduino.
5. **Reproduciendo un audio:** Tomando como base la interfaz anterior, se reproduce un audio cuando el sensor excede cierto valor con la libreria `playsound`.