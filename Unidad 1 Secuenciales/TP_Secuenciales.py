# Ejercicio 1
print("Ejercicio 1")
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

# Ejercicio 2
print("Ejercicio 2")
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. 

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
print("Ejercicio 3")
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

# Ejercicio 4
print("Ejercicio 4")
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro.

import math
radio = float(input("Ingrese el radio de un circulo: "))
area = math.pi * radio ** 2
perimetro =  2 * math.pi * radio
print("El area de un circulo es: ", area)
print("El perimetro de un circulo es: ", perimetro)

# Ejercicio 5 
print("Ejercicio 5")
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale. 

cantidad_segundos = int(input("Ingrese la cantidad de segundos: "))
horas = cantidad_segundos / 3600
print(f"Equivale {horas} horas ")

# Ejercicio 6
print("Ejercicio 6")
#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número.

numero = int(input("Ingrese un numero: "))
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

# Ejercicio 7
print("Ejercicio 7")
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

numeros_entero1 = int(input("Ingrese el primer numero: "))
numero_entero2 = int(input("Ingrese el segundo numero: "))
suma = numeros_entero1 + numero_entero2
division = numeros_entero1 / numero_entero2
multiplicacion = numeros_entero1 * numero_entero2
resta = numeros_entero1 - numero_entero2
print("La suma de los numeros es: ",suma)
print("La division de los numeros es: ",division)
print("La multiplicacion de los numeros es ",multiplicacion)
print("La resta de los numeros es: ", resta)

# Ejercicio 8
print("Ejercicio 8")
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal.

altura = float(input("Introduce tu altura en metros: "))
peso = float(input("Introduce tu peso en (kg): "))
imc = peso / (altura ** 2)
print("Su índice de masa corporal es: ", imc)

# Ejercicio 9
print("Ejercicio 9")
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit

temperatura_en_celsius = int(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = 9/5 * temperatura_en_celsius + 32
print("Su temperatura en grados fahrenheit es: ",fahrenheit)

# Ejercicio 10
print("Ejercicio 10")
#Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números. 

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print("El promedio de los tres numeros es: ",promedio)