#include <Servo.h>

Servo miServo;

byte led1 = 5;
byte led2 = 6;

int datosX;
int datosY;

String str1;
String str2;

int ejeX;
int ejeY;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  miServo.attach(7);
}

void loop() {
  if(Serial.available() > 0){
       //       leer cadena hasta...
    str1 = Serial.readStringUntil('A');
    datosX = str1.toInt();

    str2 = Serial.readStringUntil('\n');
    datosY = str2.toInt();
  }

  ejeX = map(datosX, 0, 1280, 180, 0);

  miServo.write(ejeX);
 
}




