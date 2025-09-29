import random

from personaje import Personaje


class Heroe(Personaje) :
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        super().__init__(nombre, apellidos, fecha_nacimiento)
        self.codigo_limpio = random.randint(1,100)
        self.bien_documentado = random.randint(1,100)
        self.gitGod =random.randint(1,100)
        self.arquitecto = random.randint(1,100)
        self.detallista= random.randint(1,100)
        self.puntuacion_total = self.calcularPuntuacion()

    def calcularPuntuacion(self):
        suma = self.codigo_limpio + self.bien_documentado + self.gitGod + self.arquitecto + self.detallista
        return suma /5

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellidos} (Puntuación: {self.puntuacion_total})"
