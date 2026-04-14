import json
import os
import random

import secrets
import socket
import time
import requests
import logging

import paho.mqtt.client as mqtt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Device:
    ''' Common functionality for different device types communication '''

    def __init__(self, endpoint: str, mode: str = "http", interval: int = 60, broker: str = "test.mosquitto.org"):
        self.endpoint = endpoint
        self.broker = broker
        self.mode = mode
        self.interval = interval
        self.running = False
        if self.mode =='mqtt':
            self.client = mqtt.Client()
            self.client.connect(self.broker, 1883)

        self.id = socket.gethostname()
        logger.info(f"Initializing random with ID: {self.id}")
        random.seed(self.id)

    def make_http_request(self, payload: dict):
        ''' Perform a HTTP request'''
        try:
            response = requests.post(f"{self.endpoint}", json=payload, timeout=5)
            logger.info(f"[OK] {response.status_code} - {response.text[:100]}")
        except requests.RequestException as e:
            logger.error(f"[ERROR] {e}")

    def make_mqtt_request(self, payload: dict):
        ''' Perform a MQTT request'''
        try:
            self.client.publish("gnf/devices/temp", json.dumps(payload))
            logger.info(f"[OK] Message [{payload['temperature']}] published to MQTT broker.")
        except Exception as e:
            logger.error(f"[ERROR] {e}")

    def start(self):
        self.running = True
        logger.info("Starting periodic requester...")
        while self.running:
            payload = self.get_payload()
            logger.info(f"Sending payload: {payload}")
            if self.mode=='http':
                self.make_http_request(payload)
            elif self.mode=='mqtt':
                self.make_mqtt_request(payload)
            time.sleep(self.interval)

    def stop(self):
        logger.info("Stopping requester...")
        self.running = False

