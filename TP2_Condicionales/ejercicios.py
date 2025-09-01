# ejercicio 1

edad = int(input("Por favor, ingresa tu edad: "))

if edad > 18:
    print("Es mayor de edad.")

#ejercicio 2
nota = int(input("Por favor, ingresa tu nota: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#ejercicio 3
numero = int(input("Por favor, ingresa un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#ejercicio 4
edad = int(input("Por favor, ingresa tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#ejercicio 5
contrasena = input("Por favor, ingresa una contraseña: ")

longitud = len(contrasena)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

try:
    moda = mode(numeros_aleatorios)
except:
    moda = "No hay moda"

mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"La lista de números es: {numeros_aleatorios}\n")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print("-" * 20)

if media > mediana and mediana > moda:
    print("Hay un sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("Hay un sesgo negativo o a la izquierda.")
elif media == mediana and mediana == moda:
    print("No hay sesgo.")
else:
    print("La distribución no sigue un patrón de sesgo claro.")

#ejercicio 7
frase = input("Por favor, ingresa una frase o palabra: ")

ultimo_caracter = frase[-1].lower()

vocales = ['a', 'e', 'i', 'o', 'u']

if ultimo_caracter in vocales:
    frase_final = frase + "!"
    print(frase_final)
else:
    print(frase)

#ejercicio 8
nombre = input("Por favor, ingresa tu nombre: ")

print("Elige una opción para tu nombre:")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Primera letra en mayúscula")
opcion = input("Ingresa el número de tu opción (1, 2 o 3): ")

if opcion == '1':
    nombre_modificado = nombre.upper()
    print(f"Tu nombre en mayúsculas es: {nombre_modificado}")
elif opcion == '2':
    nombre_modificado = nombre.lower()
    print(f"Tu nombre en minúsculas es: {nombre_modificado}")
elif opcion == '3':
    nombre_modificado = nombre.title()
    print(f"Tu nombre con la primera letra en mayúscula es: {nombre_modificado}")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")

#ejercicio 9
magnitud = float(input("Por favor, ingresa la magnitud del terremoto: "))

if magnitud < 3.0:
    print("Muy leve (imperceptible).")
elif magnitud >= 3.0 and magnitud < 4.0:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4.0 and magnitud < 5.0:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5.0 and magnitud < 6.0:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6.0 and magnitud < 7.0:
    print("Muy Fuerte (puede causar daños significativos).")
else: 
    print("Extremo (puede causar graves daños a gran escala).")

#ejercicio 10 
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = input("¿Qué mes del año es?: ").lower()
dia = int(input("¿Qué día del mes es?: "))

meses_nombres = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
}

if mes in meses_nombres:
    mes_numero = meses_nombres[mes]
else:
    print("Mes no válido. Por favor, ingresa un mes correcto.")
    exit() 

if hemisferio == 'N':
    if (mes_numero == 12 and dia >= 21) or mes_numero == 1 or mes_numero == 2 or (mes_numero == 3 and dia <= 20):
        print("Te encuentras en Invierno.")
    elif (mes_numero == 3 and dia >= 21) or mes_numero == 4 or mes_numero == 5 or (mes_numero == 6 and dia <= 20):
        print("Te encuentras en Primavera.")
    elif (mes_numero == 6 and dia >= 21) or mes_numero == 7 or mes_numero == 8 or (mes_numero == 9 and dia <= 20):
        print("Te encuentras en Verano.")
    elif (mes_numero == 9 and dia >= 21) or mes_numero == 10 or mes_numero == 11 or (mes_numero == 12 and dia <= 20):
        print("Te encuentras en Otoño.")
    else:
        print("Los datos ingresados no corresponden a una fecha válida.")

elif hemisferio == 'S':
    
    if (mes_numero == 12 and dia >= 21) or mes_numero == 1 or mes_numero == 2 or (mes_numero == 3 and dia <= 20):
        print("Te encuentras en Verano.")
    elif (mes_numero == 3 and dia >= 21) or mes_numero == 4 or mes_numero == 5 or (mes_numero == 6 and dia <= 20):
        print("Te encuentras en Otoño.")
    elif (mes_numero == 6 and dia >= 21) or mes_numero == 7 or mes_numero == 8 or (mes_numero == 9 and dia <= 20):
        print("Te encuentras en Invierno.")
    elif (mes_numero == 9 and dia >= 21) or mes_numero == 10 or mes_numero == 11 or (mes_numero == 12 and dia <= 20):
        print("Te encuentras en Primavera.")
    else:
        print("Los datos ingresados no corresponden a una fecha válida.")

else:
    print("Hemisferio no válido. Por favor, ingresa 'N' o 'S'.")