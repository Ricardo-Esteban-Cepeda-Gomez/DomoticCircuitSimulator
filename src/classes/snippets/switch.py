from classes.snippets.component import component
class Switch(component):
    def __init__(self, label: str):
        self.label = label
        self.isOn = False

    def toggle(self):
        self.isOn = not self.isOn 