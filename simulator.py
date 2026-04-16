#Generated with the assistance of AI Gemini

import os
import time
import json
import random
from datetime import datetime, timezone
from threading import Thread
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

# 1. Load environment variables from .env file
load_dotenv()

# Get connection strings for three devices
CONNECTION_STRINGS = {
    "DowsLake": os.getenv("DOWS_LAKE_CS"),
    "FifthAvenue": os.getenv("FIFTH_AVENUE_CS"),
    "NAC": os.getenv("NAC_CS")
}

def simulate_sensor(location_name, connection_string):
    """
    Function to simulate a single sensor device
    """
    if not connection_string:
        print(f"❌ Error: Connection String for {location_name} not found. Please check your .env file.")
        return

    try:
        # Create IoT Hub client and connect
        client = IoTHubDeviceClient.create_from_connection_string(connection_string)
        client.connect()
        print(f"✅ [{location_name}] Successfully connected to Azure IoT Hub!")

        while True:
            # 2. Generate simulated data (ice thickness, temperature, etc.)
            payload = {
                "location": location_name,
                "timestamp": datetime.now(timezone.utc).isoformat(),  # ISO format UTC time
                "ice_thickness": round(random.uniform(20.0, 40.0), 1),  # 20cm to 40cm
                "surface_temperature": round(random.uniform(-10.0, 2.0), 1),  # -10°C to 2°C
                "snow_accumulation": round(random.uniform(0.0, 15.0), 1),  # 0cm to 15cm
                "external_temperature": round(random.uniform(-15.0, 0.0), 1)  # -15°C to 0°C
            }

            # 3. Convert dictionary to JSON string and wrap as Message
            msg_str = json.dumps(payload)
            msg = Message(msg_str)
            msg.content_encoding = "utf-8"
            msg.content_type = "application/json"

            # 4. Send message
            client.send_message(msg)
            print(f"📤 [{location_name}] Data sent: {msg_str}")

            # 5. Wait 10 seconds before sending next message (project requirement)
            time.sleep(10)

    except Exception as e:
        print(f"❌ [{location_name}] Error occurred: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting Rideau Canal Sensor Simulator...")
    print("Press Ctrl+C to stop\n")

    threads = []
    
    # Start a separate thread for each location
    for location, cs in CONNECTION_STRINGS.items():
        t = Thread(target=simulate_sensor, args=(location, cs))
        t.daemon = True  # Allow threads to exit when main program exits
        t.start()
        threads.append(t)

    # Keep main program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Simulator stopped manually.")
