#!/usr/bin/python

import sys
import os
import time
import math
import logging
import math
import yaml
import requests
from temperusb.temper import TemperHandler, TemperDevice

SLEEP_TIME=1
TEMPERATURE_ATTR="temperature_f"

## Function to configure the daemon process.
def configure():
    global SLEEP_TIME, TEMPERATURE_ATTR
    conf_file = sys.argv[1]
    with open(conf_file, 'r') as stream:
        config_yaml = yaml.load(stream)
    SLEEP_TIME = config_yaml["sleep_time_seconds"]
    TEMPERATURE_ATTR = config_yaml["temperature_attr"]

def report(reading):
    print reading[TEMPERATURE_ATTR]




## Configure the daemon process
configure()

th = TemperHandler()
## There is a device discovered by the TemerHandler
if len(th.get_devices()) == 1:
    dev = th.get_devices()[0]
    sensors = range(dev.get_sensor_count())
    while True:
        temperatures = dev.get_temperatures(sensors=sensors)
        if(temperatures.get(0).get(TEMPERATURE_ATTR)):
            report(temperatures[0])
        else:
            raise Exception("Invalid reading!")
        time.sleep(SLEEP_TIME)
## No devices found...
else:
    print "No USB temperature device found!"
