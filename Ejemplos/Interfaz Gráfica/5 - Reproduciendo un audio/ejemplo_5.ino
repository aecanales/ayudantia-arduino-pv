/*
  Ayudantia Arduino: Comunicación Serial
  IDI1015 - Pensamiento Visual @ PUC
  Alonso Canales(aecanales@uc.cl)

  Ejemplo 5: Reproduciendo un audio

  Para este ejemplo, es necesario tener un sensor conectado al pin A0.
  Notar que es el mismo código que el ejemplo 4.
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
    Para realizar la comparación, usaremos comillas simples dado que son carácteres, no strings. 
    Según el valor que reciba, apagaremos o prenderemos el LED.
    */
    if (lectura == '0') {
      digitalWrite(LED_BUILTIN, LOW);  
    }
    if (lectura == '1') {
      digitalWrite(LED_BUILTIN, HIGH);  
    }
  }

    
  Serial.println(analogRead(A0));
}
