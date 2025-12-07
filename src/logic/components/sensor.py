from classes.snippets.component import Component

class Sensor(Component):
    def __init__(self, sensor_type: str = "generic", unit: str = ""):
        super().__init__()
        self.__type = sensor_type
        self.__value = 0.0
        self.__unit = unit

    def read(self):
        return f"{self.__value} {self.__unit}"

    def set_value(self, value: float):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def unit(self):
        return self.__unit

    @property
    def sensor_type(self):
        return self.__type