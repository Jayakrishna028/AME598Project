//imports
#include<WiFi.h>
#include<HTTPClient.h>

//defining the motors and 
// Wifi Credentials
const char* ssid = "SETUP-6AFB";
const char* password = "castle5853empty";

//The server URL to which the Sensor data is sent
const char* ServerName = "http://192.168.0.73:8080/sendSensorData/";
char* url;

// Ultrasonic Pins
const int trigPin1 = 2;
const int echoPin1 = 4;
const int trigPin2 = 5;
const int echoPin2 = 18;
const int trigPin3 = 19;
const int echoPin3 = 21;

const int rightPin1 = 22;
const int rightPin2 = 23;
const int leftPin1 = 35;
const int leftPin2 = 34;

// distCalculate(int pinNumber){
//   digitalWrite(pinNumber, LOW);
//   delay(2);
//   digitalWrite(pinNumber, HIGH);
//   //giving a small pulse
unsigned long lastTime = millis();

// }
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("Connecting to Wifi.....");
  pinMode(trigPin1 , OUTPUT);
  pinMode(echoPin1 , INPUT);
  pinMode(trigPin2 , OUTPUT);
  pinMode(echoPin2 , INPUT);
  pinMode(trigPin3 , OUTPUT);
  pinMode(echoPin3 , INPUT);
  pinMode(rightPin1 , OUTPUT);
  pinMode(rightPin2 , OUTPUT);
  pinMode(leftPin1 , OUTPUT);
  pinMode(leftPin2 , OUTPUT);
  
  
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
  Serial.println("started SLAMing");
}

void loop() {
  // main Loop
  if(millis()-lastTime>2){
    // long distanceFront, distanceRight, distanceLeft;

    // distanceFront = UltrasonicDistance(trigPin1, echoPin1);
    // distanceRight = UltrasonicDistance(trigPin2, echoPin2);
    // distanceLeft = UltrasonicDistance(trigPin3, echoPin3);

    // String url = String(ServerName) + "?distanceFront=" + distanceFront + "&distanceRight=" + distanceRight + "&distanceLeft=" + distanceLeft;
    // sendDataToServer(distanceFront , distanceRight, distanceLeft, url.c_str());
    // Serial.println(url);
    
    // lastTime = millis();

    moveForward();
    delay(5000);
    moveBack();
    delay(5000);
  }

  // if(distanceFront > 25){
  //   moveForward();
  // }
  // else if(distanceRight > 25 || distanceLeft > 25){
  //   if(distanceRight > 25){
  //     turnRight()
  //   }
  //   elseif(distanceLeft > 25){
  //     turnLeft();
  //   }
  // }
  // else{
  //   moveBack();s
  // }
}

long UltrasonicDistance(int trigPin , int echoPin){
  // Measure distance from sensor
  long distance , duration;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  return distance;
}

void sendDataToServer(long distance1, long distance2, long distance3, const char* ServerName) {
  HTTPClient http;
    
  // Your IP address with path or Domain name with URL path 
  http.begin(ServerName);
  
  // Send HTTP POST request
  int httpResponseCode = http.GET();
  
  String payload = "{}"; 
  
  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

}

void moveForward(){
  digitalWrite(rightPin1 , HIGH);
  digitalWrite(rightPin2 , LOW);
  digitalWrite(leftPin1, HIGH);
  digitalWrite(leftPin2 , LOW);
}

void moveBack(){
  digitalWrite(rightPin1 , LOW);
  digitalWrite(rightPin2 , HIGH);
  digitalWrite(leftPin1, LOW);
  digitalWrite(leftPin2 , HIGH);
}

void turnRight(){
  digitalWrite(rightPin1 , LOW);
  digitalWrite(rightPin2 , LOW);
  digitalWrite(leftPin1, HIGH);
  digitalWrite(leftPin2 , LOW);
}

void turnLeft(){
  digitalWrite(rightPin1 , HIGH);
  digitalWrite(rightPin2 , LOW);
  digitalWrite(leftPin1, LOW);
  digitalWrite(leftPin2 , LOW);
}
