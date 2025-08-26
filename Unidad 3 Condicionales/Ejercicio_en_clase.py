# Ejercicio en clase (condicional)

# Primero resuelvo que el programa pida la fecha y la separe en día de la semana y en números.
fecha = input("Ingrese una fecha en formato 'día, DD/MM': ")
# Separamos el texto en dos partes: el día de la semana y el número de fecha
dia_semana, num_fecha = fecha.split(",") #Uso "split()" para separar con coma
dia_semana = dia_semana.strip().lower() #Uso strip para quitar los espacios en blanco extra y lower para pasarlo a minúsculas para comparar fácil
# Separamos la parte numérica en día y mes (con la barra / como separador)
dia, mes = num_fecha.strip().split("/")
# Convertimos las partes de día y mes a números enteros
dia = int(dia)
mes = int(mes)

#Luego valido la fecha usando condicional
if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Error: la fecha ingresada no es válida.")
    exit()

# Determino qué nivel corresponde al día de la semana 
if dia_semana == "lunes":
    nivel = "inicial"
elif dia_semana == "martes":
    nivel = "intermedio"
elif dia_semana == "miercoles":
    nivel = "avanzado"
elif dia_semana == "jueves":
    nivel = "práctica hablada"
elif dia_semana == "viernes":
    nivel = "ingles para viajeros"
else:
    print("Error: el día de la semana no es válido.")
    exit()

# Según el nivel, se ejecuta lo que corresponde
#Caso 1: Niveles con exámenes
if nivel in ["inicial", "intermedio", "avanzado"]:
    examenes = input("¿Se tomaron exámenes? (si/no): ").lower()
    if examenes == "si":
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
        total = aprobados + desaprobados
        #Calculamos porcentaje solo si hay alumnos cargados
        if total > 0:
            porcentaje = (aprobados / total) * 100
            print(f"Porcentaje de aprobados: {porcentaje:.2f}%")
        else:
            print("No hubo alumnos cargados.")
    else:
        print("No se tomaron exámenes.")

#Caso 2: Práctica hablada (solo asistencia)
elif nivel == "práctica hablada":
    asistencia = float(input("Ingrese el porcentaje de asistencia (%): "))
    if asistencia > 50:
        print("Asistió la mayoría.")
    else:
        print("No asistió la mayoría.")

#Caso 3: Inglés para viajeros
elif nivel == "ingles para viajeros":
    if dia == 1 and (mes == 1 or mes == 7):
        print("Comienzo de nuevo ciclo.")
        alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = float(input("Ingrese el arancel por alumno ($): "))
        ingreso_total = alumnos * arancel
        print(f"Ingreso total: ${ingreso_total}")
    else:
        #Si no es inicio de ciclo, solo mostramos un mensaje simple
        print("Clase de inglés para viajeros (sin novedades especiales).")