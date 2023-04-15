#include <Servo.h>    // Instead of directly changing the PWM value,
                     // we'll use Servo library
Servo myservo;  
int angle = 0;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);  // Set the servo control pin
}

void loop() {
  // put your main code here, to run repeatedly:
  int temp = 60;
   int pos = map(temp, 60, 90, 0, 180);
   myservo.write(pos);
 }
