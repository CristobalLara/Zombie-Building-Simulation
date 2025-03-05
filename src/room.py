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
        state = "☠️" if self.has_zombies else "✅"
        return f"Room {self.room_number}: {state} (Sensor: {self.sensor.state})"
    
    def to_dict(self):
        return {
            "has_zombies": self.has_zombies,
            "blocked": self.blocked,
            "stairs": self.stairs
        }

    def from_dict(self, data: dict):
        self.has_zombies = data.get("has_zombies", False)
        self.blocked = data.get("blocked", False)
        self.stairs = data.get("stairs", False)
        return self