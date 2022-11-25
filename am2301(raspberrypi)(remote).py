import time
import board
import adafruit_dht
import sys
import numbers
import requests

#change data here / verander data hieronder:
dhtDevice = adafruit_dht.DHT22 (board.D4, use_pulseio=False) #board.D<number> where <number> is GPIO pin | use_pulsio = false>
domoticz_sensor_idx = 15 #change to dummy sensor idx (Temp+Hum idx)
printData = False #change to False if you don't want to print information to console
username = ''
password = ''
ipAddress = ''
port = ''

# ================================================================================================================

readSensor = True

while readSensor:
    try:
        temperature_c, humidity = 0, 0
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if isinstance (temperature_c, numbers.Number) and isinstance (humidity, numbers.Number):
            url = "http://" + ipAddress + ":" + port + "/json.htm?type=command&param=udevice&idx=" + str (domoticz_sensor_idx) + "&nvalue=0&svalue=" + str (temperature_c) + ";" + str (humidity) + ";0"
            print ("Url:", url)
            response = requests.get (url, auth = (username, password)).content

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
                
