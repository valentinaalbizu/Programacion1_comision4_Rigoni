# Crear archivo 
productos_iniciales = [
    "Lapicera,1,500,30\n",
    "Cuaderno,3,250,15\n",
    "Goma,500,40\n"
]

try:
    with open("productos.txt", "x") as archivo:
        archivo.writelines(productos_iniciales)
except FileExistsError:
    pass  

# Leer y mostrar productos
productos = []

try:
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
except FileNotFoundError:
    print("El archivo no existe. Se creará al guardar los productos.")

# Agregar producto desde teclado
nuevo = input("\nIngresar nuevo producto (nombre,precio,cantidad): ")
partes = nuevo.strip().split(",")

if len(partes) == 3:
    try:
        productos.append({
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        })
    except ValueError:
        print("Error: precio o cantidad inválidos.")
else:
    print("Formato incorrecto. No se agregó el producto.")

# Buscar producto por nombre
buscado = input("\nBuscar producto por nombre: ").lower()
encontrado = False

for p in productos:
    if p["nombre"].lower() == buscado:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

# Guardar productos actualizados
try:
    with open("productos.txt", "w") as archivo:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            archivo.write(linea)
    print("\nArchivo actualizado con todos los productos.")
except Exception as e:
    print("Error al guardar el archivo:", e)