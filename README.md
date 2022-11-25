# AM2301 to Domoticz (Python)

A Python 3 script to send data from AM2301 Temperature + Humidity sensor to Domoticz Dummy sensor.
### Used websites to write this script: 
- https://www.sigmdel.ca/michel/ha/rpi/temp_sensor_en.html
- https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup
- https://github.com/jingl3s/DHT11-DHT22-Python-library-Orange-PI

## Raspberry Pi 3(B+) or Raspberry Pi 4(B+)
Use below tutorial to read the AM2301 sensor on a Raspberry Pi and send the data to Domoticz.

### First execute following commands:
```
sudo apt update
sudo apt upgrade
pip3 install --upgrade pip
pip3 install adafruit-circuitpython-dht
sudo apt install libgpiod2
pip3 install urllib3
pip3 install requests
cd
git clone https://github.com/tom-van-pelt/AM2301_Domoticz_Python.git
```
### Change Python file parameters
There are 2 parameters to be configured before use.
```
cd AM2301_Domoticz_Python
nano am2301(raspberrypi)(local).py
```
- Line 9: GPIO pin number has to be changed to the GPIO pin where the signal wire (yellow) of the AM2301 sensor is connected. Default is GPIO pin 4.\
Example: Signal wire connected to GPIO Pin 18. In Python script (line 9):\
```dhtDevice = adafruit_dht.DHT22 (board.D18, use_pulsio=False)```

- Line 10: Change number behind ```domoticz_sensor_idx``` to idx number of the dummy 'Temp+Hum'-sensor in Domoticz.

Save the file with ```Ctrl + S``` and close the file with ```Ctrl + X```.

## Orange Pi Zero (H2+)
Use below tutorial to read the AM2301 sensor on an Orange Pi Zero H2+ and send the data to Domoticz.

### First execute following commands:
```
sudo apt update
sudo apt upgrade
pip3 install --upgrade pip
pip3 install urllib3
pip3 install requests
cd
git clone https://github.com/tom-van-pelt/AM2301_Domoticz_Python.git
```
### Change Python file parameters
There are 2 parameters to be configured before use.
```
cd AM2301_Domoticz_Python
nano am2301(orangepi)(remote).py
```
- Line 12: GPIO pin number has to be changed to the GPIO pin where the signal wire (yellow) of the AM2301 sensor is connected.\
Example: Signal wire connected to GPIO Pin UART1_RX/PG07. In Python script:\
```dhtDevice = port.PG7```

- Line 13: Change number behind ```domoticz_sensor_idx``` to idx number of the dummy 'Temp+Hum'-sensor in Domoticz.

Save the file with ```Ctrl + S``` and close the file with ```Ctrl + X```.

# Use crontab to run the script every minute: 
```
crontab -e
```
Select an editor if this is the first time using crontab (nano (1) is recommended).
### Enter the following lines add the end of the opened crontab file:
```
#Read out am2301 sensor every minute and send data to Domoticz
* * * * * /usr/bin/python3 /home/<username>/AM2301_Domoticz_Python/<filename>
```
IMPORTANT: Replace ```<username>``` with the username of the system and ```<filename>``` with the python file to use (what you should have configured).\
TIP: To get the current username, use: ```echo $USER```.
