    # --- Actividades --- #
# 1)
print("Actividad 1")
# Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:   # Caso base: factorial de 0 o 1 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Pedimos al usuario un número
num = int(input("Ingrese un número: "))

# Mostramos el factorial de todos los números entre 1 y num
print(f"\nFactoriales desde 1 hasta {num}:\n")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

# 2)
print("Actividad 2")

# Función recursiva para calcular el valor de Fibonacci en una posición
def fibonacci(n):
    if n == 0:
        return 0    # Caso base 1
    elif n == 1:
        return 1    # Caso base 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva

# Pedimos al usuario la posición hasta la cual quiere mostrar la serie
num = int(input("Ingrese la cantidad de términos de la serie de Fibonacci: "))

# Mostramos la serie completa hasta esa posición
print(f"\nSerie de Fibonacci hasta la posición {num}:\n")
for i in range(num):
    print(f"F({i}) = {fibonacci(i)}")

# 3)
print("Actividad 3")

# Función recursiva para calcular la potencia de un número
def potencia(base, exponente):
    if exponente == 0:      # Caso base: cualquier número elevado a 0 es 1
        return 1
    else:
        return base * potencia(base, exponente - 1)  # Llamada recursiva

# Algoritmo general
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)

print(f"\nEl resultado de {base}^{exponente} es: {resultado}")

# 4)
print("Actividad 4")

# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # Dividimos entre 2 y concatenamos el resto al resultado recursivo
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
num = int(input("Ingrese un número entero positivo: "))

if num < 0:
    print("Por favor, ingrese un número positivo.")
else:
    binario = decimal_a_binario(num)
    print(f"El número {num} en binario es: {binario}")

# 5)
print("Actividad 5")

# Función recursiva para verificar si una palabra es palíndromo
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y última letra son iguales, seguimos verificando el resto
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])  # Llamada recursiva con la palabra sin los extremos
    else:
        return False  # Si las letras no coinciden, no es palíndromo

# Programa principal
texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f" '{texto}' es un palíndromo.")
else:
    print(f" '{texto}' no es un palíndromo.")

# 6) 
print("Actividad 6")

# Función recursiva para sumar los dígitos de un número
def suma_digitos(n):
    # Caso base: si el número es menor que 10, solo tiene un dígito
    if n < 10:
        return n
    else:
        # Suma el último dígito (n % 10) con la suma de los demás dígitos (n // 10)
        return (n % 10) + suma_digitos(n // 10)

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

# 7)
print("Actividad 7")

# Función recursiva para contar los bloques de una pirámide
def contar_bloques(n):
    # Caso base: si solo hay un nivel, se necesita un bloque
    if n == 1:
        return 1
    else:
        # Suma los bloques del nivel actual con los del nivel superior
        return n + contar_bloques(n - 1)

# Programa principal
nivel = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))

if nivel < 1:
    print("Por favor, ingrese un número entero positivo.")
else:
    total = contar_bloques(nivel)
    print(f"El total de bloques necesarios para construir la pirámide es: {total}")

# 8)
print("Actividad 8")

# Función recursiva para contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    # Caso base: si el número tiene un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        # Verificamos si el último dígito coincide
        ultimo = numero % 10
        # Llamada recursiva con el resto del número (sin el último dígito)
        return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar (0-9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Por favor, ingrese un número positivo y un dígito válido entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")

