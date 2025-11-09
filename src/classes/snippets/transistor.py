from Component import component

class Transistor:
    def __init__(self, transistor_type: str, vt: float):
        self.type = transistor_type
        self.Vt = vt
        self.current = 0.0
    
    def computeCurrent(self, voltage_in: float):
        if voltage_in > self.Vt:
            self.current = (voltage_in - self.Vt) * 0.1
        else:
            self.current = 0.0