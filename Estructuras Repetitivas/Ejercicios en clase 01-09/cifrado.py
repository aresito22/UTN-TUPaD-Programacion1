frase_original = []
for i in range(5):
    frase_original.append(input(f"Ingrese la frase {i+1}: "))

corrimiento = int(input("Ingrese el corrimiento a utilizar: "))

# Una lista para almacenar las 5 frases post modificación.
frases_modificadas = []

# No funciona con Ñ
for i in range(5):
    # Una lista para almacenar las letras individuales modificadas de cada frase.
    letras_modificadas = []
    for letra in frase_original[i]:
        if ord('a') <= ord(letra) <= ord('z'):
            # Utilizando aritmética modular; primero se resta 'a' para tratar las letras según su posición en el abecedario
            # y luego utilizando (% 26) para "dar la vuelta" alrededor del abecedario, luego se vuelve a sumar 'a' para
            # convertirla en su valor decimal según ASCII.
            var = chr((((ord(letra) - ord('a')) + corrimiento) % 26) + ord('a'))
            letras_modificadas.append(var)
        elif ord('A') <= ord(letra) <= ord('Z'):
            var = chr((((ord(letra) - ord('A')) + corrimiento) % 26) + ord('A')) 
            letras_modificadas.append(var)
        else:
            #Si la iteración no es a-z o A-Z, simplemente se suma el caracter en la iteración sin más.
            letras_modificadas.append(letra)
    frases_modificadas.append(letras_modificadas)

print("")
print("**MENSAJES DEL DÍA**")
for i in range(5):
    print("".join(frases_modificadas[i]))