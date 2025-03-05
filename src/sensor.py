class Sensor:
    def __init__(self):
        self.state = 'normal'

    def set_alert(self):
        self.state = 'alert'

    def reset(self):
        self.state = 'normal'