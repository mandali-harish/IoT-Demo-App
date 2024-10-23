# Run the container
docker run -e MQTT_BROKER=test.mosquitto.org -e MQTT_PORT=1883 -e MQTT_TOPIC=sensor/temperature mqtt-publisher
