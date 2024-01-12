import os

class Job:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = "N/A"
        
    def consultar_estado(self):
        print(f"Job {self.nombre}: en estado {self.estado}.")

# Crear una instancia de la clase Persona
job1 = Job("JOB01AB", "os")

# Llamar a un método de la instancia
job1.consultar_estado()
