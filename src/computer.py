""""
Authors:
    Ricardo Esteban Cepeda Gomez
    Johan Sebastian Lievano Garcia
    Sebastian Vanegas
"""
class Computer:
    #This class represents a Personal Computer in the app.
    def __init__(self, brand : str, processor : str, ram : int, ssd_space : str, operative_system: str):
        #constructor of the class
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.ssd_space = ssd_space
        self.operative_system = operative_system
    def specs(self):
        print(f"I am a computer of brand {self.brand}. \nI have a processor {self.processor}, {self.ram} GB of RAM. \n{self.ssd_space} SSD capacity, and a {self.operative_system} OS.")