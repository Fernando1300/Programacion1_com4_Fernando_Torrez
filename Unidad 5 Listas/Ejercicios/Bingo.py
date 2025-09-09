# -- Ejercicio en clase -- #

    # ---BINGO--- #

import random

# Genero un cartón 5x5 con números únicos del 1 al 50
num = random.sample(range(1, 51), 25)   #elige 25 números distintos al azar entre 1 y 50
print("Tu cartón:")
carton = [num[i*5:(i+1)*5] for i in range(5)]  #los acomoda en una matriz 5x5

# Muestro el cartón inicial
for fila in carton:
    print(fila)

# Preparo la lista de sorteos (del 1 al 50)
numeros_sorteo = list(range(1, 51))  #lista con los 50 números
random.shuffle(numeros_sorteo)       #mezclar la lista al azar

# Saca numero sin repetir 
while numeros_sorteo:   #mientras queden números para sacar
    n = numeros_sorteo.pop(0)   #saca el primer número de la lista
    print(f"\nNúmero sorteado: {n}")
    
    encontrado = False
    # Reviso si está en el cartón
    for i in range(5):
        for j in range(5):
            if carton[i][j] == n:
                carton[i][j] = 0
                encontrado = True
    if not encontrado:
        print("No aparece en el cartón.")
    
    # Muestro el cartón actualizado
    for fila in carton:
        print(fila)
    
    # Verifico si ya es BINGO
    if all(all(num == 0 for num in fila) for fila in carton):
        print("\n🎉 ¡BINGO! El cartón está completo 🎉")
        break
