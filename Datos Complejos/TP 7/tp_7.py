# 1 -------------------------------------------------------------------------------------------------------------------

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2 -------------------------------------------------------------------------------------------------------------------

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3 -------------------------------------------------------------------------------------------------------------------

lista_frutas = list(precios_frutas.keys())

# 4 -------------------------------------------------------------------------------------------------------------------

agenda = {}
for i in range(5):
    contacto = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = int(input(f"Ingrese el número de {contacto}: "))
    agenda[contacto] = numero
    print()

contacto_a_buscar = input("Ingrese el número del contacto a buscar: ")
print()

if contacto_a_buscar not in agenda:
    print("Contacto no encontrado.")
else:
    print(f"El número es {agenda[contacto]}")

# 5 -------------------------------------------------------------------------------------------------------------------

frase = input("Frase: ")
print()

palabras = frase.split()

palabras_unicas = set(palabras)

contador_palabras = {}
for palabra in palabras_unicas:
    contador_palabras[palabra] = 0

for palabra in palabras:
    contador_palabras[palabra] += 1

print(f"Cuenta de palabras: {contador_palabras}\n")

print(f"Palabras únicas: {palabras_unicas}\n")

# 6 -------------------------------------------------------------------------------------------------------------------

alumnos = {}

# Ingresar alumnos y notas
for i in range(3):
    alumno = input(f"Alumno {i+1}: ")
    print()

    nota_1 = float(input(f"Primera nota de {alumno}: "))
    nota_2 = float(input(f"Segunda nota de {alumno}: "))
    nota_3 = float(input(f"Tercera nota de {alumno}: "))
    print()

    alumnos[alumno] = (nota_1, nota_2, nota_3)

# Calcular promedio
for alumno in alumnos:
    suma_notas = 0
    for nota in alumnos[alumno]:
        suma_notas += nota
    
    promedio = suma_notas / 3

    print(f"Promedio de {alumno}: {round(promedio, 2)}")

# 7 -------------------------------------------------------------------------------------------------------------------

aprobados_parcial_1 = {'Juan', 'Ana', 'David'}
aprobados_parcial_2 = {'José', 'Ana', 'Paula'}

print("Alumnos que aprobaron ambos parciales: ")

for alumno in aprobados_parcial_1:
    if alumno in aprobados_parcial_2:
        print(f"    -{alumno}")

print()

alumnos_unico_parcial = set()

for alumno in aprobados_parcial_1:
    if alumno not in aprobados_parcial_2:
        alumnos_unico_parcial.add(alumno)
for alumno in aprobados_parcial_2:
    if alumno not in aprobados_parcial_1:
        alumnos_unico_parcial.add(alumno)

print("Alumnos que aprobaron solo un parcial: ")
for alumno in alumnos_unico_parcial:
    print(f"    -{alumno}")

# 8 -------------------------------------------------------------------------------------------------------------------

productos = {'Manzanas': 20, 'Naranjas': 35, 'Peras': 15}

while True:
    print()
    print("1 - Consultar stock")
    print("2 - Agregar unidades al stock")
    print("3 - Agregar nuevo producto")
    print("4 - Salir")
    print()

    opt = input("Opción: ")
    print()

    if opt == '1':
        for producto, stock in productos.items():
            print(f"{producto}: {stock}")

    elif opt == '2':
        for producto, stock in productos.items():
            print(f"{producto}: {stock}")
        
        print()
        producto_modificar = (input("A qué producto desea modificarle el stock? "))
        nuevo_stock = int(input("Cuánto stock tiene? "))
        print()

        productos[producto_modificar] = nuevo_stock

    elif opt == '3':
        nuevo_producto = input("Nombre del nuevo producto: ")
        nuevo_stock = int(input("Stock: "))

        productos[nuevo_producto] = nuevo_stock

    elif opt == '4':
        break

    else:
        print("Opción inválida.\n")

# 9 -------------------------------------------------------------------------------------------------------------------

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia_consultar = input("Día a consultar: ")
hora_consultar = input("Hora a consultar: ")

dia = "lunes"
hora = "10:00"

# Buscar la actividad en la agenda
actividad = agenda.get((dia, hora))

# Mostrar la actividad
if actividad:
    print(f"El {dia} a las {hora} tienes: {actividad}")
else:
    print(f"No hay actividad programada para el {dia} a las {hora}.")

# 10 ------------------------------------------------------------------------------------------------------------------

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capital_temp = capital
    capitales_paises[capital] = pais

print()