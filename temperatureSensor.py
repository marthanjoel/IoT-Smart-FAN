# -*- coding: utf-8 -*-

# temperatureSensor.py (SIMULATION VERSION - Python2 compatible)
import random

class TemperatureSensor:
    def __init__(self, mode, config):
        self.ready = True
        self.address = config.get("address", "fake")
        self.gpio = config.get("gpio", 0)

    def readValue(self):
        # Simulate a random temperature between 20C and 45C
        temp = round(random.uniform(20, 45), 2)
       # print("[SIM] Sensor at %s (GPIO %s) read %s C" % (self.address, self.gpio, temp))
        return temp

