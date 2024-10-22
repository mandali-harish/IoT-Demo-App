import paho.mqtt.client as mqtt
import time
import random
import socket
import os


# MQTT broker settings
MQTT_BROKER = os.getenv('MQTT_BROKER', 'test.mosquitto.org')
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
MQTT_TOPIC = os.getenv('MQTT_TOPIC', 'sensor/temperature')

# Create MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Connected successfully to {MQTT_BROKER}")
    else:
        print(f"Connection failed with code {rc}")

client.on_connect = on_connect

try:
    # Attempt to resolve the hostname
    print(f"Attempting to resolve {MQTT_BROKER}")
    ip_address = socket.gethostbyname(MQTT_BROKER)
    print(f"Resolved {MQTT_BROKER} to {ip_address}")

    # Connect to the broker
    print(f"Connecting to {MQTT_BROKER}:{MQTT_PORT}")
    client.connect(MQTT_BROKER, MQTT_PORT)

    # Start the loop
    client.loop_start()

    # Publish data indefinitely
    while True:
        temperature = random.uniform(20.0, 30.0)
        result = client.publish(MQTT_TOPIC, f"{temperature:.2f}")
        if result.rc == 0:
            print(f"Published: {temperature:.2f}")
        else:
            print(f"Failed to publish message: {result.rc}")
        time.sleep(5)

except KeyboardInterrupt:
    print("Interrupted by user, shutting down...")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    client.loop_stop()
    client.disconnect()
    print("Disconnected from broker")
