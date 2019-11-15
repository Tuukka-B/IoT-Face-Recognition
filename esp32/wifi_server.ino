#include "WiFi.h"
 
const char* ssid = "OnePlus 6T";
const char* password =  "lorppahuuli";
 
WiFiServer wifiServer(80);
 
int ledPin = 14;
 
void processReceivedValue(char command){
 
  if(command == '1'){ digitalWrite(ledPin, HIGH);}
  else if(command == '0'){ digitalWrite(ledPin, LOW);}
 
  return;
}
 
void setup() {
 
  Serial.begin(115200);
 
  delay(1000);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());
 
  wifiServer.begin();
 
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}
 
void loop() {
 
  WiFiClient client = wifiServer.available();
 
  if (client) {
 
    while (client.connected()) {
 
      while (client.available()>0) {
        char c = client.read();
        processReceivedValue(c);
        Serial.write(c);
        Serial.println("");
      }
 
      delay(10);
    }
 
    client.stop();
    Serial.println("Client disconnected");
 
  }
}
