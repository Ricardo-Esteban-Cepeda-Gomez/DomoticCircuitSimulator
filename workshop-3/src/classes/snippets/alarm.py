from classes.snippets.component import Component

class Alarm(Component):
    def __init__ (self):
        is_on = False
        volume = 0
        frecuency = 0
    def on(self):
        if self.input_current > 0:
            self.is_on = True