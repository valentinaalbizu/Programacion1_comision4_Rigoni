#ejrcicio 1
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#ejercicio 2
mis_favoritos = ["chocolate", "libros", "gatos", "montañas", "música"]
print(mis_favoritos[-2]) 

#ejercicio 3
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luz")
lista_vacia.append("energía")
print(lista_vacia)

#ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#ejercicio 5
    #Este programa toma una lista de números, identifica el más grande y lo elimina, dejando el resto intacto.
    
#ejercicio 6
numeros = list(range(10, 31, 5))
print(numeros[:2]) 

#ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "convertible"]
print(autos)

#ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
