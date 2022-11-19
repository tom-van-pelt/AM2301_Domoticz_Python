# AM2301 on Raspberry Pi to Domoticz (Python)

A Python 3 script to send data from AM2301 Temperature + Humidity sensor to Domoticz Dummy sensor.
## Used websites to write this script: 
- https://www.sigmdel.ca/michel/ha/rpi/temp_sensor_en.html
- https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup

## Execute following commands:
```
sudo apt update
sudo apt upgrade
pip3 install adafruit-circuitpython-dht
sudo apt install libgpiod2
pip3 install urllib3
cd
git clone https://github.com/tom-van-pelt/AM2301_Domoticz_Python.git
```
## Change Python file parameters
There are 2 parameters to be configured before use.
```
cd AM2301_Domoticz_Python
nano am2301.py
```
- Line 9: GPIO pin number has to be changed to the GPIO pin where the signal wire of the AM2301 sensor is connected. Default is GPIO pin 4.\
Example: Signal wire connected to GPIO Pin 18. In Python script (line 9):\
```dhtDevice = adafruit_dht.DHT22 (board.D18, use_pulsio=False)```

- Line 10: Change number behind ```domoticz_sensor_idx``` to idx number of the dummy 'Temp+Hum'-sensor in Domoticz.

Save the file with ```Ctrl + S``` and close the file with ```Ctrl + X```.

## Use crontab to run the script every minute: 
```
crontab -e
```
Select an editor if this is the first time using crontab (nano (1) is recommended).
### Enter the following lines add the end of the opened crontab file:
```
#Read out am2301 sensor every minute and send data to Domoticz
* * * * * /usr/bin/python3 /home/<username>/AM2301_Domoticz_Python/am2301.py
```
IMPORTANT: Replace ```<username>``` with the username of the system.\
TIP: To get the current username, use: ```echo $USER```.
