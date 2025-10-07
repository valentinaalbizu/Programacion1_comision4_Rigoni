import random

palabras = ["python", "variable", "funcion", "algoritmo", "compilar", "codigo"]

# Función para elegir una palabra al azar
def elegir_palabra(lista):
    return random.choice(lista)

# Función para mostrar el estado actual de la palabra
def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print("Palabra:", tablero.strip())

# Función para mostrar el cuerpo del ahorcado
def mostrar_cuerpo(intentos_restantes):
    errores = 6 - intentos_restantes

    partes = [
        "  O  ",       # Cabeza
        " /   ",       # Brazo izquierdo
        "\\  ",       # Brazo derecho (doble barra para escapar)
        "  |  ",       # Torso
        " /",          # Pierna izquierda
        "   \\"          # Pierna derecha (doble barra para escapar)
    ]

    dibujo = [
        "  _______     ",
        " |/      |    ",
        " |           ",  # Cabeza
        " |           ",  # Brazo izquierdo + derecho
        " |           ",  # Torso
        " |           ",  # Piernas
        "_|___        "
    ]

    if errores >= 1:
        dibujo[2] = " |     " + partes[0]
    if errores >= 2:
        dibujo[3] = " |    " + partes[1]
    if errores >= 3:
        dibujo[3] += partes[2]
    if errores >= 4:
        dibujo[4] = " |     " + partes[3]
    if errores >= 5:
        dibujo[5] = " |    " + partes[4]
    if errores == 6:
        dibujo[5] += partes[5]

    print("\nEstado del ahorcado:")
    for linea in dibujo:
        print(linea)

        
# Programa principal
def jugar_ahorcado():
    palabra_secreta = elegir_palabra(palabras)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    print("Adivina la palabra letra por letra. Tienes", intentos, "intentos.")

    while intentos > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        mostrar_cuerpo(intentos)

        letra = input("Ingresa una letra: ").lower().strip()

        if len(letra) != 1 or not letra.isalpha():
            print("Error: Ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra.")
            continue

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Adivinaste una letra!")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        # Verificar si el jugador ha ganado
        todas_adivinadas = all(letra in letras_adivinadas for letra in palabra_secreta)
        if todas_adivinadas:
            mostrar_tablero(palabra_secreta, letras_adivinadas)
            print("¡Felicitaciones! La palabra es correcta:", palabra_secreta)
            break

    if intentos == 0:
        mostrar_cuerpo(intentos)
        print("Te quedaste sin intentos. La palabra era:", palabra_secreta)

# Ejecutar el juego
jugar_ahorcado()
