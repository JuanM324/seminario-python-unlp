import random
words = {
    "programacion": ["python","programa","funcion","bucle"],
    "datos": ["variable","entero","cadena","lista"]
}
puntaje = 0
print("¡Bienvenido al Ahorcado!")
print()

seguir = True

while seguir:
    print("Estas son las Categorias disponibles para Jugar")
    for categoria in words:
        print(categoria," - ") 
    categoria=input("Elegi una categoria: ").lower() 
    
    if categoria not in words:
        print("Categoria no valida")
    else:
        word = random.choice(words[categoria])
        guessed = []
        attempts = 6
        print(f"La categoria elegida es: {categoria}") 
        print(f"Su puntaje es: {puntaje}")     
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
                print("Letra no válida")
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
            puntaje = 0
            seguir=False
            print(f"Su puntaje es: {puntaje}")