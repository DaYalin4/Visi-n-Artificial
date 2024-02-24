#include <Servo.h>

Servo servoX;
Servo servoY;

int anguloX;
int anguloY;

byte led1 = 2;
byte led2 = 3;
byte led3 = 4;
byte led4 = 5;
byte led5 = 6;

String str1;
String str2;
String str3;
String str4;
String str5;

int dato1 = 640;
int dato2 = 360;
int dato3;
int dato4;
int dato5;

void setup() {
  Serial.begin(9600);
  servoX.attach(7);
  servoY.attach(8);
}

void loop() {
  
  if(Serial.available()){
    //         leer cadena hasta...
    str1 = Serial.readStringUntil('A');
    dato1 = str1.toInt();

    str2 = Serial.readStringUntil('B');
    dato2 = str2.toInt();

    str3 = Serial.readStringUntil('\n');
    dato3 = str3.toInt();
  }
  
  if(dato3 < 50){
    anguloX = map(dato1, 0, 1280, 0, 180);
    anguloY = map(dato2, 0, 720, 0, 180);

    servoX.write(anguloX);
    servoY.write(anguloY);
  }
  else{
    servoX.write(90);
    servoY.write(90);
  }

  Serial.print(dato1);
  Serial.print("     ");
  Serial.print(dato2);
  Serial.print("     ");
  Serial.println(dato3);
}






