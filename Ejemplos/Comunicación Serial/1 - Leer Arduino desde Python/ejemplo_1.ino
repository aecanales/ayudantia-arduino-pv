/*
  Ayudantia Arduino: Comunicación Serial
  IDI1015 - Pensamiento Visual @ PUC
  Alonso Canales(aecanales@uc.cl)

  Ejemplo 1: Leer Arduino desde Python
*/

void setup() {
  /*
  Abrimos el canal serial del Arduino.
  La velocidad aquí debe ser la misma que en el código de Python.
  */
  Serial.begin(9600);
}

void loop() {
  /*
  Mandamos un mensaje cada segundo. Como Python agrega su propio salto
  de linea, usamos Serial.print().
  */
  Serial.print("Hola desde Arduino.");
  delay(1000);
}
