class Sensor:
    def __init__(self):
        self.state = 'normal'

    def set_alert(self):
        self.state = 'alert'

    def reset(self):
        self.state = 'normal'

    # Métodos para guardar y cargar el estado del sensor
    def to_dict(self):
        return {
            "state": self.state
        }

    def from_dict(self, data: dict):
        self.state = data.get("state", "normal")
        return self
