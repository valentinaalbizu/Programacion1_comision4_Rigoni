#Recursividad

# 1) Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")


# 2) Serie de Fibonacci recursiva
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")


# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


# 4) Conversión decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    return decimal_a_binario(n) if n != 0 else "0"


# 5) Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


# 6) Suma de dígitos de un número
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


# 7) Contar bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


# 8) Contar cuántas veces aparece un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)


if __name__ == "__main__":
    print("Factoriales hasta 5:")
    mostrar_factoriales(5)

    print("\nFibonacci hasta posición 7:")
    mostrar_fibonacci(7)

    print("\nPotencia 2^5:", potencia(2, 5))

    print("\nBinario de 10:", convertir_a_binario(10))

    print("\n¿'reconocer' es palíndromo?", es_palindromo("reconocer"))

    print("\nSuma de dígitos de 1234:", suma_digitos(1234))

    print("\nBloques para pirámide de base 4:", contar_bloques(4))

    print("\nCantidad de veces que aparece el 2 en 12233421:", contar_digito(12233421, 2))
