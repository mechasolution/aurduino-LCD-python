#include <LiquidCrystal.h>
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

String str1 = "";
String str2 = "Serial monitor";

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Serial monitor");
  Serial.print("O");
}
void loop() 
{  
  if(Serial.available() > 0){
    str1 = str2;
    str2 = "";
    do{
      if(Serial.available() > 0){
        str2 +=  String((char) Serial.read());
      }
    }while(!str2.endsWith("\r\n"));
    str2 = str2.substring(0,str2.length()-2);
    if(str2.length() > 16){
      str2 = str2.substring(0,16);
    }
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(str1);
    lcd.setCursor(0, 1);
    lcd.print(str2);
  }
}
