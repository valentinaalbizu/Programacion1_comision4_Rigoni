#ejercicios en clase

#ejercicio for


alfabeto = "abcdefghijklmnñopqrstuvwxyz"

for i in range(5):
    mensaje = input("Ingrese el mensaje que desea encriptar: ").lower()
    desplazamiento = int(input("ingrese el corrimiento para la encriptacion en numero: "))
    
    mensaje_encriptado = ""

    for caracter in mensaje:
        if caracter in alfabeto:
            indice_actual = alfabeto.find(caracter)
            
            nuevo_indice = (indice_actual + desplazamiento) % 28
            
            nueva_letra = alfabeto[nuevo_indice]

            mensaje_encriptado += nueva_letra
        else:
            mensaje_encriptado += caracter

    print(f"--Mensaje Encriptado: {mensaje_encriptado}---")
    
    print()


#ejercicio while
import random


puntuacion_jugador = 0
puntuacion_computadora = 0


opciones = ["Piedra", "Papel", "Tijera"]

print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")

while True:
    print("--- Menú ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

    try:
        eleccion_jugador_str = input("Elige tu jugada (1-4): ")
        if not eleccion_jugador_str.isdigit():
            raise ValueError
        
        eleccion_jugador = int(eleccion_jugador_str) - 1
        
        if eleccion_jugador == 3:
            print("--- Juego terminado ---")
            print(f"Puntuación final: Jugador {puntuacion_jugador} - {puntuacion_computadora} Computadora")
            break
            
        if eleccion_jugador < 0 or eleccion_jugador > 2:
            print("Opción no válida. Por favor, elige un número del 1 al 4.")
            continue
        
        eleccion_computadora = random.randint(0, 2)
        
        print(f"Tú elegiste: {opciones[eleccion_jugador]}")
        print(f"La computadora eligió: {opciones[eleccion_computadora]}")
        
        
        if eleccion_jugador == eleccion_computadora:
            print("¡Es un empate!")
        
        elif (eleccion_jugador == 0 and eleccion_computadora == 2) or \
             (eleccion_jugador == 1 and eleccion_computadora == 0) or \
             (eleccion_jugador == 2 and eleccion_computadora == 1):
            print("¡Ganaste esta ronda!")
            puntuacion_jugador += 1
            
        else:
            print("La computadora ganó esta ronda.")
            puntuacion_computadora += 1
            
        print(f"Marcador: Jugador {puntuacion_jugador} - {puntuacion_computadora} Computadora")

    except (ValueError, IndexError):
        print("Entrada no válida. Por favor, ingresa un número del 1 al 4.")