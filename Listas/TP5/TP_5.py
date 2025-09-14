# 1
for i in range(1, 101):
    if i % 4 == 0:
        print(i)

# 2
mi_lista = ["a", "b", "c", "d", "e"]
print(mi_lista[-2])

# 3
lista_letras = []
lista_letras.append("a")
lista_letras.append("b")
lista_letras.append("c")
print(lista_letras)

# 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# 5
# El programa crea una lista de enteros, utiliza max() para extraer el entero
# de mayor valor y .remove() para eliminarlo de la lista. Es decir, elimina el
# entero más grande. Luego imprime la lista resultante que ya no contiene el número eliminado

# 6
numeros = []
for i in range(10, 31, 5):
    numeros[i] = i
print(numeros)

# 7 
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "civic"
autos[2] = "corolla"

# 8 
dobles = []
for i in range(5, 16, 5):
    dobles.append(i*2)
print(dobles)

# 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
del compras[0][0]

print(compras)

# 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)