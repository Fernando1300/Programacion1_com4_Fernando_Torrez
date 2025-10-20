        ##---Actividades---##

#1) Dado el diccionario precios_frutas 
print("Actividad 1")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800 
print("Actividad 2")
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1330
precios_frutas['Melón'] = 2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.
print("Actividad 3")
precios_frutas = ['Banana', 'Ananá', 'Melón', 'Uva','Naranja','Manzana', 'Pera']
print(precios_frutas)

#4)
print("Actividad 4")
# Define e inicializa el diccionario 'contactos'.
# Las CLAVES son los nombres (strings) y los VALORES son los números de contacto (enteros).
contactos = {"Juan": 123456, "Fer": 654321, "Sol": 678909, "Fran": 908765, "Tobi": 131415 }

consultar_nombre = input("Consultar nombre: ")
# Solicita al usuario que ingrese un nombre y guarda esa entrada (string)
# en la variable 'consultar_nombre'.
print(contactos[consultar_nombre])
# Intenta acceder al diccionario 'contactos' usando el nombre ingresado por el usuario
# como CLAVE para obtener e imprimir el número de contacto asociado.

#5)
print("Actividad 5")
import string

def procesar_frase():

    print("--- Procesador de Frases ---")

    # Solicitar la frase al usuario
    frase_original = input("Por favor, ingresa una frase o texto: ")

    # Preprocesamiento: Convertir a minúsculas y limpiar puntuación
    # Transforma la frase a minúsculas
    frase_limpia = frase_original.lower()

    # Quita los signos de puntuación (tablas, comas, etc.) reemplazándolos por un espacio
    # Esto ayuda a que "hola." y "hola" se cuenten como la misma palabra.
    for punc in string.punctuation:
        frase_limpia = frase_limpia.replace(punc, ' ')

    # Dividir la frase en palabras (filtrando espacios extra)
    # split() sin argumentos divide por cualquier espacio y filtra los vacíos
    palabras = frase_limpia.split()

    # --- Resultados ---

    # Palabras Únicas (Usando un set)
    palabras_unicas = set(palabras)
    print("\n--- Palabras Únicas (Set) ---")
    print(palabras_unicas)

    # Diccionario con la Frecuencia de Palabras
    frecuencia_palabras = {}
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementa su contador
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        # Si no está, inicializa su contador en 1
        else:
            frecuencia_palabras[palabra] = 1

    print("\n--- Frecuencia de Palabras (Diccionario) ---")
    print(frecuencia_palabras)

# Ejecutar la función
procesar_frase()

#6)  
print("Actividad 6")
def calcular_promedios_sin_excepciones():

    alumnos_data = {}  # Diccionario para almacenar: {nombre: tupla_de_notas}

    print("--- Ingreso de Notas de Alumnos (Sin manejo de errores) ---")

    # Bucle para ingresar los datos de 3 alumnos
    for i in range(3):
        # Solicitar el nombre
        nombre = input(f"\nIngresa el nombre del alumno {i + 1}: ")

        # Solicitar las 3 notas (asumiendo que el usuario ingresa números válidos)
        print(f"Ingresa las 3 notas para {nombre}:")
        
        # Las entradas se convierten directamente a float.
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        # Guardar las notas como una tupla
        notas_alumno = (nota1, nota2, nota3)
        alumnos_data[nombre] = notas_alumno

    # --- Cálculo y Muestra de Promedios ---
    print("\n--- Promedios de los Alumnos ---")

    # Recorrer el diccionario para calcular e imprimir el promedio de cada alumno
    for nombre, notas in alumnos_data.items():
        # Calcular el promedio: sum(tupla) / len(tupla)
        promedio = sum(notas) / len(notas)

        # Mostrar el resultado, redondeando a 2 decimales
        print(f"El promedio de {nombre} es: {promedio:.2f}")

# Ejecutar la función
calcular_promedios_sin_excepciones()

#7) 
print("Actividad 7")
# Datos de ejemplo (Sets de estudiantes que aprobaron)
parcial1_aprobados = {101, 105, 110, 115, 120, 125}
parcial2_aprobados = {105, 110, 120, 130, 135, 140}

print(f"Aprobaron Parcial 1: {parcial1_aprobados}")
print(f"Aprobaron Parcial 2: {parcial2_aprobados}")

# Mostrar los que aprobaron ambos parciales (Intersección)
# Operador: & o .intersection()
aprobados_ambos = parcial1_aprobados.intersection(parcial2_aprobados)
print("\n--- 1. Aprobaron AMBOS parciales (Intersección) ---")
print(aprobados_ambos)

# Mostrar los que aprobaron SOLO uno de los dos (Diferencia Simétrica)
# Operador: ^ o .symmetric_difference()
# Esto excluye a los que aprobaron AMBOS.
aprobados_solo_uno = parcial1_aprobados.symmetric_difference(parcial2_aprobados)
print("\n--- 2. Aprobaron SOLO UNO de los dos (Diferencia Simétrica) ---")
print(aprobados_solo_uno)

# Mostrar la lista TOTAL de estudiantes que aprobaron al menos un parcial (Unión)
# Operador: | o .union()
# Esto incluye a todos los de P1, todos los de P2, y no repite a los que están en ambos.
aprobados_total = parcial1_aprobados.union(parcial2_aprobados)
print("\n--- 3. Total que aprobaron AL MENOS UNO (Unión) ---")
print(aprobados_total)

#8) 

print("Actividad 8")
def gestionar_inventario():
    
    # Diccionario inicial de ejemplo (Clave: Producto, Valor: Stock)
    inventario = {
        "Laptop": 15,
        "Mouse inalámbrico": 50,
        "Monitor 27": 25,
        "Teclado mecánico": 40
    }

    print("--- Sistema de Gestión de Inventario ---")
    
    while True:
        print("\nInventario actual:", inventario)
        print("\nSelecciona una opción:")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades / Añadir nuevo producto")
        print("3. Salir")
        
        opcion = input("Ingresa el número de tu elección: ")

        if opcion == '1':
            # --- CONSULTAR STOCK ---
            producto = input("Ingresa el nombre del producto a consultar: ").strip()
            
            if producto in inventario:
                print(f"El stock de '{producto}' es: {inventario[producto]} unidades.")
            else:
                print(f"Error: El producto '{producto}' no se encuentra en el inventario.")

        elif opcion == '2':
            # --- AGREGAR / AÑADIR PRODUCTO ---
            producto = input("Ingresa el nombre del producto a modificar o añadir: ").strip()
            
            try:
                unidades = int(input("¿Cuántas unidades deseas agregar? (Ingresa un número entero): "))
            except ValueError:
                print("Error: Debes ingresar un número entero válido.")
                continue

            if producto in inventario:
                # Caso 1: El producto EXISTE (Agregar unidades)
                inventario[producto] += unidades
                print(f"Stock actualizado. Se agregaron {unidades}. Nuevo stock de '{producto}': {inventario[producto]}")
            else:
                # Caso 2: El producto NO EXISTE (Añadir nuevo producto)
                # Se añade el producto con el stock ingresado
                inventario[producto] = unidades
                print(f"Producto nuevo añadido. '{producto}' agregado con stock inicial de {unidades} unidades.")

        elif opcion == '3':
            # --- SALIR ---
            print("\nCerrando el sistema de inventario. ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

# Ejecutar el gestor de inventario
gestionar_inventario()

#9)
print("Actividad 9")
def gestionar_agenda():
    """
    Crea un diccionario de agenda donde las claves son tuplas (día, hora).
    Permite al usuario agregar y consultar eventos.
    """
    # Diccionario inicial con el ejemplo que proporcionaste
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "11:30"): "Almuerzo con cliente"
    }

    print("--- Sistema de Gestión de Agenda ---")

    while True:
        print("\n--- Agenda Actual ---")
        # Imprimir la agenda de forma legible
        for (dia, hora), evento in agenda.items():
            print(f"{dia.capitalize()} a las {hora}: {evento}")
        
        print("\nSelecciona una opción:")
        print("1. Agregar un nuevo evento")
        print("2. Consultar un evento por (Día, Hora)")
        print("3. Salir")

        opcion = input("Ingresa el número de tu elección: ")

        if opcion == '1':
            # --- AGREGAR EVENTO ---
            print("\n--- Agregar Evento ---")
            dia = input("Ingresa el día (ej: Lunes): ").strip().lower()
            hora = input("Ingresa la hora (formato HH:MM, ej: 14:30): ").strip()
            evento = input("Ingresa la descripción del evento: ").strip()

            # La clave es la tupla (dia, hora)
            clave_tupla = (dia, hora)

            if clave_tupla in agenda:
                print(f"¡Atención! Ya hay un evento: '{agenda[clave_tupla]}'")
                confirmacion = input("¿Deseas sobrescribirlo? (s/n): ").lower()
                if confirmacion != 's':
                    print("Operación cancelada.")
                    continue

            agenda[clave_tupla] = evento
            print(f"Evento '{evento}' programado.")

        elif opcion == '2':
            # --- CONSULTAR EVENTO ---
            print("\n--- Consultar Evento ---")
            dia = input("Ingresa el día a consultar: ").strip().lower()
            hora = input("Ingresa la hora a consultar (HH:MM): ").strip()

            clave_tupla = (dia, hora)

            if clave_tupla in agenda:
                print(f"Evento encontrado: '{agenda[clave_tupla]}'")
            else:
                print(f"No hay eventos programados para el {dia.capitalize()} a las {hora}.")

        elif opcion == '3':
            # --- SALIR ---
            print("\nCerrando la agenda. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

# Ejecutar el programa
gestionar_agenda()


#10)
print("Actividad 10")
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "España": "Madrid", "Francia": "París"}
invertido = {}

# Recorrer el diccionario original
for pais, capital in original.items():
    # Asignar el valor (capital) como la nueva clave, 
    # y la clave (país) como el nuevo valor.
    invertido[capital] = pais

print("--- Diccionario Invertido (Bucle For) ---")
print(invertido)