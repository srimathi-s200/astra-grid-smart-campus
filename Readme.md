# 🚀 Astra Grid – Smart Campus Energy & Environment System

Astra Grid is an ESP32-based smart campus automation prototype designed to monitor environmental conditions and occupancy and make local decisions for lighting and cooling.

The system combines **embedded hardware, sensors, serial communication, Python Flask, APIs, and a live web dashboard** into a single working system.

---

## 📌 Project Overview

Traditional campus automation systems often depend on manual control or separate monitoring systems.

Astra Grid provides a simple integrated approach:

- Detects human presence using a PIR sensor
- Measures ambient light using an LDR
- Monitors temperature and humidity using a DHT11
- Automatically controls a lighting indicator based on occupancy and light level
- Determines whether cooling is required based on temperature
- Sends live sensor data from ESP32 to a Python Flask backend
- Displays the information on a real-time web dashboard

---

## 🧠 System Architecture

```text
                  ┌─────────────────────┐
                  │       Sensors       │
                  │                     │
                  │  PIR    LDR   DHT11 │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │        ESP32        │
                  │                     │
                  │ Sensor Processing   │
                  │ Decision Logic      │
                  └──────────┬──────────┘
                             │
                     Serial Communication
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Python + Flask    │
                  │                     │
                  │ Serial Data Reader  │
                  │ REST API            │
                  └──────────┬──────────┘
                             │
                          JSON Data
                             │
                             ▼
                  ┌─────────────────────┐
                  │    Web Dashboard    │
                  │                     │
                  │ HTML + CSS + JS     │
                  │                     │
                  │ Live Monitoring     │
                  │ Decision Status     │
                  └─────────────────────┘
````

---

## ⚙️ Hardware Used

| Component  | Purpose                              |
| ---------- | ------------------------------------ |
| ESP32      | Main microcontroller                 |
| PIR Sensor | Occupancy / motion detection         |
| LDR Module | Ambient light measurement            |
| DHT11      | Temperature and humidity measurement |
| LED        | Temporary lighting load / indicator  |
| Resistor   | LED current limiting                 |

---

## 🔌 Pin Configuration

| Component  | ESP32 Pin |
| ---------- | --------- |
| PIR OUT    | GPIO 27   |
| LDR AO     | GPIO 34   |
| DHT11 DATA | GPIO 4    |
| LED        | GPIO 5    |

### Power Connections

* PIR → 3.3V / GND
* LDR → 3.3V / GND
* DHT11 → 3.3V / GND
* LED → GPIO 5 through 220–330Ω resistor

---

## 💻 Software Technologies

### Embedded

* Arduino IDE
* Embedded C/C++
* ESP32
* Sensor interfacing

### Backend

* Python
* Flask
* PySerial
* REST API
* JSON

### Frontend

* HTML
* CSS
* JavaScript

---

## 📊 Data Flow

The ESP32 continuously reads the sensors and sends data through serial communication.

Example:

```text
1,389,30.6,55.8,1,1
```

The values represent:

```text
PIR, LDR, Temperature, Humidity, Lighting, Cooling
```

Example interpretation:

```text
PIR          → 1
LDR          → 389
Temperature  → 30.6 °C
Humidity     → 55.8 %
Lighting     → ON
Cooling      → REQUIRED
```

---

## 🤖 Decision Logic

### Lighting

The system considers:

* Occupancy
* Ambient light level

If a person is detected and the environment is sufficiently dark:

```text
Occupancy detected
        +
Low light
        ↓
   Lighting ON
```

Otherwise:

```text
Lighting OFF
```

### Cooling

Temperature is monitored continuously.

If:

```text
Temperature ≥ 30 °C
```

the system marks:

```text
Cooling REQUIRED
```

Otherwise:

```text
Cooling NOT REQUIRED
```

---

## 🌐 Web Dashboard

The dashboard provides live information about:

* Occupancy
* Temperature
* Humidity
* Light level
* Lighting status
* Cooling status
* ESP32 connection status
* Last update time

The dashboard communicates with the Flask backend through:

```text
/api/data
```

Example JSON response:

```json
{
    "temperature": 30.5,
    "humidity": 55.9,
    "ldr": 385,
    "occupancy": true,
    "lighting": true,
    "cooling": true,
    "system": "ONLINE"
}
```

---



---

## ▶️ How to Run

### 1. Upload the ESP32 Firmware

Open the Arduino firmware in Arduino IDE.

Select the appropriate ESP32 board and COM port.

Upload the program.

Set the Serial Monitor baud rate to:

```text
115200
```

---

### 2. Install Python Dependencies

Open the project terminal and run:

```bash
pip install flask pyserial
```

---

### 3. Check the Serial Port

Make sure the ESP32 is connected to the correct COM port.

The current configuration uses:

```python
SERIAL_PORT = "COM3"
BAUD_RATE = 115200
```

Change `COM3` if your ESP32 appears on another port.

---

### 4. Start the Flask Server

Run:

```bash
python app.py
```

You should see:

```text
ESP32 connected!
```

and live sensor data such as:

```text
ESP32: 1,389,30.6,55.8,1,1
```

---

### 5. Open the Dashboard

Open the local Flask address shown in the terminal, typically:

```text
http://127.0.0.1:5000
```

The dashboard will update automatically every 2 seconds.

---

## 🔬 Current Prototype

The current prototype demonstrates:

✅ ESP32 sensor integration
✅ PIR-based occupancy detection
✅ LDR-based light monitoring
✅ DHT11 temperature and humidity monitoring
✅ Automatic lighting decision
✅ Temperature-based cooling decision
✅ ESP32-to-PC serial communication
✅ Python Flask backend
✅ JSON API
✅ Live web dashboard
✅ Online/offline system status

---

## 🚀 Future Improvements

Possible future development includes:

* Relay-controlled real electrical loads
* Multiple rooms / zones
* Energy consumption monitoring
* Current and voltage sensing
* Additional environmental sensors
* Local data logging
* Historical graphs
* Mobile-friendly interface
* User authentication
* MQTT-based communication
* Edge-based decision making
* Multi-node campus deployment

---

## 🎯 Project Objective

The objective of Astra Grid is to demonstrate how **embedded systems, IoT sensing, local decision-making, and web technologies** can be integrated to create a practical smart-campus automation platform.

---

## 👩‍💻 Developed By

**Srimathi S**
2nd Year – Electronics and Communication Engineering
Sri Ramakrishna Engineering College, Coimbatore

---
