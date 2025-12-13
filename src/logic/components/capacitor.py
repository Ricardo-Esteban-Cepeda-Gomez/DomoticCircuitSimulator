from logic.components.component import Component

class Capacitor(Component):
    def __init__(self, capacitance:float = 1.0, voltage_limit:float = 10.0):
        super().__init__()
        self.__capacitance = capacitance
        self.__voltage = 0.0
        self.__charge = 0.0
        self.__voltage_limit = voltage_limit

    @property
    def capacitance(self):
        return self.__capacitance

    @capacitance.setter
    def capacitance(self, value:float):
        if value > 0:
            self.__capacitance = value

    @property
    def voltage(self):
        return self.__voltage

    @property
    def charge(self):
        return self.__charge

    def update(self, dt: float = 1.0):
        """Integrate input_current over time step dt to update charge and voltage.

        Q_new = Q + I * dt
        V = Q / C
        """
        if self.is_burned:
            self.output_current = 0.0
            return

        # Ensure dt positive
        try:
            dt = float(dt) if dt is not None else 1.0
            if dt <= 0:
                dt = 1.0
        except Exception:
            dt = 1.0

        # Integrate charge (I in amps, dt in seconds -> Q in coulombs)
        # The code uses abstract units; keep simple proportional behavior
        if getattr(self, "input_current", 0.0) and self.input_current > 0:
            self.__charge += self.input_current * dt
            try:
                self.__voltage = self.__charge / self.__capacitance
            except Exception:
                self.__voltage = 0.0
            if self.__voltage > self.__voltage_limit:
                self.burn()
        else:
            # discharge slowly (simple exponential-like decay)
            self.__charge -= self.__charge * (0.1 * dt)
            if self.__charge < 1e-9:
                self.__charge = 0.0
            try:
                self.__voltage = self.__charge / self.__capacitance
            except Exception:
                self.__voltage = 0.0
            # output current proportional to voltage (simple model)
            self.output_current = self.__voltage * 0.1

    def discharge(self, rate:float = 0.05):
        if self.__charge > 0:
            self.__charge -= self.__charge * rate
            try:
                self.__voltage = self.__charge / self.__capacitance
            except Exception:
                self.__voltage = 0.0

    def burn(self):
        super().burn()
        self.output_current = 0
        self.__voltage = 0

    def fix_burn(self):
        super().fix_burn()

    def draw(self, canvas):
        color = "blue" if not self.is_burned else "black"
        x, y = self.position_x, self.position_y
        w, h = 40, 20
        self.obj = canvas.create_rectangle(x, y, x+w, y+h, fill=color, width=2)
        canvas.create_text(x+20, y+30, text=f"C {self.id}", font=("Arial",10))

    def __str__(self):
        return f"Capacitor(id={self.id}, C={self.capacitance}, V={self.voltage}, Q={self.charge})"