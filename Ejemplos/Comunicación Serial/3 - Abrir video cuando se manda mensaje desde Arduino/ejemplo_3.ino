/*
  Ayudantia Arduino: Comunicación Serial
  IDI1015 - Pensamiento Visual @ PUC
  Alonso Canales(aecanales@uc.cl)

  Ejemplo 4: Abrir video cuando se manda mensaje desde Arduino
*/

/*
Usaremos una variable para anotar que video se está tocando en el computador. 
0 representa que no se está tocando un video, 1 el primer video, 2 el segundo, etc.
*/
int videoActivado = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (videoActivado == 0) {
    /* 
    En este ejemplo, simplemente esperaremos 5 segundos antes de empezar el video.
    En su código, podrian mandar el mensaje cuando e.j. se active un sensor de proximidad.
    */
    delay(5 * 1000);
    Serial.print("1"); // Llamamos el primer video.
    videoActivado = 1;
  }
  if (videoActivado == 1) {
    // Esperamos diez segundos y llamamos el segundo video.
    delay(10 * 1000);
    Serial.print("2");
    videoActivado = 2;
  }
  if (videoActivado == 2) {
    // Esperamos diez segundos y llamamos 0 para cerrar los videos y empezar de nuevo.
    delay(10 * 1000);
    Serial.print("0");
    videoActivado = 0;
  }
}
