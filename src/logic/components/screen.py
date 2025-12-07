from classes.snippets.component import Component

class Screen(Component):
    def __init__(self, brightness: float = 1.0):
        super().__init__()
        self.__brightness = brightness
        self.__is_on = False
        self.__text = ""

    def turn_on(self):
        if self.input_current > 0:
            self.__is_on = True

    def turn_off(self):
        self.__is_on = False
        self.__text = ""

    def set_brightness(self, value: float):
        self.__brightness = value

    def display(self, text: str):
        if self.__is_on:
            self.__text = text

    def clear(self):
        self.__text = ""

    @property
    def is_on(self):
        return self.__is_on

    @property
    def brightness(self):
        return self.__brightness

    @property
    def text(self):
        return self.__text