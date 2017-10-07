#!/usr/bin/python3
from gpiozero import DigitalOutputDevice
import time
import paho.mqtt.client as mqtt


relay = DigitalOutputDevice(27)

def on_connect(client, userdata, flags, rc):  
        print("Connected with result code "+str(rc))
        client.subscribe("garden")

def on_message(client, userdata, msg):  
        message = str(msg.payload)
        message = message[2:(len(message)-1)]
        print(message)
        if(message=="water garden"):
                print("Watering Garden")
                relay.on()
                time.sleep(2)
                relay.off()
                time.sleep(10)

client = mqtt.Client()  
client.on_connect = on_connect  
client.on_message = on_message  
client.connect("BROKER IP ADDRESS", 1883, 60)
client.loop_forever() 