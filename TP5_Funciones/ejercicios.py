import math

# 1. Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludar al usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: división por cero"
    return (suma, resta, multiplicacion, division)

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Menú principal
def mostrar_menu():
    print("--- MENÚ DE FUNCIONES ---")
    print("1. Imprimir Hola Mundo")
    print("2. Saludar Usuario")
    print("3. Información Personal")
    print("4. Área y Perímetro de un Círculo")
    print("5. Convertir Segundos a Horas")
    print("6. Tabla de Multiplicar")
    print("7. Operaciones Básicas")
    print("8. Calcular IMC")
    print("9. Celsius a Fahrenheit")
    print("10. Calcular Promedio")
    print("11. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            imprimir_hola_mundo()

        case "2":
            nombre = input("Ingresa tu nombre: ")
            print(saludar_usuario(nombre))

        case "3":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = input("Edad: ")
            residencia = input("Residencia: ")
            informacion_personal(nombre, apellido, edad, residencia)

        case "4":
            try:
                radio = float(input("Ingresa el radio del círculo: "))
                print(f"Área: {calcular_area_circulo(radio):.2f}")
                print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
            except ValueError:
                print("Error: Ingresa un número válido.")

        case "5":
            try:
                segundos = int(input("Ingresa la cantidad de segundos: "))
                print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")
            except ValueError:
                print("Error: Ingresa un número entero.")

        case "6":
            try:
                numero = int(input("Ingresa un número para la tabla: "))
                tabla_multiplicar(numero)
            except ValueError:
                print("Error: Ingresa un número entero.")

        case "7":
            try:
                a = float(input("Número A: "))
                b = float(input("Número B: "))
                resultados = operaciones_basicas(a, b)
                print(f"Suma: {resultados[0]}")
                print(f"Resta: {resultados[1]}")
                print(f"Multiplicación: {resultados[2]}")
                print(f"División: {resultados[3]}")
            except ValueError:
                print("Error: Ingresa números válidos.")

        case "8":
            try:
                peso = float(input("Peso en kg: "))
                altura = float(input("Altura en metros: "))
                imc = calcular_imc(peso, altura)
                print(f"Tu IMC es: {imc:.2f}")
            except ValueError:
                print("Error: Ingresa valores numéricos.")

        case "9":
            try:
                celsius = float(input("Temperatura en Celsius: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                print(f"Equivalente en Fahrenheit: {fahrenheit:.2f}")
            except ValueError:
                print("Error: Ingresa un número válido.")

        case "10":
            try:
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                c = float(input("Tercer número: "))
                promedio = calcular_promedio(a, b, c)
                print(f"Promedio: {promedio:.2f}")
            except ValueError:
                print("Error: Ingresa números válidos.")

        case "11":
            print("¡Hasta luego!")
            break

        case _:
            print("Opción inválida. Intenta nuevamente.")
