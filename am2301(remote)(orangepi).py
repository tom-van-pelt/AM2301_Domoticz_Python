from pyA20.gpio import gpio
from pyA20.gpio import port

import dht_orangepizero as dht

import time
import sys
import numbers
import requests

#change data here / verander data hieronder:
dhtDevice = port.PG7 #port.PG<number> where <number> is GPIO pin
domoticz_sensor_idx = 15 #change to dummy sensor idx (Temp+Hum idx)
printData = False #change to False if you don't want to print information to console
username = ''
password = ''
ipAddress = ''
port = ''

# ================================================================================================================

readSensor = True
gpio.init ()
sensor = dht.DHT (pin = dhtDevice)

while readSensor:
    try:
        temperature_c, humidity = 0, 0
        readData = sensor.read ()
        if (readData.is_valid ()):
            temperature_c = readData.temperature
            humidity = readData.humidity
            print ("Temperature:", temperature_c)
            print ("Humidity:", humidity)

            if isinstance (temperature_c, numbers.Number) and isinstance (humidity, numbers.Number):
                url = "http://" + ipAddress + ":" + port + "/json.htm?type=command&param=udevice&idx=" + str (domoticz_sensor_idx) + "&nvalue=0&svalue=" + str (temperature_c) + ";" + str (humidity) + ";0"
                print ("Url:", url)
                #response = requests.get (url, auth = (username, password)).content
                response = request.get (url).content

                # Print the values to the serial port
                if printData:
                    print ("Temp: {:.1f} C | Humidity: {}% ".format(temperature_c, humidity))
                    print ("Domoticz response:", response)

                readSensor = False

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print (error.args[0])
        time.sleep (1.0)
        continue

    except Exception as error:
        dhtDevice.exit ()
        raise error
