# Ejercicio 1: Crear diccionario y agregar frutas
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2: Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio 3: Crear lista solo con nombres de frutas
lista_frutas = list(precios_frutas.keys())
print("Ejercicio 3 - Lista de frutas:", lista_frutas)

# Ejercicio 4: Agenda de contactos
contactos = {}
for i in range(5):
    nombre = input(f"Ejercicio 4 - Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre que querés consultar: ")
if consulta in contactos:
    print(f"Número de {consulta}: {contactos[consulta]}")
else:
    print("Ese contacto no existe.")

# Ejercicio 5: Frase → palabras únicas y recuento
frase = input("Ejercicio 5 - Ingresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# Ejercicio 6: Alumnos y promedio de notas
alumnos = {}
for i in range(3):
    nombre = input(f"Ejercicio 6 - Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(int(input(f"Ingresá nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

# Ejercicio 7: Sets de estudiantes
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Ejercicio 7 - Aprobados en ambos:", ambos)
print("Aprobados solo en uno:", solo_uno)
print("Aprobados en al menos uno:", al_menos_uno)

# Ejercicio 8: Stock de productos
stock = {"lapiz": 10, "cuaderno": 5}
producto = input("Ejercicio 8 - Ingresá el nombre del producto a consultar: ")

if producto in stock:
    print(f"Stock de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingresá stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# Ejercicio 9: Agenda con tuplas como claves
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
dia = input("Ejercicio 9 - Ingresá el día: ")
hora = input("Ingresá la hora: ")
evento = agenda.get((dia, hora), "No hay actividad programada.")
print(f"Actividad en {dia} a las {hora}: {evento}")

# Ejercicio 10: Invertir diccionario país-capital
paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo"}
invertido = {capital: pais for pais, capital in paises.items()}
print("Ejercicio 10 - Diccionario invertido:", invertido)
