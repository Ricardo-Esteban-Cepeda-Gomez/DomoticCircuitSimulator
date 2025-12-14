from logic.components.component import Component

class Switch(Component):
    def __init__(self, label: str = "Switch", is_on: bool = False):
        super().__init__()
        self.label = label
        self.is_on = is_on

    def toggle(self) -> None:
        self.is_on = not self.is_on

    def set_on(self, value: bool) -> None:
        self.is_on = bool(value)

    def allows_current(self) -> bool:
        return self.is_on

    def pass_current(self, current: float) -> float:
        return current if self.is_on else 0.0