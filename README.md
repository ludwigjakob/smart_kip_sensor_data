# SmartKIP Sensor Data

Temperature data collection service using DS18B20 sensors, storing values in InfluxDB.

## Features
- Periodic DS18B20 sensor readings
- Write time-series data into InfluxDB
- Provide historical data for analysis and visualization

## Start the app with Docker
```bash
./start.sh
```

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses
This project uses third-party libraries under the following licenses:
- influxdb-client (MIT)
- python-dotenv (BSD-3-Clause)
- mysql-connector-python (GPL-2.0 with FOSS Exception)
