#include <iarduino_DHT.h> //подключаем библиотеку для работы с датчиком 
#define DHTPIN 2  //пин к которому подключен датчик
#define reley_pin 6 //пин к которому подключено реле
#define fan_pin 4 //пин к которому подключен вентилятор
iarduino_DHT dht ( DHTPIN ); //обьявляем датчик
void setup() {  

    Serial.begin(19200); //обьявляем работу порта на скорости 19200 бод
    pinMode(reley_pin,OUTPUT); //обьявляем пин на котором реле как выход
    pinMode(fan_pin,OUTPUT); //обьявляем пин на котором подключен вентилятор как выход
   

}
void loop() { 
  
  if (Serial.available() > 0){ //если на пор поступает информация
  dht.read(); //читаем показания с датчика
  if (Serial.read()== '1') { //если сигнал на ком порте 1 
      digitalWrite(reley_pin, HIGH); //подаем питание на пин реле
  }
  if (Serial.read()== '2') { 
      digitalWrite(reley_pin, LOW);
  }
  if (Serial.read()== '3') { 
      digitalWrite(fan_pin, HIGH);
  }
  if (Serial.read()== '4') { 
      digitalWrite(fan_pin, LOW);
  }
  if (Serial.read()== '5') { //если сигнал на ком порте 5
      Serial.print(round(dht.tem)); //отправить на порт округленные данные с датчика
    }
  }
  if (Serial.read()== '6') {
    Serial.print(round(dht.hum));
  }
  }
