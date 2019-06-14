# Comunicación serial
Estos ejemplos requieren tener [Python 3+ instalado](https://www.python.org/downloads/) y las librerias ``pygame``, ``pyserial`` y ``opencv-python``. Para instalar las librerias, se debe ejecutar ``cmd.exe`` como administrador e ingresar el comando ``pip install pygame pyserial opencv-python`` escribiendolo y presionando Enter. Si no reconoce el comando `pip`, [deberán instalarlo manualmente](https://www.liquidweb.com/kb/install-pip-windows/) y reiniciar su computador.
1. **Leer Arduino desde Python:** Se envia un mensaje desde Arduino a Python, el cuál Python imprime en pantalla.
2. **Mandar mensaje a Arudino desde Python:** Se envia un mensaje desde Python a Arduino para controlar un LED.
3. **Interfaz simple para controlar Arduino:** Mediante ``pygame`` se crea una interfaz con dos botones para encender y apagar un LED.
