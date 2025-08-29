# --Actividades TP3 Condicionales--

# 1) 
print("Actividad 1")

# Se pide al usuario que ingrese su edad (entero)
edad =  int(input("Ingrese su edad: "))
# Condición: si la edad es mayor o igual a 18, escribe "Eres mayor de edad"
if edad >= 18:
    print("Eres mayor de edad")
    # Si la edad es menor que 18, "Eres menor de edad"
elif edad < 18:
    print("Eres menor de edad")

# 2) 
print("Actividad 2")

# Se pide la nota al usuario
nota_del_usuario = int(input("Ingrese su nota: "))
# Condición: si la nota es mayor o igual a 6, está aprobado
if nota_del_usuario >= 6:
    print("Aprobado")
# Si la nota es menor que 6, está desaprobado
elif nota_del_usuario < 6:
    print("Desaprobado")

# 3)  
print("Actividad 3")

# Se pide al usuario un número entero
numeros_pares = int(input("Ingrese un numero: "))
# Si el resto de la división entre 2 es 0, el número es par
if numeros_pares % 2 == 0:
    print("Ha ingresado un número par")
# De lo contrario, se indica que no es par
else:
    print("Por favor ingrese un numero par")

# 4) 
print("Actividad 4")

# Se pide al usuario su edad
edad_usuario = int(input("Ingrese su edad: "))
# Menores de 12 años → Niño/a
if edad_usuario < 12:
    print("Niño/a")
# Menores de 12 años → Niño/a
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Adolescente")
# Entre 18 y 29 años → Adulto/a joven
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Adulto/a joven")
# 30 o más → Adulto/a
elif edad_usuario >= 30:
    print("Adulto/a")

# 5) 
print("Actividad 5") 

# Se pide al usuario que ingrese una contraseña
contraseña = input("Ingrese contraseña entre 8 y 14 caracteres: ")
# Validamos la longitud de la contraseña con len()
# La función len() devuelve la cantidad de caracteres que tiene el texto
if len(contraseña) >= 8 and len(contraseña) <= 14:
    # Si la longitud está entre 8 y 14 → contraseña válida
    print("Ha ingresado una contraseña correcta")
else:
    # Si no cumple con la condición → contraseña inválida
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) 
print("Actividad 6")

# Importamos los módulos necesarios
import random 
from statistics import mean, median, mode
# Generamos una lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Calculamos media, mediana y moda con funciones de statistics
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
# Mostramos resultados
print("Números aleatorios:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
# Determinamos el sesgo:
# - Sesgo positivo: media > mediana > moda
# - Sesgo negativo: media < mediana < moda
# - Caso contrario: simétrica
if media > mediana and mediana > moda:
    print("Hay sesgo positivo (a la derecha).")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo (a la izquierda).")
else:
    print("No hay sesgo (simétrica).")

# 7) 
print("Actividad 7")

# Se pide al usuario una frase
frase = str(input("Ingrese una frase: "))
# Se verifica si la última letra es vocal
if frase[-1].lower() in "aeiou":
    # Si lo es, se añade "!"
    frase = frase + "!"
    print(frase)
else:
    # Si no, se imprime la frase tal cual
    print(frase)

# 8)
print("Actividad 8")

# Pido al usuario que ingrese su nombre
nombre_de_usuario = input("Ingrese su nombre: ")
# Muestro un menú de opciones 
print("Menú de opciones:")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Convertir a Título")
# Pido al usuario que elija una opción
opcion = input("Ingrese una opción (1/2/3): ")
# Evaluo la opción ingresada   
if opcion == "1":
    # Convierto el nombre a MAYÚSCULAS usando .upper()
    print(nombre_de_usuario.upper())
elif opcion == "2":
    # Convierto el nombre a minúsculas usando .lower()
    print(nombre_de_usuario.lower())
elif opcion == "3":
    # Convierto el nombre a formato título usando .title(). Convierte la primera letra a mayuscula
    print(nombre_de_usuario.title())

# 9)
print("Actividad 9")

# Pido al usuario que ingrese la magnitud del terremoto y uso float para permitir decimales 
magnitud_terremoto = float(input("Ingrese la magnitud de un terremoto: "))
# Si la magnitud es menor a 3, se considera "Muy leve"
if magnitud_terremoto < 3:
        print("Muy leve")
# Si la magnitud está entre 3 (inclusive) y menor que 4 → "Leve"
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:         
        print("Leve")
# Si la magnitud está entre 4 (inclusive) y menor que 5 → "Moderado"
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
        print("Moderado")
# Si la magnitud está entre 5 (inclusive) y menor que 6 → "Fuerte"
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
        print("Fuerte")
# Si la magnitud está entre 6 (inclusive) y menor que 7 → "Muy fuerte"
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
        print("Muy fuerte")
else:  #Todo lo que sea 7 o más
        print("Extremo")

# 10)

print("Activida 10")

# Pido al usuario el hemisferio en el que se encuentra (N o S).
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper() # .upper() convierte la entrada a mayúscula por si se ingrea (n/s)
mes_del_año = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
# Determinar estación
# Opción 1: Invierno en el hemisferio norte, Verano en el sur
# Del 21 de diciembre al 20 de marzo
if (mes_del_año == 12 and dia >= 21) or (mes_del_año in [1, 2]) or (mes_del_año == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
# Opción 2: Primavera en el norte, Otoño en el sur
# Del 21 de marzo al 20 de junio
elif (mes_del_año == 3 and dia >= 21) or (mes_del_año in [4, 5]) or (mes_del_año == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
# Opción 3: Verano en el norte, Invierno en el sur
# Del 21 de junio al 20 de septiembre
elif (mes_del_año == 6 and dia >= 21) or (mes_del_año in [7, 8]) or (mes_del_año == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
# Opción 4: Otoño en el norte, Primavera en el sur
# Del 21 de septiembre al 20 de diciembre
elif (mes_del_año == 9 and dia >= 21) or (mes_del_año in [10, 11]) or (mes_del_año == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
# Mostrar resultado
if hemisferio == "N":
    print("En el hemisferio norte la estación es:", estacion_norte)
elif hemisferio == "S":
    print("En el hemisferio sur la estación es:", estacion_sur)
else:
    print("Opción de hemisferio no válida. Use N o S.")