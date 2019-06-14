# Ayudantia Arduino - Pensamiento Visual @ PUC
Colección de clases y ejemplos de código de la ayudantía de Arduino del curso exploratorio del Major IDI **[IDI1015 Pensamiento Visual](http://catalinacortazar.com/PensamientoVisual/)** @ Pontificia Universidad Católica de Chile. Parte de la inciativa **[DILAB.](https://www.di-lab.cl/)**

## Clases
* **Arduino Básico I:** Introdución a lo que es Arduino y cómo controlar un LED.
* **Arduino Básico II:** Repaso. Introdución a la lectura análoga y como contrar un servo motor.
* **Arduino Avanzado I:** Clase teoríca. Introducción de más conceptos de programación. Muestra de actuadores, sensores y shields. Explicación de la utilidad de un Raspberry Pi.

## Ejemplos
### Comunicación serial
Estos ejemplos requieren tener [Python 3+ instalado](https://www.python.org/downloads/) y las librerias ``pygame``, ``pyserial`` y ``opencv-python``. Para instalar las librerias, se debe ejecutar ``cmd.exe`` como administrador e ingresar el comando ``pip install pygame pyserial opencv-python`` escribiendolo y presionando Enter. Si no reconoce el comando `pip`, [deberán instalarlo manualmente](https://www.liquidweb.com/kb/install-pip-windows/) y reiniciar su computador.
1. **Leer Arduino desde Python:** Se envia un mensaje desde Arduino a Python, el cuál Python imprime en pantalla.
2. **Mandar mensaje a Arudino desde Python:** Se envia un mensaje desde Python a Arduino para controlar un LED.
3. **Interfaz simple para controlar Arduino:** Mediante ``pygame`` se crea una interfaz con dos botones para encender y apagar un LED.
