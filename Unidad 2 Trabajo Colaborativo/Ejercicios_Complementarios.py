# Ejercicios complementarios

# 1)  
print("Actividad 1")
numero1 = 5 #Creo la variable "numero1" donde guardo mi numero entero asignado (en este caso 5)
print("El numero entero es: ", numero1)

# 2)
print("Actividad 2")
numero2 = 1.4 #Creo la variable "numero2" donde guardo mi numero decimal asignado (en este caso 1.4)
print("El numero decimal es:", numero2)

# 3) 
print("Actividad 3")
suma = numero1 + numero2 #Creo la variable "suma" donde guardo las anteriores variables "numero1" y "numero2"
print("El resultado de suma es: ",suma)

# 4) 
print("Actividad 4")
resta = numero1 - numero2 #Creo la variable "resta" donde guardo y resto "numero1" y "numero2"
multiplicacion = numero1 * numero2 #Creo la variable "multiplicacion" donde guardo y multiplico "numero1" y "numero2"
division = numero1 / numero2 #Creo la variable "division" donde guardo y divido "numero1" y "numero2"
#Luego con print muestro el resultado que da cada variable
print("La suma es: : ",suma) 
print("La resta es: ",resta)
print("La multiplicacion es: ",multiplicacion)
print("La division es: ",division)

# 5)
print("Actividad 5")
nombre = "Fernando" #Creo una variable llamada nombre y agrego mi nombre
print(f"El nombre que agregue es {nombre}")

# 6) 
print("Actividad 6")
precio = 49.99  #Creo una variable llamada precio y le asigno un valor en decimal
print(f"Precio asignado es: {precio}")

# 7) 
print("Actividad 7")
descuento = 0.25 #Creo una variable llamada descuento con el valor 0.25 (equivale al 25%)
monto_descuento = precio * descuento #Calculo el monto del descuento multiplicando el precio por el porcentaje de descuento
print(f"El monto de descuento es: {monto_descuento}")

# 8)  
print("Actividad 8")
precio_final = precio - monto_descuento #Se calcula el precio final restando el monto del descuento al precio original
print("Precio original: ", precio) #Muestra en pantalla el precio original antes del descuento
print("Monto del descuento (25%): ", monto_descuento) #Muestra en pantalla el monto del descuento (en este caso el 25%)
print("Precio final con descuento: ", precio_final) #Muestra en pantalla el precio final después de aplicar el descuento

# 9)  
print("Actividad 9")
cadena = "¡Buenas Tardes!" #Creo una variable llamada cadena, que contiene un texto
print(f"El texo que contiene es: {cadena}")

# 10)    
print("Actividad 10")
longitud = len(cadena) #Creo una variable llamada longitud y la función len() devuelve la cantidad de caracteres de la cadena
print("la longitud de la cadena es: ",longitud) #Se imprime en pantalla un mensaje junto con el valor de longitud

# 11) 
print("Actividad 11")
precio = 49.99 #Creo una variable llamada precio y se le asigna un valor decimal (float)
precio_1 = int(precio) #Creo una nueva variable llamada precio_1 y con la funcion int() convierto el número decimal en un entero
print(precio_1) #Se imprime en pantalla el valor de precio_1

# 12)  
print("Actividad 12")
#Creo 2 variables con el nombre y apellido
nombre = "Fernando"
apellido = "Torrez"
nombre_completo = nombre + " " + apellido #Se concatenan nombre y apellido pero agregando un espacio en medio
print(f"Mi nombre es {nombre_completo}") #Se imprime el nombre completo

# 13) 
print("Actividad 13")
mi_edad = 23 #Creo una variable llamada mi_edad y se le asigna el valor 23
mi_edad = mi_edad + 5 #Se incrementa la edad en 5 (ahora mi_edad vale 28)
mi_edad = mi_edad - 10 #Se disminuye la edad en 10 (ahora mi_edad vale 18)
print(f"El resultado final es de: {mi_edad} años ") #Se imprime en pantalla el valor final de mi_edad

# 14) 
print("Actividad 14")
altura = 1.84 #Se crea una variable llamada altura y se le asigna un valor decimal (metros)
resultado_altura = (altura * 4) / 3 #Se crea otra variable llamada "resultado_altura" donde se multiplica la altura por 4 y luego se divide entre 3
print(resultado_altura) #Se imprime en pantalla el valor calculado

# 15) 
print("Actividad 15")
nombre_mayuscula = "FERNANDO" #Creo una variable llamada nombre_mayuscula y se guarda un texto en MAYÚSCULAS
#Creo una variable llamada minuscula y usamos .lower(), que convierte TODAS las letras de la cadena a minúsculas
minuscula = nombre_mayuscula.lower() 
print(minuscula) #Se imprime el contenido de la variable minuscula en pantalla

# 16) 
print("Actividad 16")
nombre_mayuscula = "FERNANDO" #Creo una variable llamada nombre_mayuscula y se le asigna el texto en MAYÚSCULAS
#Se crea otra variable llamada minuscula y usamos .capitalize() que convierte la primera letra en mayúscula y resto de las letras en minúsculas
minuscula = nombre_mayuscula.capitalize()
print(minuscula) # Muestra en pantalla el resultado de la conversión