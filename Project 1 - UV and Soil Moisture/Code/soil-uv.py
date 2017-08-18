
#!/usr/bin/python3
"""
This code uses the Python_SI1145 Library written by Joe Gutting.
You can read more about this great library by visiting.

https://github.com/THP-JOE/Python_SI1145

"""
from gpiozero import MCP3008
import time
import SI1145.SI1145 as SI1145
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sensor = SI1145.SI1145()
soil = MCP3008(channel=0)

while True:
    UV = sensor.readUV()
    uvIndex = UV / 100.0
    print('UV Index:        ' + str(uvIndex))
    soil_check = round(soil.value,2)
    print('The wetness of the soil is',soil_check)
    time.sleep(1)
    if soil_check <= 0.1:
        fromaddr = "YOUR EMAIL ADDRESS"
        toaddr = "EMAIL ADDRESS TO SEND TO"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = 'Garden requires water'
        readings = 'Soil is '+str(soil_check)+'wet and the UV index is '+str(uvIndex)
        body = readings
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "PASSWORD")
        text = msg.as_string()
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        time.sleep(10)

