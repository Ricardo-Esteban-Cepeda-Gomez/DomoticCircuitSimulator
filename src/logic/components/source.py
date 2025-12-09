from logic.components.component import Component

class Source(Component):
    def __init__(self):
        super().__init__()
        self.__type = "DC"
        self.current = 0.0
        self.voltage = 0.0