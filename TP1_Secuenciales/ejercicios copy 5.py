#ejercicios secuenciales   (Valentina albizu)

#ejercicio 7
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#ejercicio 8
peso = float(input("Ingrese su peso en kilogramos (kg): "))
altura = float(input("Ingrese su altura en metros (m): "))

# IMCpeso dividido por la altura al cuadrado (IMC=peso/altura 
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")

#ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius (°C): "))

# convertir de Celsius a Fahrenheit es: F=(9/5)C+32.
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit}°F.")

#ejercicio 10
num3 = float(input("Ingrese el primer número: "))
num4 = float(input("Ingrese el segundo número: "))
num5 = float(input("Ingrese el tercer número: "))

promedio = (num3 + num4 + num5) / 3
print(f"El promedio de los tres números es: {promedio}")