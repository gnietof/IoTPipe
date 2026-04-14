import logging
import os

from app.device.mock import MockDevice
from app.device.tracked import Tracked
from app.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
    
if __name__ == "__main__":
    # Mock device which just sends a random temperature
    # device = MockDevice(
    #     endpoint=settings.ENDPOINT,
    #     interval=10,
    #     broker=settings.BROKER,
    #     mode=os.getenv("MODE", "http")
    # )
    # Mock device which sends coordinates and altitude from a real flight
    device = Tracked(
        path="/home/genaro/Documents/FlightAware_LVL230K_KMIA_LEBL_20260413.geojson",
        endpoint=settings.ENDPOINT,
        interval=10,
        broker=settings.BROKER,
        mode=os.getenv("MODE", "http")
    )

    try:
        device.start()
    except KeyboardInterrupt:
        device.stop()
        logger.info("Exited cleanly.")