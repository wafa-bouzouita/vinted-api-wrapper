from datetime import datetime, timezone
from pyVinted.requester import requester


class Item:
    def __init__(self, data):
        self.raw_data = data
        self.id = data["id"]
        self.title = data["title"]
        self.brand_title = data["brand_title"]
        try:
            self.size_title = data["size_title"]
        except:
            self.size_title = 'N/A'
        self.currency = data["currency"]
        self.price = data["price"]
        self.description = data["description"]
        self.status = data["status"]
        try:
            self.photo = data["photo"]["url"]
        except:
            self.photo = 'N/A'
        self.url = data["url"]
        self.created_at_ts = datetime.fromtimestamp(
            data["photo"]["high_resolution"]["timestamp"], tz=timezone.utc
        )
        self.raw_timestamp = data["photo"]["high_resolution"]["timestamp"]

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(('id', self.id))

    def isNewItem(self, minutes=3):
        delta = datetime.now(timezone.utc) - self.created_at_ts
        return delta.total_seconds() < minutes * 60

