            # ---Actividades--- #

# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad
print("Actividad 1")
# Nombre del archivo que vamos a crear
nombre_archivo = "productos.txt"

# Datos a escribir en el archivo, siguiendo el formato: nombre,precio,cantidad
datos_productos = [
    "Laptop,850.50,15",
    "Mouse inalambrico,25.99,50",
    "Teclado mecanico,95.00,20"
]

# Abrir el archivo en modo escritura ('w')
# 'w' sobrescribe el archivo si ya existe.
try:
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        # Escribir cada línea en el archivo
        for linea in datos_productos:
            archivo.write(linea + '\n')
            
    print(f"✅ Archivo '{nombre_archivo}' creado exitosamente con el siguiente contenido:")
    for linea in datos_productos:
        print(f"   {linea}")

except IOError:
    print(f"❌ Error al intentar escribir el archivo '{nombre_archivo}'.")


# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
# formato: 
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30 
print("Actividad 2")

def leer_y_mostrar_productos(nombre_archivo="Productos.txt"):
    """
    Abre un archivo de texto, lee cada línea, la procesa y muestra los datos
    de los productos en un formato específico.
    """
    try:
        # Abrir el archivo en modo lectura ('r')
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            print(f"--- Listado de Productos desde '{nombre_archivo}' ---")
            
            # Leer cada línea del archivo
            for linea in archivo:
                # 1. Procesar la línea: Eliminar espacios y saltos de línea (.strip())
                linea_limpia = linea.strip()

                # 2. Separar los campos usando la coma como delimitador (.split(","))
                # Esto crea una lista: [nombre, precio, cantidad]
                campos = linea_limpia.split(',')
                
                # Asegurarse de que hay al menos 3 campos
                if len(campos) >= 3:
                    nombre = campos[0].strip()
                    precio = campos[1].strip()
                    cantidad = campos[2].strip()

                    # 3. Mostrar el producto en el formato solicitado
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
                else:
                    print(f"⚠️ Advertencia: Línea con formato incorrecto omitida: {linea_limpia}")

    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró. Asegúrate de haberlo creado.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

# Ejecutar la función
leer_y_mostrar_productos()

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
# cantidad) y lo agregue al archivo sin borrar el contenido existente. 
print("Actividad 3")

import os

def gestionar_productos(nombre_archivo="productos.txt"):
    """
    1. Lee y muestra los productos existentes en el archivo.
    2. Solicita al usuario un nuevo producto y lo agrega al archivo.
    """
    
    #  Parte 1: Leer y mostrar productos existentes 
    print("\n" + "="*40)
    print("--- 1. Productos Existentes ---")
    print("="*40)
    
    productos_encontrados = False

    try:
        # Abrir el archivo en modo lectura ('r')
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                campos = linea_limpia.split(',')
                
                if len(campos) >= 3:
                    nombre = campos[0].strip()
                    precio = campos[1].strip()
                    cantidad = campos[2].strip()
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
                    productos_encontrados = True
            
            if not productos_encontrados:
                print("El archivo está vacío o no tiene productos válidos.")


    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró. Se creará uno al agregar.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado durante la lectura: {e}")

    
    # --- Parte 2: Agregar nuevo producto desde teclado ---
    print("\n" + "="*40)
    print("--- 2. Agregar Nuevo Producto ---")
    print("="*40)

    # 1. Solicitar los datos del nuevo producto
    try:
        nuevo_nombre = input("Ingrese el nombre del nuevo producto: ").strip()
        nuevo_precio = float(input("Ingrese el precio del nuevo producto (ej: 120.50): "))
        nueva_cantidad = int(input("Ingrese la cantidad del nuevo producto (entero): "))
        
        # Formatear la nueva línea de datos
        # Usamos f-string y aseguramos que el precio tenga 2 decimales para consistencia
        nueva_linea = f"{nuevo_nombre},{nuevo_precio:.2f},{nueva_cantidad}\n"
        
        # 2. Abrir el archivo en modo APPEND ('a') para agregar al final
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(nueva_linea)
            
        print("\n✅ Producto agregado exitosamente al archivo.")
        print(f"   Datos agregados: {nueva_linea.strip()}")
        
    except ValueError:
        print("❌ Error de entrada: Asegúrate de ingresar un número para el precio y la cantidad.")
    except Exception as e:
        print(f"❌ Ocurrió un error al intentar escribir en el archivo: {e}")


# Ejecutar la función principal
gestionar_productos()

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
# una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad. 

print("Actividad 4")

import os

def cargar_productos_a_diccionario(nombre_archivo="productos.txt"):
    """
    Lee el archivo productos.txt y carga los datos en una lista de diccionarios.
    Cada diccionario tiene las claves: 'nombre', 'precio' (float) y 'cantidad' (int).
    """
    productos = []
    
    try:
        # Abrir el archivo en modo lectura ('r')
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            print(f"--- Cargando datos desde '{nombre_archivo}' ---")
            
            for linea in archivo:
                linea_limpia = linea.strip()
                campos = linea_limpia.split(',')
                
                # Asegurarse de que hay 3 campos y que no es una línea vacía
                if len(campos) == 3 and linea_limpia:
                    try:
                        # Convertir los tipos de datos: precio a float, cantidad a int
                        nombre = campos[0].strip()
                        precio = float(campos[1].strip())
                        cantidad = int(campos[2].strip())
                        
                        # Crear el diccionario para el producto
                        producto_dict = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad
                        }
                        
                        # Agregar el diccionario a la lista
                        productos.append(producto_dict)
                        
                    except ValueError:
                        print(f"⚠️ Advertencia: Error en la conversión de tipo en la línea: {linea_limpia}. Omitida.")
                
        print("✅ Carga de datos completada.")
        
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

    return productos

#  Ejecución 

# 1. Cargar la lista de diccionarios
lista_productos = cargar_productos_a_diccionario()

# 2. Mostrar la estructura de la lista y el contenido cargado para verificar
print("\n--- Estructura de la Lista de Diccionarios ---")
print(lista_productos)

# Opcional: Mostrar los tipos de datos
if lista_productos:
    primer_producto = lista_productos[0]
    print(f"\nTipo de dato de 'precio': {type(primer_producto['precio'])}")
    print(f"Tipo de dato de 'cantidad': {type(primer_producto['cantidad'])}")

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
# no existe, mostrar un mensaje de error. 

print("Actividad 5")

def cargar_productos_a_diccionario(nombre_archivo="productos.txt"):
    """
    Lee el archivo y carga los datos en una lista de diccionarios.
    (Función reutilizada del paso 4)
    """
    productos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                campos = linea_limpia.split(',')
                if len(campos) == 3 and linea_limpia:
                    try:
                        nombre = campos[0].strip()
                        precio = float(campos[1].strip())
                        cantidad = int(campos[2].strip())
                        
                        producto_dict = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad
                        }
                        productos.append(producto_dict)
                    except ValueError:
                        pass # Ignorar líneas con errores de tipo
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró.")
    return productos

def buscar_producto_por_nombre(lista_productos):
    """
    Pide al usuario el nombre de un producto y busca sus datos en la lista.
    """
    print("\n" + "="*40)
    print("--- 5. Buscar Producto por Nombre ---")
    print("="*40)
    
    # Pedir el nombre al usuario y limpiar el espacio en blanco (strip())
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    
    producto_encontrado = None
    
    # Recorrer la lista de diccionarios
    for producto in lista_productos:
        # La condición de búsqueda es si el nombre del diccionario coincide
        if producto["nombre"].lower() == nombre_buscado.lower():
            producto_encontrado = producto
            break # Detenemos el bucle una vez que encontramos el producto
            
    # Mostrar el resultado
    if producto_encontrado:
        print("\n✅ Producto encontrado:")
        print(f"   Nombre: {producto_encontrado['nombre']}")
        print(f"   Precio: ${producto_encontrado['precio']:.2f}")
        print(f"   Cantidad en Stock: {producto_encontrado['cantidad']}")
    else:
        print(f"\n❌ Error: El producto '{nombre_buscado}' no existe en el inventario.")

#  Ejecución Principal 

# 1. Cargar los datos del archivo
lista_productos = cargar_productos_a_diccionario()

# 2. Ejecutar la búsqueda solo si se cargaron productos
if lista_productos:
    buscar_producto_por_nombre(lista_productos)

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
# productos actualizados desde la lista. 

def cargar_productos_a_diccionario(nombre_archivo="productos.txt"):
    """Lee el archivo y carga los datos en una lista de diccionarios."""
    productos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                campos = linea_limpia.split(',')
                if len(campos) == 3 and linea_limpia:
                    try:
                        nombre = campos[0].strip()
                        # Convertir a float y int para mantener los tipos de datos correctos
                        precio = float(campos[1].strip())
                        cantidad = int(campos[2].strip())
                        
                        producto_dict = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad
                        }
                        productos.append(producto_dict)
                    except ValueError:
                        print(f"⚠️ Advertencia: Error de formato en la línea: {linea_limpia}. Omitida.")
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró. Iniciando con lista vacía.")
    return productos

#  NUEVA FUNCIÓN PARA GUARDAR DATOS (Paso 6)

def guardar_productos_actualizados(productos, nombre_archivo="productos.txt"):
    """
    Sobrescribe el archivo de texto con el contenido actual de la lista de diccionarios.
    """
    print("\n" + "="*40)
    print(f"--- 6. Guardando Productos en '{nombre_archivo}' ---")
    print("="*40)
    
    try:
        # Abrir el archivo en modo ESCRITURA ('w') para SOBRESCRIBIR todo el contenido
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            for producto in productos:
                # Formato: nombre,precio,cantidad
                # Usamos :.2f para asegurar que el precio se guarda con 2 decimales
                linea = f"{producto['nombre']},{producto['precio']:.2f},{producto['cantidad']}\n"
                archivo.write(linea)
            
        print("✅ Inventario guardado exitosamente. El archivo ha sido actualizado.")
        
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

#  Búsqueda y Modificación (Demostración de un cambio) 

def buscar_y_agregar_stock(lista_productos):
    """Función de ejemplo para demostrar que la lista se puede modificar."""
    print("\n--- DEMO: Agregando Stock a Laptop ---")
    
    for producto in lista_productos:
        if producto['nombre'].lower() == 'laptop':
            stock_a_agregar = 5
            producto['cantidad'] += stock_a_agregar
            print(f"Stock de {producto['nombre']} actualizado. Nuevo stock: {producto['cantidad']}")
            return

    # Si no se encuentra el producto, se puede agregar uno nuevo para demostrar la escritura
    nuevo_producto = {
        "nombre": "Auriculares Pro",
        "precio": 150.99,
        "cantidad": 30
    }
    lista_productos.append(nuevo_producto)
    print(f"Producto '{nuevo_producto['nombre']}' añadido a la lista.")


#  EJECUCIÓN PRINCIPAL DEL PROGRAMA 

# 1. Cargar los datos a la lista de diccionarios (Paso 4)
lista_productos = cargar_productos_a_diccionario()
print(f"Total de productos cargados: {len(lista_productos)}")

# 2. Realizar alguna modificación o adición (Simulación)
buscar_y_agregar_stock(lista_productos)

# 3. Guardar la lista actualizada de vuelta al archivo (Paso 6)
guardar_productos_actualizados(lista_productos)