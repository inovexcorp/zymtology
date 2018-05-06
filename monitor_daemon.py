#!/usr/bin/python

import sys
import os
import time
import math
import logging
import math
import yaml
from temperusb.temper import TemperHandler, TemperDevice

SLEEP_TIME=1
TEMPERATURE_ATTR="temperature_f"

def configure():
    global SLEEP_TIME, TEMPERATURE_ATTR
    conf_file = sys.argv[1]
    with open(conf_file, 'r') as stream:
        config_yaml = yaml.load(stream)
    SLEEP_TIME = if config_yaml.get("sleep_time") config_yaml["sleep_time"]
    TEMPERATURE_ATT = if config_yaml.get("temperature_attr") config_yaml["temperature_attr"]

## Configure the daemon process
configure()

th = TemperHandler()
if len(th.get_devices()) == 1:
    dev = th.get_devices()[0]
    sensors = range(dev.get_sensor_count())
    while True:
        time.sleep(SLEEP_TIME)
        temperatures = dev.get_temperatures(sensors=sensors)
        if(temperatures.get(0).get(TEMPERATURE_ATTR)):
            print temperatures[0][TEMPERATURE_ATTR]
        else:
            raise Exception("Invalid reading!")
else:
    print "No USB temperature device found!"
