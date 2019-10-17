/*
  Ayudantia Arduino: Básicos
  IDI1015 - Pensamiento Visual @ PUC
  Alonso Canales(aecanales@uc.cl)

  Ejemplo 1: Blink
*/

// Notemos primero que podemos escribir comentarios en Arduino usando doble barra oblicua.
/*
   También podemos escribir comentarios de múltiples líneas usando barra oblicua con asterisco.
   Los comentarios son útiles para explicar como funcionan ciertas partes del código.
*/

/* 
  Para definir una variable en Arduino debemos escribir primero su tipo(s) y luego su nombre.
  El tipo 'int' representa un número entero, mientras que 'const' es un valor constante que no
  cambiaremos durante la ejecución del código. 
  En este caso, estamos definiendo una variable que va a contener el pin en cuál se ubica el LED
  que controlaremos. En el caso del Arduino Uno, el LED on-board se ubica en el pin 13.
*/

const int LED_PIN = 13;  // ¡Cada sentencia que escribimos debe terminar con ';' o sino se cae el programa!


// 'setup()' contiene código que se ejecutará una única vez al encenderse el Arduino.
void setup() {
  // El comando 'pinMode' activa un pin de la placa Arduino y toma dos parámetros: el n° de pin y el modo.
  // En este caso elegimos el modo 'OUTPUT' ya que deseamos enviar un señal indicando si apagar o encender el LED.
  pinMode(LED_PIN, OUTPUT);
}

// 'loop()' contiene código que correrá continuamente mientras esté encendido el Arduino.
void loop() {
  // El comando 'digitalWrite' envia una señal al pin indicado. En este caso enviamos 'HIGH' para encender el LED.
  digitalWrite(LED_PIN, HIGH);
  
  // 'delay' pausa la ejecución de nuestro código durante un cantidad de millisegundos (1000ms = 1sec).
  // ¡Es necesario ya que si no se encendería y apagaría tan rápido el LED que no lo veriamos!
  delay(1000);

  // Ahora apágamos el LED y pausamos durante otro segundo.
  digitalWrite(LED_PIN, HIGH);
  delay(1000);

  // Al llegar aquí el Arduino volverá al comienzo de 'loop()', así ejectuándose el código infinitamente.
}