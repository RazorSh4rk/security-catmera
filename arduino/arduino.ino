#include <ESP8266WiFi.h>
#include <Servo.h>
 
const char* ssid = "ssid";
const char* password = "password";
 
WiFiServer server(80);
Servo servoX;
Servo servoY;
 
void setup() {
  Serial.begin(115200);
  delay(10);
  servoX.attach(D4);
  servoY.attach(D3);
 
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 
  // Start the server
  server.begin();
  Serial.println("Server started");
 
  // Print the IP address
  Serial.print("Use this URL : ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
 
}
 
void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
 
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
 
  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();
 
  // Match the request
 
  int pos = request.indexOf("/pos=");
  if(pos != -1){
    int x = request.substring(pos + 5, pos + 8).toInt();
    int y = request.substring(pos + 9, pos + 12).toInt();
    Serial.println("------");
    Serial.println(x);
    Serial.println(y);
    Serial.println("------");
    servoX.write(x);
    servoY.write(y);
  }
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/json");
  client.println("Access-Control-Allow-Origin: *");
  client.println("");
  delay(1);
  Serial.println("Client disconnected");
  Serial.println("");
 
}
