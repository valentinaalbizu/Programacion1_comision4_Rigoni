#hacer una mochila

# Función para pedir un número válido de espacios
def crear_mochila():
    while True:
        try:
            espacios = int(input("Ingresa cuántos espacios tendrá la mochila: "))
            if espacios <= 0:
                print("Error: Debes ingresar un número positivo mayor que cero.")
            else:
                return ["vacío"] * espacios
        except ValueError:
            print("Error: Ingresa un número entero válido.")

# Función para mostrar el contenido de la mochila
def ver_mochila(mochila):
    print("\nContenido de la mochila:")
    for i in range(len(mochila)):
        print(f"Espacio {i}: {mochila[i]}")

# Función para guardar un objeto 
def guardar_objeto(mochila):
    try:
        pos = int(input(f"Ingrese la posición (0-{len(mochila)-1}): "))
        objeto = input("Ingresa el objeto mágico: ").strip()
        if objeto == "":
            print("Error: No se puede guardar una cadena vacía.")
        else:
            mochila[pos] = objeto
            print(f"{objeto} guardado en el espacio {pos}")
    except ValueError:
        print("Error: Debes ingresar un número entero para la posición.")
    except IndexError:
        print("Error: La posición ingresada no existe en la mochila.")

# Función para eliminar un objeto
def eliminar_objeto(mochila):
    try:
        pos = int(input(f"Ingrese la posición a vaciar (0-{len(mochila)-1}): "))
        if mochila[pos] == "--- vacío ---":
            print("Ese espacio ya está vacío.")
        else:
            mochila[pos] = "--- vacío ---"
            print(f"Objeto eliminado del espacio {pos}")
    except ValueError:
        print("Error: Debes ingresar un número entero para la posición.")
    except IndexError:
        print("Error: La posición ingresada no existe en la mochila.")

# Programa principal
mochila = crear_mochila()

while True:
    print("\n--- Menú de la Mochila ---")
    print("1. Guardar objeto")
    print("2. Ver mochila")
    print("3. Salir")
    print("4. Eliminar objeto")  # Desafío extra

    opcion = input("Elige una opción: ")

    if opcion == "1":
        guardar_objeto(mochila)
    elif opcion == "2":
        ver_mochila(mochila)
    elif opcion == "3":
        print("¡Hasta la próxima aventura!")
        break
    elif opcion == "4":
        eliminar_objeto(mochila)
    else:
        print("Opción inválida. Intenta nuevamente.")

