from logic.components.component import Component

class Source(Component):
    def __init__(self, voltage: float = 5.0, source_type: str = "DC"):
        super().__init__()
        self.__type = source_type
        # Nominal voltage of the source (Volts)
        self.voltage = float(voltage)
        # current supplied by the source (A) - updated by the simulator
        self.current = 0.0
        # convenience: treat voltage_drop as the source voltage
        self.voltage_drop = float(self.voltage)

    def set_voltage(self, v: float):
        try:
            self.voltage = float(v)
            self.voltage_drop = float(self.voltage)
        except Exception:
            pass

    def update(self):
        # Ensure derived fields stay in sync
        try:
            self.voltage_drop = float(self.voltage)
        except Exception:
            pass
        try:
            # output_current mirrors current computed by workspace/simulator
            self.output_current = float(getattr(self, "current", 0.0))
        except Exception:
            pass