import logging
from Gestor import Gestor

logging.basicConfig(
    filename="heroes_villanos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def menu():
    print("1) Para crear Heroe")
    print("2) Para crear Villano")
    print("3) Para buscar un heroe o villano")
    print("4) Para emparejar personajes")
    print("5) Para borrar personaje ")
    print("6) Para salir")

def gestionAulaDeHeroesYVillanos(opcion):

    if opcion == 1:
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        fecha = input("Fecha de nacimiento (dd/mm/yyyy): ")
        h = Gestor.crear_heroe(nombre, apellidos, fecha)
        print("Héroe creado:", h)
    elif opcion == 2:
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        fecha = input("Fecha de nacimiento (dd/mm/yyyy): ")
        v = Gestor.crear_villano(nombre, apellidos, fecha)
        print("Villano creado:", v)
    elif opcion == 3:
        tipo = input("¿Buscar heroe o villano?: ")
        atributo = input("Introduce el atributo que buscas(nombre, apellidos, edad...): ")
        valor = input("Introduce el valor: ")
        resultados = Gestor.buscar(tipo, atributo, valor)
        if resultados.__len__() > 0:
            for r in resultados:
                print(r)
        else:
            print("No se encontraron resultados.")
    elif opcion == 4:
        Gestor.emparejar()
    elif opcion ==5:
        tipo = input("¿Borrar heroe o villano?: ")
        print(Gestor.mostrar_personajes(tipo))
        id = input("Introduce el ID personaje que quieres borrar: ")
        Gestor.borrar_personaje(tipo,id)




def main():
    try:
        while True:
            menu()
            opcion = int(input("¿Qué eliges?: "))
            if opcion ==6:
                    break
            if opcion > 6:
                print("Selecciona una opción válida")
            else:
                gestionAulaDeHeroesYVillanos(opcion)
    except Exception as e:
        print(f"Error {e}")
        logging.error(f"Error en main: {e}")

if __name__ == "__main__":
    main()
