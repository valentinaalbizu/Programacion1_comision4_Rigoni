import csv
import os

archivo = "productos.csv"

# Crear archivo con encabezado si no existe
if not os.path.exists(archivo):
    try:
        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "precio"])
    except:
        print("Error al crear el archivo.")

while True:
    print("\nMENÚ DE PRODUCTOS")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            with open(archivo, "r") as f:
                lector = csv.DictReader(f)
                total = 0
                print("\nProductos registrados:")
                for fila in lector:
                    print(f"- {fila['nombre']} -> ${fila['precio']}")
                    total += float(fila['precio'])
                print(f"Total de precios: ${total}")
        except:
            print("Error al leer el archivo.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio: ")
        try:
            precio = float(precio)
            if precio > 0:
                with open(archivo, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([nombre, precio])
                print("Producto agregado correctamente.")
            else:
                print("El precio debe ser mayor a cero.")
        except:
            print("Precio inválido.")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a eliminar: ").lower()
        productos = []
        eliminado = False
        try:
            with open(archivo, "r") as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    if fila["nombre"].lower() != nombre:
                        productos.append(fila)
                    else:
                        eliminado = True
            with open(archivo, "w", newline="") as f:
                campos = ["nombre", "precio"]
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(productos)
            if eliminado:
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")
        except:
            print("Error al eliminar el producto.")

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")