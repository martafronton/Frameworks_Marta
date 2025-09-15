from datetime import datetime


ruta = "C:\\Users\\Marta\\Downloads\\Libro2.txt"

fecha = datetime.now().strftime("%d%m%Y")

with open(ruta, "r") as f1:
    lineas = f1.readlines()


with open(f"{fecha}_Personas.log", "a") as f2:
    for fila in lineas:

        datos = fila.split()


        f2.write(
            f'Insert Personas (id,Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) '
            f'values (seq_personas.nextval, "{datos[0]}", "{datos[1]}", "{datos[2]}", "{datos[3]}", "{datos[4]}", "{datos[5]}", "{datos[6]}");\n'
        )

#rutas relativas nunca absolutas. create una carpeta log y lo metes dentro el nuevo archivo. y cuidado con main.php.py php no me gusta mucho
