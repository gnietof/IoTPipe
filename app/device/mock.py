import json
import os
import random

import secrets
import socket
import time
import requests
import logging

import paho.mqtt.client as mqtt

from app.device.device import Device

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MockDevice(Device):
    # def __init__(self, endpoint: str, mode: str = "http", interval: int = 60, broker: str = "test.mosquitto.org"):
    #     Device.__init__(self, endpoint, mode, interval, broker)

    def get_payload (self):
        temp = random.randint(20,30)
        return {
            "temperature": temp,
            "device_id": self.id,
            "timestamp": time.time()
            }


