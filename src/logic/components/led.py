from logic.components.component import Component

class Led(Component):
    def __init__(self, color: str, max_current: float = 5.0):
        super().__init__()
        self.color = color
        self.intensity = 0
        self.max_current = max_current

    def update_state(self):
        if self.is_burned:
            self.intensity = 0
            return

        if self.input_current > 0:
            if self.input_current <= self.max_current:
                self.state = True
                self.intensity = min(int(self.input_current), 10)
            else:
                self.burn()
                self.state = False
                self.intensity = 0
        else:
            self.state = False
            self.intensity = 0

    def turn_off(self):
        self.state = False
        self.intensity = 0

    def burn(self):
        self.is_burned = True
        self.state = False
        self.intensity = 0

    def fix(self):
        self.is_burned = False