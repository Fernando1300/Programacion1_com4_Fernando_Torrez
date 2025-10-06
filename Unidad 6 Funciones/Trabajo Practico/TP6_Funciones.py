    # ---Actividades--- # 

# 1)
print("Actividad 1")
def imprimir_hola_mundo():
    return "Hola Mundo!" # Devuelve el texto "Hola Mundo!" con return.

resultado = imprimir_hola_mundo() # Luego, en el programa principal, lo guarda en la variable resultado.
print(resultado) # Finalmente, con print(resultado), se muestra en pantalla.

# 2)
print("Actividad 2")
# Se define la función saludar_usuario(nombre) que recibe un parámetro (nombre) y lo devuelve con return.
def saludar_usuario(nombre):
    return nombre 

nombre = input("Ingrese su nombre: ") # En el programa principal, pido al usuario que escriba su nombre con input().
# Ese valor se pasa como argumento a la función (saludar_usuario(nombre)).
resultado = saludar_usuario(nombre) # La función devuelve el nombre, se guarda en resultado.
print(f"Hola {resultado}!") # Finalmente, se imprime el saludo.

#  3)
print("Actividad 3")
# Definimos la función que muestra la información personal
def informacion_personal(nombre, apellido, edad, residencia):
    # Imprime la información en el formato solicitado
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Pedimos al usuario que ingrese su nombre, apellido, edad y residencia 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
# Llamamos a la función con los datos ingresados por el usuario
informacion_personal(nombre, apellido, edad, residencia)

# 4)
print("Actividad 4")
import math # Para usar el valor de pi
# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Pedir al usuario el radio
radio = float(input("Ingrese el radio de un circulo: "))
# Llamar a las funciones y mostrar los resultados
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# 5)
print("Actividad 5")
def segundos_a_horas(segundos): # La función segundos_a_horas recibe los segundos y devuelve directamente las horas.
    return segundos / 3600

# Pedimos los segundos al usuario, llamas a la función y guardas el resultado en horas.
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"Equivale {horas:.2f} horas ")

#  6)
print("Actividad 6")
# Definimos la función que imprime la tabla de multiplicar
def tabla_multiplicar(numero):
    # Recorremos los números del 1 al 10
    for i in range(1, 11):
        # Imprimimos el resultado de multiplicar 'numero' por 'i'
        print(f"{numero} x {i} = {numero * i}")

# Pedimos al usuario que ingrese un número y lo convertimos a entero
numero = int(input("Ingrese un numero: "))
# Llamamos a la función pasando el número ingresado por el usuario
tabla_multiplicar(numero)

#  7)
print("Actividad 7")
# Función que realiza las operaciones básicas y devuelve los resultados
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division  # Devuelve la tupla

# Pedimos los números al usuario
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

# Desempaquetamos la tupla directamente en variables con nombres claros
suma, resta, multiplicacion, division = operaciones_basicas(a, b)

# Mostramos los resultados de forma clara
print(f"La suma de los números es: {suma}")
print(f"La resta de los números es: {resta}")
print(f"La multiplicación de los números es: {multiplicacion}")
print(f"La división de los números es: {division}")

#  8)
print("Actividad 8")
# Definimos la función que calcula el IMC
def calcular_imc(peso, altura):
    # Fórmula del IMC: peso dividido por la altura al cuadrado
    return peso / (altura **2)

# Pedimos al usuario que ingrese su altura en metros y la convertimos a float
altura = float(input("Introduce tu altura en metros: "))
# Pedimos al usuario que ingrese su peso en kilogramos y lo convertimos a float
peso = float(input("Introduce tu peso en (kg): "))
# Llamamos a la función calcular_imc con los valores ingresados y guardamos el resultado
imc = calcular_imc(peso, altura)
# Mostramos el resultado con dos decimales usando f-string
print(f"Su índice de masa corporal es: {imc:.2f}")

#  9)
print("Actividad 9")
# Definimos la función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
     # Fórmula de conversión: Fahrenheit = (Celsius * 9/5) + 32
    return 9/5 * celsius + 32

# Pedimos al usuario que ingrese la temperatura en grados Celsius
# Convertimos la entrada a entero (float si quieres permitir decimales)
celsius = int(input("Ingrese una temperatura en grados Celsius: "))
# Llamamos a la función pasando la temperatura ingresada y guardamos el resultado
fahrenheit = celsius_a_fahrenheit(celsius)
# Mostramos el resultado de forma clara
print(f"Su temperatura en grados fahrenheit es: {fahrenheit:.2f}") 

#  10)
print("Actividad 10")
# Definimos la función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    # Suma los tres números y divide entre 3 para obtener el promedio
    return (a + b + c) / 3

# Pedimos al usuario que ingrese 3 numeros y los convertimos a enteros 
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
# Llamamos a la función con los tres números ingresados y guardamos el resultado en 'promedio'
promedio = calcular_promedio(a, b, c)
# Mostramos el promedio calculado de manera clara al usuario
print(f"El promedio de los tres numeros es: {promedio}")

print("--Fin de las actividades--")