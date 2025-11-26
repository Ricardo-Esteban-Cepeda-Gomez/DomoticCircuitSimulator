from classes.snippets.component import Component

class Led(Component):
    def __init__(self, color):
        self.color = color
        self.intensity = 3