from .sensor import Sensor

class Room:
    def __init__(self, room_number: int):
        self.room_number = room_number
        self.sensor = Sensor()
        self.has_zombies = False
        self.stairs = False
        self.blocked = False

    def add_zombies(self):
        self.has_zombies = True
        self.sensor.set_alert()

    def remove_zombies(self):
        self.has_zombies = False

    def reset_sensor(self):
        self.sensor.reset()

    def __str__(self):
        if self.sensor.state == "alert":
            state = "☠️" if self.has_zombies else "❗"
        else:
            state = "✅"
        return f"Room {self.room_number}: {state} (Sensor: {self.sensor.state})"

    def to_dict(self):
        return {
            "room_number": self.room_number,
            "has_zombies": self.has_zombies,
            "blocked": self.blocked,
            "stairs": self.stairs,
            "sensor": self.sensor.to_dict()
        }

    def from_dict(self, data: dict):
        self.room_number = data.get("room_number", self.room_number)
        self.has_zombies = data.get("has_zombies", False)
        self.blocked = data.get("blocked", False)
        self.stairs = data.get("stairs", False)
        
        sensor_data = data.get("sensor", {})
        self.sensor.from_dict(sensor_data)
        
        return self