from classes.snippets.component import Component

class Motor(Component):
    def __init__(self, nominal_voltage: float = 5.0, max_current: float = 12.0):
        super().__init__()
        self.nominal_voltage = nominal_voltage
        self.max_current = max_current

        self.__speed = 0.0
        self.__torque = 0.0
        self.__is_rotating = False

    def update_state(self):
        if self.is_burned:
            self.stop()
            return

        if self.input_current <= 0:
            self.stop()
            return

        if self.input_current > self.max_current:
            self.burn()
            self.stop()
            return

        self.__is_rotating = True
        self.__speed = (self.input_current / self.nominal_voltage) * 1000
        self.__torque = self.input_current * 0.3

    def stop(self):
        self.__is_rotating = False
        self.__speed = 0.0
        self.__torque = 0.0

    def fix(self):
        self.is_burned = False

    @property
    def speed(self):
        return self.__speed

    @property
    def torque(self):
        return self.__torque

    @property
    def is_rotating(self):
        return self.__is_rotatingfrom classes.snippets.component import Component

class Motor(Component):
    def __init__(self, nominal_voltage: float = 5.0, max_current: float = 12.0):
        super().__init__()
        self.nominal_voltage = nominal_voltage
        self.max_current = max_current

        self.__speed = 0.0
        self.__torque = 0.0
        self.__is_rotating = False

    def update_state(self):
        if self.is_burned:
            self.stop()
            return

        if self.input_current <= 0:
            self.stop()
            return

        if self.input_current > self.max_current:
            self.burn()
            self.stop()
            return

        self.__is_rotating = True
        self.__speed = (self.input_current / self.nominal_voltage) * 1000
        self.__torque = self.input_current * 0.3

    def stop(self):
        self.__is_rotating = False
        self.__speed = 0.0
        self.__torque = 0.0

    def fix(self):
        self.is_burned = False

    @property
    def speed(self):
        return self.__speed

    @property
    def torque(self):
        return self.__torque

    @property
    def is_rotating(self):
        return self.__is_rotating