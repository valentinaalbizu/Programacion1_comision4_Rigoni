#ejercicios secuenciales   (Valentina albizu)

#ejercicio 1
print("Hola mundo")

#ejercicio 2
nombre=input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre1=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
lugar_residencia=input("Ingrese su lugar de residencia: ")
print(f"soy {nombre1} {apellido},tengo {edad} y vivo en {lugar_residencia} ")

#ejercicio 4
import math
radio = float(input("Ingrese el radio del círculo: "))

# área (π * radio²)
area = math.pi * radio**2

# perímetro (2 * π * radio)
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")