import logging
import random
from heroe import Heroe
from villano import Villano

class Gestor:
    heroes = []
    villanos = []

    @staticmethod
    def crear_heroe(nombre, apellidos, fecha):
        h = Heroe(nombre, apellidos, fecha)
        Gestor.heroes.append(h)
        logging.info(f"Héroe creado: {h}")

        return h

    @staticmethod
    def crear_villano(nombre, apellidos, fecha):
        v = Villano(nombre, apellidos, fecha)
        Gestor.villanos.append(v)
        logging.info(f"Villano creado: {v}")
        return v

    @staticmethod
    def borrar_personaje(tipo, id_personaje):
        id_personaje=int(id_personaje)
        if tipo.lower() == "heroe":
            lista = Gestor.heroes
        else:
           lista = Gestor.villanos
        for p in lista:
            if p.id == id_personaje:
                lista.remove(p)
                logging.info(f"{tipo} borrado: {p}")
                print(f"{tipo} borrado correctamente.")
                return
        logging.warning(f"Intento de borrar {tipo} con ID {id_personaje} no encontrado")
        print("Personaje no encontrado.")

    @staticmethod
    def mostrar_personajes(tipo):
        tipo = tipo.strip().lower()
        todos = []

        if tipo == "heroe":
            for h in Gestor.heroes:
                todos.append([h.id, h.nombre])
        elif tipo == "villano":
            for v in Gestor.villanos:
                todos.append([v.id, v.nombre])
        else:
            print("Tipo desconocido. Debe ser 'heroe' o 'villano'.")
            logging.warning("Se intento introducir un dato incorrecto")
        return todos

    @staticmethod
    def buscar(tipo, atributo, valor):
        tipo = tipo.strip().lower()
        if tipo == "heroe":
            lista = Gestor.heroes
        elif tipo == "villano":
            lista = Gestor.villanos
        else:
            print("Tipo desconocido. Debe ser 'heroe' o 'villano'.")
            logging.warning("Se intento introducir un dato incorrecto")
            return []

        valor = valor.strip()
        resultados = []

        for p in lista:
            if atributo.lower() == "edad":
                try:
                    edad = int(valor)
                    if p.calcular_edad() == edad:
                        resultados.append(p)
                except ValueError:
                    print("Edad debe ser un número")
                    logging.warning("Se intento introducir un dato incorrecto")
                    return []
            elif hasattr(p, atributo):
                attr = getattr(p, atributo)
                if type(attr) == int or type(attr) == float:
                    if str(attr) == valor:
                        resultados.append(p)
                else:
                    if valor.lower() == str(attr).lower():
                        resultados.append(p)

        logging.info(f"Búsqueda {tipo} por {atributo}={valor}, encontrados {resultados.__len__()}")
        return resultados

    @staticmethod
    def emparejar():
        if  Gestor.heroes.__len__() ==0 or Gestor.villanos.__len__() ==0:
            logging.warning("Intento de emparejamiento sin suficientes héroes o villanos")
            print("No hay héroes o villanos suficientes para emparejar.")
            return
        h = random.choice(Gestor.heroes)
        v = random.choice(Gestor.villanos)
        diferencia = abs(h.puntuacion_total - v.puntuacion_total)
        if diferencia < 20:
            estado="Equilibrado"
        else:
            estado="Desequilibrado"
        logging.info(f"Emparejamiento: {h} vs {v} combate: {estado}")
        print(f"Combate: {h.nombre} ({h.puntuacion_total}) vs {v.nombre} ({v.puntuacion_total}) combate: {estado}")
