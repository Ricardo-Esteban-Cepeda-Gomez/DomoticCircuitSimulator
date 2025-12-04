from classes.snippets.component import Component

class Switch(Component):
    def __init__(self, label: str):
        self.label = label
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on 