# IoTPipe
This is an exercise to create a (mock) IoT infrastructure including:
- One or more brokers receiving information from remote devices.
- One NGINX server for load balancing among all the brokers.
- One or more (mock)devices.

# Code & Docker images
All the code (broker and devices) is part of a single project. When building the Docker image file, the Docker compose generates two different images with different commands.

# Mock Device
This is a completely mock device which generates a random temperature value and a timestamp.

# Tracked Device
The tracked device is slightly more complex because the information is being retrieved from a GeoJSON device. In this case, latitude, longitude and altitude are retrieved from a GeoJSON file and sent one sample every few seconds. 
The GeoJSON file used belongs to a real flight. But because the position timestamps were lost when converting from KML to GeoJSON, there is no option to provide speed or real time spacing between each of the points.

## Configuration file
This project requires a configuration file with these values:

'''
ENDPOINT="http://localhost:9000/data"
#ENDPOINT="http://host.docker.internal:9000/data"
BROKER="test.mosquitto.org"
TOPIC="gnf/devices/data"
'''

The ENDPOINT using host.docker.internal is required when using Docker to run the application so that the devices can communicate with the broker if using the HTTP protocol.
This broker does not require credentials and might be replaced with any other broker.
Finally the TOPIC can be replaced with any other topic. 


Picture shows running in 'temperature mode' with two brokers and one device in HTTP mode.
<img width="1233" height="691" alt="image" src="https://github.com/user-attachments/assets/ba2e62ff-a0ef-4021-913d-6f33d16f8684" />

Picture shows running in 'temperature mode' with two brokers and one device in MQTT mode.
<img width="1238" height="563" alt="image" src="https://github.com/user-attachments/assets/1765f52f-66dc-43d3-93b0-1c3be78eab11" />

Picture shows running in 'temperature mode' with two brokers and two devices one in HTTP mode and one in MQTT mode.
<img width="1250" height="670" alt="image" src="https://github.com/user-attachments/assets/c3d9bca3-f7c9-44fe-81c2-67d4aad78878" />

Picture shows running in 'tracking mode' with two brokers and one device in MQTT mode.
<img width="1100" height="559" alt="image" src="https://github.com/user-attachments/assets/ea51cad8-7dfb-4eba-8e36-a74b8c5eb9f9" />


