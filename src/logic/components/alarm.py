from component import Component
import time

class Alarm(Component):
    def __init__(self, volume:int = 50, frequency:int = 440):
        super().__init__()
        
        self.__is_on = False
        self.__volume = volume
        self.__frequency = frequency
        self.last_trigger_time = None
    @property
    def is_on(self): return self.__is_on

    @property
    def volume(self): return self.__volume

    @volume.setter
    def volume(self, value:int):
        self.__volume = max(0, min(100, value)) 

    @property
    def frequency(self): return self.__frequency

    @frequency.setter
    def frequency(self, value:int):
        if value > 0:
            self.__frequency = value
    def draw(self, canvas):

        color = "red" if self.__is_on else "gray"
        size = 40

        x,y = self.position_x, self.position_y
        self.obj = canvas.create_oval(x, y, x+size, y+size, fill=color, width=2)
        canvas.create_text(x+20, y+55, text=f"Alarm {self.id}", font=("Arial",10))
    
    def __str__(self):
        return f"Alarm(id={self.id}, on={self.is_on}, volume={self.volume}, freq={self.frequency})"