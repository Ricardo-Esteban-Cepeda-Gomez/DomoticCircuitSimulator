from logic.components.component import Component

class Switch(Component):
    """
    Switch que puede permitir o bloquear el paso de corriente.
    Métodos útiles:
      - toggle(): invierte el estado
      - set_on(bool): fija el estado
      - allows_current(): True si deja pasar corriente
      - pass_current(current): devuelve la corriente de salida (0 si está abierto)
    """
    def _init_(self, label: str = "Switch", is_on: bool = False):
        super()._init_()
        self.label = label
        self.is_on = is_on

    def toggle(self) -> None:
        """Invierte el estado del switch."""
        self.is_on = not self.is_on

    def set_on(self, value: bool) -> None:
        """Fija el estado del switch."""
        self.is_on = bool(value)

    def allows_current(self) -> bool:
        """Indica si el switch permite el paso de corriente."""
        return self.is_on

    def pass_current(self, current: float) -> float:
        """
        Simula el paso de corriente a través del switch.
        Devuelve 'current' si está cerrado (ON), o 0.0 si está abierto (OFF).
        """
        return current if self.is_on else 0.0