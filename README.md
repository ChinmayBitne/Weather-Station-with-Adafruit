# Weather Station with Adafruit
Welcome to the Weather Station with Adafruit project! This project combines IoT technology, environmental sensing, and web development to create a comprehensive weather monitoring system. Using an ESP8266 NodeMCU and a DHT11 sensor, this weather station collects real-time data on temperature, and humidity. The data is then displayed on an OLED screen and can be uploaded to the Adafruit IO platform for remote monitoring. Additionally, the project features a web interface for data visualization and management.

**Features**

🌡 Real-Time Environmental Sensing: Collect temperature, humidity, and pressure data.

📡 WiFi Connectivity: Upload sensor data to Adafruit IO for IoT applications.

🌐 Web Interface: Visualize data through a custom web page, including real-time updates.

📊 Database Management: Store historical sensor data for trend analysis.

🔒 Automated Testing: Ensure reliability of the web platform with Selenium tests.

🛠 Easy Customization: Tailor the project to meet specific monitoring needs


**Components**

ESP8266 NodeMCU
DHT11 sensor for temperature, and humidity
OLED Display
Breadboard and jumper wires

**Setup and Installation**

_Hardware Assembly:_ Connect the DHT11 sensor and OLED display to the ESP8266 according to the wiring diagram.

_Software Configuration:_ Upload the Arduino sketch (Weather_Station.ino) to the ESP8266.

_Web and Database Setup:_ Deploy the PHP scripts on your web server and create the MySQL database using the schema.

_Adafruit IO Setup:_ Create an account on Adafruit IO and configure the feed for receiving sensor data.


**Usage**

The OLED display will show real-time sensor readings once the device is powered up.
Data is uploaded to Adafruit IO automatically for remote monitoring.
Access the web interface via your web server's URL to view historical data and trends.
