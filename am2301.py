import time
import board
import adafruit_dht
import sys
import urllib.request
import numbers

#change data here / verander data hieronder:
dhtDevice = adafruit_dht.DHT22 (board.D4, use_pulseio=False) #board.D<number> where <number> is GPIO pin | use_pulsio = false for Raspberry Pi
domoticz_sensor_idx = 7 #change to dummy sensor idx (Temp+Hum idx)
printData = True #change to False if you don't want to print information to console
update_interval = 60.0 #seconds | standard 60 seconds

# ================================================================================================================

#make sure 127.0.0.1 is local IP-address in Domoticz (Setup -> Settings -> Local Networks)
url_json = "http://127.0.0.1:8080/json.htm?type=command&param=udevice&idx="

while True:
    try:
        temperature_c, humidity = 0, 0
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if isinstance (temperature_c, numbers.Number) and isinstance (humidity, numbers.Number):
            cmd = url_json + str (domoticz_sensor_idx) + "&nvalue=0&svalue=" + str (temperature_c) + ";" + str (humidity) + ";0"
            print ("Url:", cmd)
            send_data = urllib.request.urlopen (cmd)

            # Print the values to the serial port
            if printData:
                print ("Temp: {:.1f} C | Humidity: {}% ".format(temperature_c, humidity))
                print ("Domoticz response:", send_data.read ())

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print (error.args[0])
        time.sleep (1.0)
        continue

    except Exception as error:
        dhtDevice.exit ()
        raise error

    #update interval (seconds)
    time.sleep (update_interval)
