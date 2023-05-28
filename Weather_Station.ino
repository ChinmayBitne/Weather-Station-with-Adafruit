#include <dht.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <Adafruit_MQTT.h>
#include <Adafruit_MQTT_Client.h>
#define DHTPIN 2

// Adafruit IO
#define AIO_SERVER      "io.adafruit.com"
#define AIO_SERVERPORT  1883
#define AIO_USERNAME    "xxxxxxxxx"  //username
#define AIO_KEY         "xxx_xxxxxxxxxxxxxxxxxxx" //aio_key

const char *ssid = "xxxxxxxx";  //ENTER YOUR WIFI ssid
const char *password = "xxxxxxxxx";  //ENTER YOUR WIFI password
WiFiClient client;
dht DHT;
// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);
Adafruit_MQTT_Publish Temp = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/Temperature");
Adafruit_MQTT_Publish Hum = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/Humidity");

void setup() {
  delay(1000);
  Serial.begin(115200);
  WiFi.mode(WIFI_OFF);        //Prevents reconnection issue (taking too long to connect)
  delay(1000);
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot
  WiFi.begin(ssid, password);     //Connect to your WiFi router
  Serial.println("");
  Serial.print("Connecting");
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  //If connection successful show IP address in serial monitor 
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  //IP address assigned to your ESP

  connect();
}

void loop() {
    //Adafruit IO
  if(! mqtt.ping(3)) {
    // reconnect to adafruit io
    if(! mqtt.connected())
      connect();
  }
  int chk = DHT.read11(DHTPIN);
  int h = DHT.humidity;
  int t = DHT.temperature;
  delay(5000);
    if (! Temp.publish(t)) {                     //Publish to Adafruit
    Serial.println(F("Failed"));
  } 
  if (! Hum.publish(h)) {                     //Publish to Adafruit
    Serial.println(F("Failed"));
  }
  else {
    Serial.println(F("Sent!"));
  }

SendSensorData();
}

// connect to adafruit io via MQTT
void connect() {
  Serial.print(F("Connecting to Adafruit IO... "));
  int8_t ret;
  while ((ret = mqtt.connect()) != 0) {
    switch (ret) {
      case 1: Serial.println(F("Wrong protocol")); break;
      case 2: Serial.println(F("ID rejected")); break;
      case 3: Serial.println(F("Server unavail")); break;
      case 4: Serial.println(F("Bad user/pass")); break;
      case 5: Serial.println(F("Not authed")); break;
      case 6: Serial.println(F("Failed to subscribe")); break;
      default: Serial.println(F("Connection failed")); break;
    }

    if(ret >= 0)
      mqtt.disconnect();

    Serial.println(F("Retrying connection..."));
    delay(10000);
  }
  Serial.println(F("Adafruit IO Connected!"));
}

//function to send sensor data 
void SendSensorData() {
  HTTPClient http;    //Declare object of class HTTPClient
  int chk = DHT.read11(DHTPIN);
  String Temperature,Humidity, postData;
  Temperature=DHT.temperature;
    Humidity= DHT.humidity;
  //Post Data
  postData = "Temperature=" +  Temperature + "&Humidity=" + Humidity;
  
  http.begin(client,"http://192.168.36.19/esp8266/postData.php");              //change the ip to your computer ip address
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");    //Specify content-type header
 
  int httpCode = http.POST(postData);   //Send the request
  String payload = http.getString();    //Get the response payload
 
  Serial.println(postData);   //Print Values on serial moniter
  Serial.println(httpCode);   //Print HTTP return code
  Serial.println(payload);    //Print request response payload


  http.end();  //Close connection
  
  delay(5000);  //Post Data at every 5 seconds
}
