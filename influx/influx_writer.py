from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import os
from dotenv import load_dotenv

load_dotenv()  # Lädt Umgebungsvariablen aus .env

class InfluxWriter:
    def __init__(self):
        self.url = os.getenv("INFLUX_URL", "http://localhost:8086")
        self.token = os.getenv("INFLUX_TOKEN", "my-token")
        self.org = os.getenv("INFLUX_ORG", "my-org")
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write(self, bucket: str, data: dict):
        point = (
            Point(data["type"])
            .tag("sensor", data["sensor"])
            .field("value", data["value"])
        )
        self.write_api.write(bucket=bucket, org=self.org, record=point)
