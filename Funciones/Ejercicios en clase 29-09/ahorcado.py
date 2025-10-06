import random

def crear_palabra_vacia(palabra):
    palabra_vacia = []

    for letra in palabra:
        palabra_vacia.append('_')

    return palabra_vacia

def realizar_intento(palabra_elegida, palabra_en_pantalla, letra_intentar):
    if letra_intentar in palabra_elegida:
        for i, letra in enumerate(palabra_elegida):
            if letra == letra_intentar:
                palabra_en_pantalla[i] = letra_intentar
        return palabra_en_pantalla
    else:
        return False

palabras = ["boeing", "airbus", "embraer", "bombardier"]

indice_aleatorio = random.randint(0, len(palabras) - 1)
palabra_elegida = palabras.pop(indice_aleatorio)

palabra_en_pantalla = crear_palabra_vacia(palabra_elegida)

intentos_fallidos = 0
letras_intentadas = []
victoria = False

while True:    
    print()
    print(f"Intentos fallidos: {intentos_fallidos}/6")
    print(f"Letras intentadas: {letras_intentadas}")
    print()

    print(*palabra_en_pantalla)
    print()

    letra = input("Ingrese una letra o palabra a adivinar: ")
    print()
    resultado = realizar_intento(palabra_elegida, palabra_en_pantalla, letra)

    if resultado == False:
        print("La letra no está en la palabra.")
        intentos_fallidos += 1
        letras_intentadas.append(letra)
    elif letra == palabra_elegida:
        print("Palabra acertada!")
        victoria = True
    else:
        print("Letra acertada!")

    if "_" not in palabra_en_pantalla:
        victoria = True

    print()

    if victoria == True:
        print(*palabra_en_pantalla)
        print("Ganaste!")
        break
    elif intentos_fallidos > 6:
        print(*palabra_en_pantalla)
        print("Perdiste.")
        break
    else:
        pass