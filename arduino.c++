#include "AFMotor.h"  //библиотека моторов для шилда L293D
int port; //переменная для получения данных с порта
    
AF_DCMotor motor1(1); //мотор 1
AF_DCMotor motor2(2); //мотор 2
AF_DCMotor motor3(3); //мотор 3
AF_DCMotor motor4(4); //мотор 4
   
void setup() 
{  
  Serial.begin(9600); // порт

  motor1.setSpeed(255); //скорость 0-255
  motor1.run(RELEASE);  // STOP
  motor2.setSpeed(255);    
  motor2.run(RELEASE);    
  motor3.setSpeed(255);    
  motor3.run(RELEASE);    
  motor4.setSpeed(255);    
  motor4.run(RELEASE);  
}

void loop()
{
  if(Serial.available() > 0) //если буфер > 0 
  {
    port = Serial.read(); //чтение порта в переменную 'port'
  }

  if(port == 'f') //если получили 'f' -> впреде
  {
    motor1.run(BACKWARD);   
    motor2.run(BACKWARD); 
    motor3.run(FORWARD); 
    motor4.run(FORWARD); 
  }
  else if(port == 'e') //если получили 'e' -> вправо
  {
    motor1.setSpeed(255);
    motor1.run(BACKWARD);    
    motor2.setSpeed(255);    
    motor2.run(BACKWARD);    
    motor3.setSpeed(0);    
    motor3.run(FORWARD);    
    motor4.setSpeed(0);    
    motor4.run(FORWARD);  
  }
  else if(port == 'r') //если получили 'r' -> влево
  {
    motor1.setSpeed(0);
    motor1.run(BACKWARD);    
    motor2.setSpeed(0);    
    motor2.run(BACKWARD);    
    motor3.setSpeed(255);    
    motor3.run(FORWARD);    
    motor4.setSpeed(255);    
    motor4.run(FORWARD);  
  }
  else if(port == 'd') //если получили 'd' -> стоп
  {
    motor1.run(RELEASE);   
    motor2.run(RELEASE); 
    motor3.run(RELEASE); 
    motor4.run(RELEASE); 
  }
}
}
