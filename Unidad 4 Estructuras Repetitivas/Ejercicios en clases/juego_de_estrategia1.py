# Defino el alfabeto español con 27 letras (incluye la ñ)
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
# Pido al usuario la cantidad de posiciones que queremos correr cada letra (corrimiento) lo pido una sola vez
corrimiento = int(input("Ingrese un número entre 1 y 26: ")) 

# Mostrar la tabla de corrimiento
for i in alfabeto:
    indice_letra = alfabeto.index(i)  #Buscamos la posición de la letra en el alfabeto
    nuevo_indice = (indice_letra + corrimiento) % 27 #Calculamos la nueva posición sumando el corrimiento y usando módulo 27
    print(i, "→", alfabeto[nuevo_indice])  #Mostramos la letra original y la letra encriptada

print("\nAhora encriptaremos 5 mensajes...\n")

# Hago un bucle para pedir y encriptar 5 mensajes consecutivos
for num in range(1, 6):
    mensaje = input(f"Ingrese el mensaje {num}: ")
    mensaje_encriptado = ""

# Recorro cada letra del mensaje (lo convertimos a minúscula)
    for letra in mensaje.lower():
        if letra in alfabeto:  #Si es una letra
            indice_letra = alfabeto.index(letra)
            nuevo_indice = (indice_letra + corrimiento) % 27 
            mensaje_encriptado += alfabeto[nuevo_indice]
        else:
            mensaje_encriptado += letra  #Deja espacios o símbolos igual 

    # Mostramos el mensaje original y el encriptado
    print("Mensaje original:   ", mensaje)
    print("Mensaje encriptado: ", mensaje_encriptado, "\n")
