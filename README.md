# Ayudantia Arduino - Pensamiento Visual @ PUC
Colección de clases y ejemplos de código de la ayudantía de Arduino del curso exploratorio del Major IDI **[IDI1015 Pensamiento Visual](http://catalinacortazar.com/PensamientoVisual/)** @ Pontificia Universidad Católica de Chile. Parte de la inciativa **[DILAB.](https://www.di-lab.cl/)**

## Clases
* **Arduino Básico I:** Introdución a lo que es Arduino y cómo controlar un LED.
* **Arduino Básico II:** Repaso. Introdución a la lectura análoga y como contrar un servo motor.
* **Arduino Avanzado I:** Clase teoríca. Introducción de más conceptos de programación. Muestra de actuadores, sensores y shields. Explicación de la utilidad de un Raspberry Pi.

## Ejemplos
## Básicos
Ejemplos que demuestran los comandos básicos para interactuar con un Arduino.
1. **Blink:** Mediante el comando ``digitalWrite`` y ``delay``, enciende y apaga el LED *on-board* del Arduino.
2. **Servo:** Controla un motor servo mediante un potenciómetro.
### Comunicación serial
Estos ejemplos requieren tener [Python 3+ instalado](https://www.python.org/downloads/) y las librerias ``pygame``, ``pyserial`` y ``opencv-python``. Para instalar las librerias, se debe ejecutar ``cmd.exe`` como administrador e ingresar el comando ``pip install pygame pyserial opencv-python`` escribiendolo y presionando Enter. Si no reconoce el comando `pip`, [deberán instalarlo manualmente](https://www.liquidweb.com/kb/install-pip-windows/) y reiniciar su computador.
1. **Leer Arduino desde Python:** Se envia un mensaje desde Arduino a Python, el cuál Python imprime en pantalla.
2. **Mandar mensaje a Arudino desde Python:** Se envia un mensaje desde Python a Arduino para controlar un LED.
3. **Interfaz simple para controlar Arduino:** Mediante ``pygame`` se crea una interfaz con dos botones para encender y apagar un LED.
4. **Abrir video cuando se manda mensaje desde Arduino:** Mediante un mensaje mandado periodicamente por el Arduino se abren 2 videos en Python con ``opencv``.

## Preguntas frecuentes

### ¿Dónde puedo conseguir componentes electrónicos? 
Puedes pedir componentes del [stock del Major](https://tinyurl.com/StockIDI) enviándome un email. Si necesitas un componente que no tenemos, te puedo recomendar estas tiendas que me han funcionado bien:
* [SomosMaker](https://www.somosmakers.cl/)
* [AMG Kits](https://amgkits.com/)
* [AFEL](https://afel.cl/?v=5bc574a47246)

Si buscan tiendas de Arduino en Google probablemente se topen con [MCI Electronics,](https://www.mcielectronics.cl/) el cual es una buena tienda, pero bastante más cara que las otras. Lo recomiendo sólo si el producto está con descuento o es el único lugar dónde encontraron el componente que necesitan.
