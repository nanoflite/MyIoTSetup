import paho.mqtt.client as mqtt
import json
import rrdtool

host = "192.168.1.6"
port = 1883
topic = 'dragino/0183FC63/data'
sensor_db = "./db/sensordata.rrd"
client = "record_sensor_data"

def on_connect(client, userdata, flags, rc):
    print("connected...")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("incoming message")
    data = json.loads(msg.payload)
    # {'BatV': 3.588, 'TempC_SHT': 8.1, 'SNR': 9.2, 'EXTI_Trigger': 'FALSE', 'Hum_SHT': 79,
    temperature = data["TempC_SHT"]
    humidity = data["Hum_SHT"]
    battery = data["BatV"]
    print(temperature, humidity, battery)
    rrdtool.update(sensor_db, "N:" + str(float(temperature)) + ":" + str(float(humidity)) + ":" + str(float(battery)))

client = mqtt.Client(client)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port)
client.loop_forever()
