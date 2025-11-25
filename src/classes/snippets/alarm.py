from classes.snippets.component import component
class Alarm(component):
    def __init__ (self):
        is_on = False
        volume = 0
        frecuency = 0
    def toggle(self):
        self.is_on = not self.is_on 