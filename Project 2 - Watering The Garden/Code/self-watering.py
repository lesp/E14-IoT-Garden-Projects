
#!/usr/bin/python3
from gpiozero import MCP3008, DigitalOutputDevice
import time

soil = MCP3008(channel=0)
relay = DigitalOutputDevice(17)

while True:
    soil_check = round(soil.value,2)
    print('The wetness of the soil is',soil_check)
    time.sleep(1)
    if soil_check <= 0.1:
        relay.on()
        time.sleep(2)
        relay.off()
        time.sleep(10)
