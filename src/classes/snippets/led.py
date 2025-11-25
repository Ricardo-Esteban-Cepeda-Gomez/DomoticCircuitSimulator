from classes.snippets.component import Component

class Led(Component):
    def __init__(self, color):
        self.color = color
        self.__intensity = 3
    
    def set_intensity(self, intensity: float):
        self.__intensity = intensity