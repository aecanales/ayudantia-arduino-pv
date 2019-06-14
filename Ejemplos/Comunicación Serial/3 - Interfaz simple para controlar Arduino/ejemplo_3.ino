/*
  Ayudantia Arduino: Comunicación Serial
  IDI1015 - Pensamiento Visual @ PUC
  Alonso Canales(aecanales@uc.cl)

  Ejemplo 3: Interfaz simple para controlar Arduino
  (notar que el código de Arduino de este ejemplo es el mismo que el ejemplo 2)
*/


void setup() {
  // Abrimos el canal serial del Arduino.
  Serial.begin(9600);
  // Activamos el LED integrado de la placa.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Sólo revisaremos el serial cuando haya algo que leer.
  if (Serial.available() > 0){
    // Cuando leamos del serial, leeremos de UN carácter a la vez.
    char lectura;
    lectura = Serial.read();
    
    /*
    Para realizar la comparación, es necesario convertir la variable del tipo char
    al tipo String. Según el valor que reciba, apagaremos o prenderemos el LED.
    */
    if (String(lectura) == "0") {
      digitalWrite(LED_BUILTIN, LOW);  
    }
    if (String(lectura) == "1") {
      digitalWrite(LED_BUILTIN, HIGH);  
    }
  }
}
