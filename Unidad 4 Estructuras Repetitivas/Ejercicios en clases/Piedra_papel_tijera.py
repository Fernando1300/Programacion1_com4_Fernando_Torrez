import random

victorias = 0
derrotas = 0
empates = 0
continuar = 1

while continuar == 1:
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    opcionUsuario = int(input("Tu elección (1/2/3): "))

    if opcionUsuario < 1 or opcionUsuario > 3:
        print("Opción inválida. Intenta de nuevo.")
        continue  # vuelve al inicio del while

    # Elección de la PC
    opcionPC = random.randint(1, 3)

    # Traducción de números a texto
    if opcionUsuario == 1:
        Usuario = "Piedra"
    elif opcionUsuario == 2:
        Usuario = "Papel"
    else:
        Usuario = "Tijera"

    if opcionPC == 1:
        PC = "Piedra"
    elif opcionPC == 2:
        PC = "Papel"
    else:
        PC = "Tijera"

    # Mostrar elecciones
    print("Tú elegiste:", Usuario)
    print("La computadora eligió:", PC)

    # Lógica del juego
    if opcionUsuario == opcionPC:
        print("¡Empate!")
        empates += 1
    elif (opcionUsuario == 1 and opcionPC == 3) or \
         (opcionUsuario == 2 and opcionPC == 1) or \
         (opcionUsuario == 3 and opcionPC == 2):
        print("¡Ganaste!")
        victorias += 1
    else:
        print("Perdiste :(")
        derrotas += 1

    # Preguntar si se sigue jugando
    continuar = int(input("¿Deseas jugar otra vez? (1: Sí, 0: No): "))

# Resumen
print("\nResumen del juego:")
print("Victorias:", victorias)
print("Derrotas:", derrotas)
print("Empates:", empates)

