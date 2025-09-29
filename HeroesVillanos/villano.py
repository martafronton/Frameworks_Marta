import random

from personaje import Personaje

class Villano(Personaje) :
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        super().__init__(nombre, apellidos, fecha_nacimiento)
        self.chagepeteador = random.randint(1,100)
        self.entregador_tardio = random.randint(1,100)
        self.ausencias = random.randint(1,100)
        self.hablador = random.randint(1,100)
        self.puntuacion_total = self.calcularPuntuacion()

    def calcularPuntuacion(self):
        suma = self.chagepeteador + self.entregador_tardio + self.ausencias + self.hablador
        return suma /4



    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellidos} (Puntuación: {self.puntuacion_total})"

