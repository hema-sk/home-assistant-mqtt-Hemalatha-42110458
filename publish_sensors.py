import paho.mqtt.client as mqtt
import time

student_name = "Hemalatha G."
unique_id = "42110458"
topic = "home/hemalatha-2025/sensor"

broker_address = "192.168.1.6"  
username = "hema2124"
password = "Harinisk@0217"   

client = mqtt.Client(client_id=unique_id)
client.username_pw_set(username, password)
client.connect(broker_address, 1883, 60)


while True:
    temperature = 25
    humidity = 60
    sound = 50  

    payload = (
        f'{{"temperature": {temperature}, '
        f'"humidity": {humidity}, '
        f'"sound": {sound}}}'
    )

    client.publish(topic, payload)
    print("Published:", payload)
    time.sleep(5)
