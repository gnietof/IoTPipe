import logging
import os

from app.device.mock import MockDevice
from app.device.tracked import Tracked
from app.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
    
if __name__ == "__main__":
    mode = os.getenv("MODE",'http')
    type = os.getenv("TYPE",'temp')
    logger.info(f"Starting a '{type}' device in mode '{mode}'")

    # Mock device which just sends a random temperature
    if type=='temp':  
        device = MockDevice(
            endpoint=settings.ENDPOINT,
            interval=10,
            broker=settings.BROKER,
            mode=os.getenv("MODE", "mqtt")
    )
        
    # Mock device which sends coordinates and altitude from a real flight
    if type=='track':  
        device = Tracked(
            # path="/home/genaro/Documents/FlightAware_LVL230K_KMIA_LEBL_20260413.geojson",
            path=os.getenv("TRACK_PATH"),
            endpoint=settings.ENDPOINT,
            interval=10,
            broker=settings.BROKER,
            mode=mode
        )

    try:
        device.start()
    except KeyboardInterrupt:
        device.stop()
        logger.info("Exited cleanly.")