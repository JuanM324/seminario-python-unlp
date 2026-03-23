import random
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]
word = random.choice(words)
guessed = []
attempts = 6
puntaje = 0
print("¡Bienvenido al Ahorcado!")
print(f"Su puntaje es: {puntaje}")
print()
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
# Verificar si el jugador ya adivinó la palabra completa

    if "_" not in progress:
        print("¡Ganaste! Sumas +6 puntos.")
        puntaje+=6
        print(f"Puntaje = {puntaje}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()
    if len(letter) !=1 or not letter.isalpha():
        print("Entrada no válida")
        print()
    else:    
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter) 
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print(f"Esa letra no está en la palabra. Se le resta -1 punto. Puntaje = {puntaje}")
        print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Su puntaje es: {puntaje == 0}")