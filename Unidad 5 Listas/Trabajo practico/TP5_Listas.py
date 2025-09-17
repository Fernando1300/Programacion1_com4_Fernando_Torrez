#### ---Actividades--- ####

# 1) 
print("Actividad 1")
# Lista con range(4,101,4) empieza en 4, termina en 100 y va de 4 en 4.
primera_lista =  list(range(4,101, 4)) 
# Muestra todos los múltiplos de 4 del 1 al 100
print("Multiplos de 4: ", primera_lista)


# 2) 
print("Actividad 2")
segunda_lista = [True, 5, 2.4, "Hola", -5 ]
print("El penultimo elemento de la lista es: ",segunda_lista[3]) # Accede al elemento en el índice 3 (penúltimo, porque hay 5 elementos).


# 3) 
print("Actividad 3")
# Lista vacia en la cual le agregaremos tres palabras con el uso de "append"
lista_vacia = []
# Agregamos los tres elementos utilizando append
lista_vacia.append("Universidad")
lista_vacia.append("Tecnologica")
lista_vacia.append("Nacional")
print("Los elementos agregados a la lista vacia son: ",lista_vacia)


# 4) 
print("Actividad 4")
lista_animales = ["perro", "gato", "conejo", "pez"] 
# Reemplazar elementos en posiciones específicas de la lista.
lista_animales[1] = "loro" # Reemplaza el valor en índice 1
lista_animales[3] = "oso"  # Reemplaza el valor en índice 3
print("Lista con los animales reemplazados: ",lista_animales)


# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 
print("Actividad 5")
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros)) # Utiliza remove(elementoAEliminar) para eliminar el numero maximo de la lista, que seria "22" el numero maximo.
print(numeros) # Entonces la salida del codigo seria [8, 15, 3, 7], 22 fue el numero que elimino.


# 6) 
print("Actividad 6")
# Genera [10, 15, 20, 25, 30]
tercera_lista =  list(range(10,35, 5)) 
# [:2] devuelve los dos primeros elementos → [10, 15]
print(tercera_lista[:2]) 


# 7) 
print("Actividad 7")
# Reemplazar los valores centrales de la lista.
lista_autos = ["sedan", "polo", "suran", "gol"] 
lista_autos[1] = "fiat" # Reemplaza el índice 1
lista_autos[2] = "toyota" # Reemplaza el índice 2
print("Lista con los valores reemplazados: ",lista_autos)


# 8) 
print("Actividad 8")
# Creo una lista vacia llamada lista_dobles y agrego el doble de 5, 10 y 15 usando append 
lista_dobles = []
lista_dobles.append(5*2)
lista_dobles.append(10*2)
lista_dobles.append(15*2)
print(lista_dobles)


# 9) 
print("Actividad 9")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
# Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo") 
# Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
compras[1][1] = "tallarines" 
# Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan") 
# Imprimir la lista resultante por pantalla 
print("Lista de compras actualizada: ",compras)


# 10) 
print("Actividad 10")
# lista_anidada[0] = 15
# lista_anidada[1] = True
# lista_anidada[2] = [25.5, 57.9, 30.6]  (otra lista dentro)
# lista_anidada[3] = False
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)