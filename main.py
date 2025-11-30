import json
import time
import signal
import sys
from sensors.temperature_sensor import DeboTempSensor
#from influx.influx_writer import InfluxWriter
from common.data_connector.connector_manager import ConnectorManager

def load_sensors():
    with open("config.json") as f:
        config = json.load(f)
    sensors = []
    for entry in config["sensors"]:
        if entry["class"] == "DeboTempSensor":
            sensors.append(DeboTempSensor(entry["name"], entry["bucket"]))
        # Weitere Sensoren hier ergänzen
    return sensors

def handle_sigint(sig, frame):
    print("\n🛑 Beende sensor data collection...")
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, handle_sigint)
    sensors = load_sensors()
    #influx = InfluxWriter()
    connector_manager = ConnectorManager()

    while True:
        for sensor in sensors:
            data = sensor.read()
            print(f"{data['sensor']} → {data['value']}°C → {sensor.bucket}")
            #influx.write(sensor.bucket, data)
            connector_manager.set("temperature", data)
        time.sleep(10)

if __name__ == "__main__":
    main()
