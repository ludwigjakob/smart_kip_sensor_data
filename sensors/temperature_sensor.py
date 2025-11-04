import glob
import time
from sensors.base_sensor import BaseSensor

class DeboTempSensor(BaseSensor):
    def __init__(self, name="debo_temp_1", bucket="temp_bucket"):
        super().__init__(name, bucket)
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def read(self):
        with open(self.device_file, 'r') as f:
            lines = f.readlines()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            with open(self.device_file, 'r') as f:
                lines = f.readlines()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return {
                "sensor": self.name,
                "type": "temperature",
                "value": round(temp_c, 2)
            }
