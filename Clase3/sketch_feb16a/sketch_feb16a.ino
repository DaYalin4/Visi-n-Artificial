//DECLARAMOS LAS VARIABLES PARA LOS LEDS (no. pin)
byte led1= 5;
byte led2 = 6;
 

//Para Guardarlos como cadena de caracteres diferentes.
String str1;
String str2;
//Para guardar la cadena como números
int datosX; 
int datosY;

int ejeX;
int ejeY;

void setup() {
  Serial.begin(9600);
  //para inicializar los leds 
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

}

void loop() {
  // nos entrega un numero mayor que 0 
  if (Serial.available() > 0){
    // Leer cadena hasta ...
    str1 = Serial.readStringUntil('A');
    datosX = str1.toInt();

    str2 = Serial.readStringUntil('\n');
    datosY = str2.toInt();
  }
  //Para no tener errores por las dimensiones de las ventanas.
  ejeX=map(datosX,0,1280,0,255);
  ejeY=map(datosY,0,720,0,255);

  // para mandar una señal
  analogWrite(led1,ejeX);
  analogWrite(led2,ejeY);

  //No es bueno tener tanta información en python
  //Serial.print(datosX);
  //Serial.print("    ");
  //Serial.println(datosY);

}
