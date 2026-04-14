import socket
import threading

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import paho.mqtt.client as mqtt

from app.device.device import Device
import logging

from app.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Broker Service")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
)   

@app.post("/data")
def read_data(payload: dict):
    ''' Process incoming messages through HTTP '''
    id = socket.gethostname()
    logger.info(f"[HTTP] [{id}] {payload}.")
    return {
        "handled_by": id
    }

@app.on_event("startup")
def startup():
    ''' Execute initialization code on startup'''
    thread = threading.Thread(target=start_mqtt, daemon=True)
    thread.start()

def start_mqtt():
    ''' Initialize MQTT client '''
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("test.mosquitto.org", 1883)
    logger.info(f"Subscribing to topic $share/group1/{settings.TOPIC}")
    client.subscribe(f"$share/group1/{settings.TOPIC}")
    client.loop_forever()
    logger.info("MQTT client started.")

def on_message(client, userdata, msg):
    ''' Process incoming messages through MQTT '''
    id = socket.gethostname()
    logger.info(f"[MQTT] [{id}] {msg.payload.decode()}")
    