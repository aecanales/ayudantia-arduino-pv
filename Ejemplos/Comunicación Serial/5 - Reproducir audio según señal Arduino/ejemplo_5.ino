/*
  Ayudantia Arduino: Comunicación Serial
  IDI1015 - Pensamiento Visual @ PUC
  Alonso Canales(aecanales@uc.cl)

  Ejemplo 5: Reproducir audio según señal Arduino
*/

void setup() {
  /*
  Abrimos el canal serial del Arduino.
  La velocidad aquí debe ser la misma que en el código de Python.
  */
  Serial.begin(9600);
}

void loop() {
  // Mandamos un mensaje cada diez segundos. Este contendrá el nombre del audio que deseamos reproducir.
  Serial.print("sonido.mp3");
  delay(10 * 1000);
}
