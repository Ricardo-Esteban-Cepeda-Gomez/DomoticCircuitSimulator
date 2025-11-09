from Component import component

class led(component):
    def __init__(self, color):
        self.color = color
        self.__intensity = 3
    
    def setIntensity(self, intensity: float):
        self.__intensity = intensity