from datetime import datetime


class Personaje:

    identificador=0
    id=0

    def __init__(self, nombre, apellidos, fecha_nacimiento):
       Personaje.identificador+=1
       self.id = Personaje.identificador
       self.nombre = nombre
       self.apellidos = apellidos
       self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
       self.puntuacion_total =0

    def calcular_edad(self):
        ahora = datetime.now()
        return ahora.year - self.fecha_nacimiento.year - (
                (ahora.month, ahora.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellidos}"


