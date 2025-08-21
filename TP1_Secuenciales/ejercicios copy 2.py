#ejercicios secuenciales clase 1  (Valentina albizu y Sofia blangetti)


#Pedir al usuario el monto total de la cuenta.

precio=float(input("Por favor ingrese el monto total de la cuenta: "))

print(f"El monto de se cuenta si descuentos es de: {precio}")



#Calcular la propina sugerida al 10%

descuento1=0.10

print("Al producto se le realizara un descunto del 10%")

precio1= precio - (precio*descuento1)

print(f"Propina sugerida del 10% es de: {precio1}")

precio_total1= precio + precio1

print(f"Total a pagar con el 10%: {precio_total1}")



#Calcular la propina sugerida al 15%

descuento2=0.15

print("Al producto se le realizara un descunto del 15%")

precio2= precio - (precio*descuento2)

print(f"Propina sugerida del 15% es de: {precio2}")

precio_total2= precio + precio2

print(f"T0tal a pagar con el 15%: {precio_total2}")