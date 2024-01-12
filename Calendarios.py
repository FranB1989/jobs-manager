import os

class Calendario:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def consultar_nombre(self):
        print(f"Calendario {self.nombre}.")
    