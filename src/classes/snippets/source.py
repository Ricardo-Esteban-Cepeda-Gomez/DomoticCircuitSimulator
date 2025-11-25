from classes.snippets.component import Component

class Source(Component):

    def __init__(self):
        self.__type = "AC"
        self.current = 0.0
        self.voltage = 0.0