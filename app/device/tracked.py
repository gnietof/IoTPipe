import json

from app.device.device import Device


class Tracked(Device):
    def __init__(self, id:str, path: str, endpoint: str, mode: str = "http", interval: int = 60, broker: str = "test.mosquitto.org"):
        Device.__init__(self, endpoint, mode, interval, broker)

        self.data = self.load_points(path)
        self.id = id

    def load_points(self,path:str) -> list:
        with open(path, 'r') as f:
            geojson = json.load(f)

        # for feature in data['features']:
        #     yield feature

        features = geojson['features']
        feature = features[2]
        geometry = feature['geometry']
        coordinates = geometry['coordinates']

        return iter(coordinates)

    def get_payload(self) -> dict | None:
        try:
            data = next(self.data)
            
            payload = {
                "id": self.id,
                "longitude": data[0],
                "latitude": data[1],
                "altitude": data[2]
            }
            return payload
        except StopIteration:
            return None

