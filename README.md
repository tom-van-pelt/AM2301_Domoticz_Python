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
pip3 install numbers
cd
git clone https://github.com/tom-van-pelt/AM2301_Domoticz_Python.git
```
