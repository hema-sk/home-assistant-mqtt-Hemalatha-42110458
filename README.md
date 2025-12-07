# Home Assistant - MQTT Assignment  
Student name: **Hemalatha G**
Register Number: **42110458**  
Topic Used: **home/hemalatha-2025/sensor**

This repository contains my MQTT, Python, Home Assistant assignment for **Nakshatra Automation**

## Task Overview
### Task 1 - Home Assistant Installation  
Home Assistant OS was installed using **VirtualBox**.  
The VM boots successfully and HA is accessible through the browser.

# Task 2 - MQTT Broker Installation  
The **Mosquitto MQTT Broker** was installed on the local system.  
The broker runs on port **1883**, and authentication is enabled.

# Task 3 - Python Script (MQTT Publisher)  
A Python program (`sensor_publish.py`) publishes the following sensor values:
- Temperature = **25**
- Humidity = **60**
- Light = **200**
- Sound = **50** (extra sensor chosen by me)

The script publishes data to the topic:  
`home/hemalatha-2025/sensor`

The script includes:
- `student_name`
- `unique_id`
- `topic` 

# Task 4 - Home Assistant Dashboard  
HA listens to the MQTT topic and displays the sensor values live.

### Task 5 - Demo Video  
The submitted video shows:
- My face (verification)
- Real-time timestamp  
- Home Assistant dashboard  
- Python script output  
- MQTT broker with live data

# Task 6 - GitHub Upload  
This repo contains:
- Python script  
- README documentation  

### Task 7 - PDF  
Includes:
- Name  
- Register Number  
- MQTT Topic  
- Extra Sensor Explanation  
- Steps followed  

## How to Run the Script
pip install paho-mqtt
python sensor_publish.py
The program publishes values every **5 seconds**.


## Extra Sensor Chosen: SOUND  
I selected **sound level** as the extra sensor.  
It simulates environmental noise for smart home monitoring.


## Summary  
This project demonstrates:
- MQTT understanding  
- Python MQTT client  
- Mosquitto broker setup  
- Home Assistant integration  
- Sensor visualization  

All tasks were completed individually as per the assignment rules.

