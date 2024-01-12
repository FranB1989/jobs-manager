from Calendario import Calendario

class Job:
    def __init__(self, nombre, tipo, calendario):
        self._nombre = nombre
        self._tipo = tipo
        self._estado = "N/A"
        self._calendario = calendario
    
    @property
    def nombre(self):
        return self._nombre    
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        self._estado = nuevo_estado

    @property
    def calendario(self):
        return self._calendario
    
    @calendario.setter
    def calendario(self, nuevo_calendario):
        self._calendario = nuevo_calendario
        

# Crear una instancia de la clase Persona
calendario = Calendario("Semanal")
job1 = Job("JOB01AB", "os", calendario)

# Llamar a un método de la instancia
print(f"El calendario del job {job1.nombre} es {job1.calendario.nombre}")
