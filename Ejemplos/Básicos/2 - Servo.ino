/*
  Ayudantia Arduino: Básicos
  IDI1015 - Pensamiento Visual @ PUC
  Alonso Canales(aecanales@uc.cl)

  Ejemplo 2: Servo
*/

// Lo primero que debemos hacer es incluir la liberia de Servo.
// Las librerias son paquetes de código que nos facilitan interactuar con componentes.
#include <Servo.h>

// Una vez incluida la libreria, podemos crear un objeto servo y una variable para indicar dónde lo conectaremos.
// Ojo que el pin debe ser un pin PWN (con un '~' al lado del número).
Servo myServo;
int servoPin = 9;

// Indicamos en que pin análogo conectaremos el potenciómetro.
int potPin = 0;

void setup() {
  /* 
    El Serial nos permite enviar información desde el Arduino al computador y viceversa. Es muy útil a la hora
    de probar si el código está funcionando o si queremos hacer que el Arduino interactue con una aplicación de Python.
    Para poder usarlo, debemos escribir esta línea para inicializarla y luego una vez corriendo el Arduino, 
    abrir el 'monitor serial' (la lupita arriba a la derecha). 
  */
  Serial.begin(9600);

  // Usamos el comando 'attach' para decirle al objeto 'myServo' donde está conectado el servo.
  myServo.attach(servoPin);
}

void loop() {
  // Primero leemos el valor del potenciómetro con el comando 'analogRead'.
  // Esto retornará un valor entre 0 y 1023.
  int lectura = analogRead(potPin);

  // Nuestro servo puede moverse entre 0 y 180 grados, ¿pero como convertimos la lectura del potenciómetro en
  // un ángulo? Para esto podemos usar 'map', el cual traduce proporcionalmente un valor  ('lectura' en nuestro caso) 
  // de un rango a otro (en nuestro caso, de 0 - 1023 a 0 - 180). 
  int angulo = map(lectura, 0, 1023, 0, 180);

  // Para mover el servo a un cierto ángulo, usamos el comando 'write'.
  myServo.write(angulo);

  // Para mandar mensajes a nuestro serial, podemos usar los comandos 'print' y 'println'.
  // Si usamos el primero, el siguiente mensaje que mandemos se imprimirá en la misma línea,
  // mientras que si usamos el segundo se agrega un salto de línea al final del mensaje.
  Serial.print("Lectura: ");
  Serial.print(lectura);
  Serial.print(" Ángulo: ")
  Serial.println(angulo);

  // Para darle tiempo al servo para moverse, es buena costumbre agregar un pequeño delay.
  delay(50);
}