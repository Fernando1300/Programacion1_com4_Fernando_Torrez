## ---Actividades--- ##

# 1)  
print("--Actividad 1--")

# Inicializamos la variable 'cont' en 0, que será nuestro contador
cont = 0

# Bucle que se repetirá mientras 'cont' sea menor o igual a 100
while cont <= 100: 
    # Imprime el valor actual de 'cont' en cada vuelta del bucle
    print(cont)
    # Incrementa 'cont' en 1 para avanzar hacia el final del bucle
    cont = cont + 1 #Cuando cont llega a 101, la condición cont <= 100 ya no se cumple y el while termina.

# 2) 
print("--Actividad 2--") 

# Pide al usuario un número entero y lo guarda en la variable 'numero'
numero = int(input("Ingrese un numero entero: "))

# Inicializa un contador en 0, que servirá para contar los dígitos
contador = 0

# Bucle que se repite mientras 'numero' sea mayor que 0
while numero > 0:
    # Divide 'numero' entre 10 usando división entera, esto elimina el último dígito del número en cada vuelta
    numero = numero // 10 
    # Suma 1 al contador por cada dígito eliminado
    contador = contador + 1
    # Muestra la cantidad total de dígitos que tenía el número

print(f"El numero contiene {contador} digitos") #Al final, contador indica cuántos dígitos tenía el número.

# 3)
print("--Actividad 3--")

# Pedimos los dos números al usuario
numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

# Inicializamos la suma
suma = 0

# Determinamos cuál es el menor y cuál es el mayor
minimo = min(numero1, numero2)
maximo = max(numero1, numero2)

# Bucle para sumar los números intermedios, excluyendo los extremos
while minimo + 1 < maximo:
    minimo += 1
    suma += minimo

# Mostramos el resultado final
print(suma)

# 4)  
print("--Actividad 4--") 

# Inicializamos la variable que va a almacenar la suma de todos los números ingresados
suma_total = 0

# Pedimos al usuario que ingrese el primer número entero
numeros_enteros = int(input("Ingrese numeros enteros: "))

# Mientras que el usuario ingrese un numero diferente a cero, el programa va a seguir ejecutandose 
while numeros_enteros != 0:
    # Sumamos el número ingresado al total acumulado
    suma_total = suma_total + numeros_enteros
    # Pedimos al usuario el siguiente número entero
    # Si ingresa 0, el bucle se detendrá
    numeros_enteros = int(input("Ingrese el siguiente numero: "))

# Una vez que el usuario ingresa 0, el bucle termina
# Mostramos el total acumulado de todos los números ingresados
print("El total acumulado es: ", suma_total)

# 5) 
print("--Actividad 5--")

import random #Importa el módulo 'random' para poder generar números aleatorios

# Genera un número entero aleatorio entre 0 y 9 y lo guarda en 'numero_secreto'
numero_secreto = random.randint(0, 9)

# Inicializa el contador de intentos en 0
intentos = 0

# Pide al usuario que ingrese un número y lo convierte a entero
numero_ingresado = int(input("Adivina el número entre 0 y 9: "))

# Mientras el número ingresado sea distinto al número secreto, sigue el bucle
while numero_ingresado != numero_secreto:
    # Suma 1 al contador de intentos cada vez que se falla
    intentos += 1 
    # Si el número ingresado es mayor que el secreto, indica al usuario que bajé el número
    if numero_ingresado > numero_secreto:
        print("Muy alto")
    # Si el número ingresado es menor que el secreto, indica al usuario que suba el número
    else:
        print("Muy bajo")
    # Pide otro número al usuario para seguir intentando
    numero_ingresado = int(input("Haga otro intento: ")) 

# Suma 1 más para contar el último intento correcto (cuando sale del while)
intentos += 1

# Muestra un mensaje indicando que adivinó y cuántos intentos le llevó
print(f"Adivinaste! En {intentos} intentos ")

# 6) 
print("--Actividad 6--")

# Inicializa la variable 'contador1' en 100, que será nuestro contador decreciente
contador1 = 100

# Bucle que se repetirá mientras 'contador1' sea mayor o igual a 0
while contador1 >= 0: 
    # Verifica si el número actual es par (divisible por 2 sin residuo)
    if contador1 % 2 == 0: 
        # Si es par, lo imprime en pantalla
        print(contador1)
    contador1 -= 1 #Disminuye 'contador1' en 1 para ir hacia números más pequeños

# 7) 
print("--Actividad 7--")

# Inicializa un contador que irá desde 0 hasta el número ingresado
contador2 = 0

# Inicializa la variable que acumulará la suma de los números
suma_numeros = 0

# Pide al usuario un número entero positivo y lo guarda en 'numero_positivo'
numero_positivo = int(input("Ingrese un numero entero positivo: "))

# Bucle que se repite mientras 'contador2' sea menor o igual al número ingresado
while contador2 <= numero_positivo:
    # Suma el valor actual del contador a la variable acumuladora
    suma_numeros = contador2 + suma_numeros 
    # Incrementa el contador en 1 para pasar al siguiente número
    contador2 += 1

# Muestra en pantalla la suma total de todos los números desde 0 hasta el número ingresado
print(f"{suma_numeros} es la suma de todos los números comprendidos entre 0 y un número entero positivo.")

# 8)  
print("--Actividad 8--")

# Inicio contadores (pares, impares,positivos, negativos y contador) en 0
pares = 0 
impares = 0 
positivos = 0
negativos = 0
contador3 = 0 #Llevará la cuenta de cuántos números ha ingresado el usuario

# Bucle que se repetirá 100 veces, permitiendo ingresar 100 números
while contador3 < 100: 
    # Pide al usuario que ingrese un número entero
    numeros_usuario = int(input("Ingrese un numero entero: "))
    # Si el número es divisible por 2, es par; se incrementa el contador de pares
    if numeros_usuario % 2 == 0: 
        print("El numero es par")
        pares += 1
    # Si no es divisible por 2, es impar; se incrementa el contador de impares
    elif numeros_usuario % 2 != 0:
        print("El numero no es par")
        impares += 1
    # Si el número es mayor que 0, es positivo; se incrementa el contador de positivos
    if numeros_usuario > 0:
        print("El numero ingresado es positivo: ")
        positivos += 1
    # Si el número es menor que 0, es negativo; se incrementa el contador de negativos
    elif numeros_usuario < 0:
        print("El numero ingresado es negativo")
        negativos += 1
    contador3 += 1  #Incrementa el contador para avanzar hacia los 100 números

# Muestra al usuario un resumen con la cantidad de pares, impares, positivos y negativos ingresados    
print(f"{pares} numeros son pares.")
print(f"{impares} numeros son impares.")
print(f"{positivos} numeros son positivos.")
print(f"{negativos} numeros son negativos.")

# 9) 
print("--Actividad 9--")

# Inicializa las variables
suma_valores = 0 #Para acumular la suma de todos los números
media = 0 #Para guardar el resultado final
total = 0 #Para contar cuántos números se ingresan

# Bucle que se repetirá 100 veces, permitiendo ingresar 100 números
while total < 100: 
    # Pide al usuario un número entero
    numeros_media = int(input("Ingrese un numero para calcular la media: "))
    # Acumula la suma de los números ingresados
    suma_valores += numeros_media
    total += 1 # Incrementa el contador para avanzar hacia los 100 números

# Calcula la media dividiendo la suma total de los números entre la cantidad total de números ingresados    
media = suma_valores / total

# Muestra en pantalla la media calculada
print(f"{media} es la media de los valores ingresados. ")

# 10) 
print("--Actividad 10--")

# Inicializa la variable que almacenará el número con los dígitos invertidos
invertido = 0

# Pide al usuario que ingrese un número entero
numero_invertido = int(input("Ingrese numeros enteros: "))

# Bucle que se repite mientras el número ingresado no sea 0
while numero_invertido != 0:
    # Toma el último dígito del número usando el residuo de la división por 10
    digito = numero_invertido % 10 
    # Multiplica el número invertido actual por 10 y suma el nuevo dígito
    invertido = invertido * 10 + digito #Esto agrega el dígito al final del número invertido
    # Elimina el último dígito del número original usando división entera
    numero_invertido //= 10

# Imprime el número resultante con los dígitos invertidos
print("Numeros invertidos: ", invertido)