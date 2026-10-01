from flask import Flask, render_template, jsonify
import serial
import threading
import time

app = Flask(__name__)

# =====================================
# ESP32 SERIAL SETTINGS
# =====================================

SERIAL_PORT = "COM3"
BAUD_RATE = 115200


# =====================================
# SENSOR DATA
# =====================================

sensor_data = {
    "temperature": 0,
    "humidity": 0,
    "ldr": 0,
    "occupancy": False,
    "lighting": False,
    "cooling": False,
    "system": "WAITING"
}


# =====================================
# READ ESP32 DATA
# =====================================

def read_esp32():

    global sensor_data

    while True:

        try:

            print("Connecting to ESP32...")

            esp32 = serial.Serial(
                SERIAL_PORT,
                BAUD_RATE,
                timeout=2
            )

            time.sleep(2)

            print("ESP32 connected!")

            sensor_data["system"] = "ONLINE"

            while True:

                line = esp32.readline().decode(
                    "utf-8",
                    errors="ignore"
                ).strip()

                if not line:
                    continue

                print("ESP32:", line)

                # Ignore startup message
                if line == "ASTRA_GRID_READY":
                    continue

                values = line.split(",")

                # Only process valid sensor data
                if len(values) != 6:
                    continue

                try:

                    pir = int(values[0])
                    ldr = int(values[1])
                    temperature = float(values[2])
                    humidity = float(values[3])
                    lighting = int(values[4])
                    cooling = int(values[5])

                except ValueError:

                    # Ignore ESP32 boot/debug messages
                    continue


                # =====================================
                # UPDATE SENSOR DATA
                # =====================================

                sensor_data["occupancy"] = (
                    pir == 1
                )

                sensor_data["ldr"] = ldr

                sensor_data["temperature"] = temperature

                sensor_data["humidity"] = humidity

                sensor_data["lighting"] = (
                    lighting == 1
                )

                sensor_data["cooling"] = (
                    cooling == 1
                )

                sensor_data["system"] = "ONLINE"


        except Exception as error:

            print("ESP32 connection error:", error)

            sensor_data["system"] = "OFFLINE"

            time.sleep(3)


# =====================================
# DASHBOARD
# =====================================

@app.route("/")
def dashboard():

    return render_template("dashboard.html")


# =====================================
# API
# =====================================

@app.route("/api/data")
def get_data():

    return jsonify(sensor_data)


# =====================================
# START
# =====================================

if __name__ == "__main__":

    serial_thread = threading.Thread(
        target=read_esp32,
        daemon=True
    )

    serial_thread.start()

    app.run(
        debug=False,
        use_reloader=False
    )