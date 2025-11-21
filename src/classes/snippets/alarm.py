from Component import component
class alarm(component):
    def __init__ (self):
        isOn = False
        volume = 0
    def toggle(self):
        self.isOn = not self.isOn 