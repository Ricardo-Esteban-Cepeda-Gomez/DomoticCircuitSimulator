from logic.components.component import Component

class Resistor(Component):
    def __init__(self, resistance: float = 100.0, max_power: float = 0.25):
        super().__init__()
        self.resistance = resistance
        self.max_power = max_power

        self.__voltage_drop = 0.0
        self.__current_flow = 0.0

    def update_state(self, input_voltage: float):
        if self.is_burned:
            self.input_current = 0
            self.output_current = 0
            return

        self.__current_flow = input_voltage / self.resistance
        power = input_voltage * self.__current_flow

        if power > self.max_power:
            self.burn()
            self.input_current = 0
            self.output_current = 0
            return

        self.input_current = self.__current_flow
        self.output_current = self.__current_flow
        self.__voltage_drop = input_voltage

    @property
    def voltage_drop(self):
        return self.__voltage_drop

    @property
    def current_flow(self):
        return self.__current_flow