# Rideau Canal Sensor Simulation

This repository contains the Python-based IoT sensor simulation for the Rideau Canal Skateway real-time monitoring project. It acts as the data generation layer, simulating telemetry data from three key locations along the canal.

## Features
* Simulates three IoT devices concurrently using Python's `threading` library (Dow's Lake, Fifth Avenue, NAC).
* Generates realistic real-time telemetry data within specified project ranges:
  * Ice Thickness (20.0 - 40.0 cm)
  * Surface Temperature (-10.0 - 2.0 °C)
  * Snow Accumulation (0.0 - 15.0 cm)
  * External Temperature (-15.0 - 0.0 °C)
* Packages data into JSON format and transmits it to Azure IoT Hub exactly every 10 seconds.

## Prerequisites
* Python 3.8 or higher
* An active Azure IoT Hub with three registered devices

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Shan-AC/rideau-canal-sensor-simulation.git](https://github.com/Shan-AC/rideau-canal-sensor-simulation.git)
   cd rideau-canal-sensor-simulation
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration:**
   Rename `.env.example` to `.env` (or create a new `.env` file) and replace the placeholder strings with your actual Azure IoT Hub Primary Connection Strings.
   *Note: The `.env` file is included in `.gitignore` to prevent exposing sensitive credentials.*

## Usage

Start the simulator by running:
```bash
python sensor_simulator.py
```
You should see console output indicating successful connections and continuous data transmission for all three locations. Press `Ctrl+C` to stop the simulation.

## AI Usage Disclosure
*As per course requirements, I declare that Generative AI (Gemini) was utilized to assist in writing the Python threading logic, generating the randomized dataset ranges, and formatting this README documentation.*