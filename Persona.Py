class persona:
    def __init__(self, nombre, anio_nacimiento):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento

    def calcular_edad(self, anio_actual):
        return anio_actual - self.anio_nacimiento
