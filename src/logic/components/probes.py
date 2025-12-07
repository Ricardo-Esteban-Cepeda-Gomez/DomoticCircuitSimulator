from classes.snippets.component import Component

class Probes(Component):
    def __init__(self, mode: str = "voltage"):
        super().__init__()
        self.__mode = mode
        self.__value = 0.0
        self.__is_connected = False

    def connect(self):
        self.__is_connected = True

    def disconnect(self):
        self.__is_connected = False
        self.__value = 0.0

    def set_mode(self, mode: str):
        self.__mode = mode

    def measure(self, component: Component):
        if not self.__is_connected or component.is_burned:
            self.__value = 0.0
            return

        if self.__mode == "voltage":
            self.__value = getattr(component, "voltage_drop", 0.0)

        elif self.__mode == "current":
            self.__value = getattr(component, "current_flow", 0.0)

        elif self.__mode == "resistance":
            self.__value = getattr(component, "resistance", 0.0)

    @property
    def value(self):
        return self.__value

    @property
    def mode(self):
        return self.__mode

    @property
    def is_connected(self):
        return self.__is_connected