import json
import time
from sensors.temperature_sensor import DeboTempSensor
from influx.influx_writer import InfluxWriter

def load_sensors():
    with open("config.json") as f:
        config = json.load(f)
    sensors = []
    for entry in config["sensors"]:
        if entry["class"] == "DeboTempSensor":
            sensors.append(DeboTempSensor(entry["name"], entry["bucket"]))
        # Weitere Sensoren hier ergänzen
    return sensors

def main():
    sensors = load_sensors()
    influx = InfluxWriter()

    while True:
        for sensor in sensors:
            data = sensor.read()
            print(f"{data['sensor']} → {data['value']}°C → {sensor.bucket}")
            influx.write(sensor.bucket, data)
        time.sleep(10)

if __name__ == "__main__":
    main()
