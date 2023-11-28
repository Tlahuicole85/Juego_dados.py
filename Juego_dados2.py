# python Juego_dados2.py _(copia y pega en shell )

import random

option = (1, 2, 3, 4, 5, 6)

user_wins = 0
computer_wins = 0

for _ in range(3):
    # Lanzamiento de dados para el usuario
    user_dice1 = random.choice(option)
    user_dice2 = random.choice(option)
    user_total = user_dice1 + user_dice2

    # Lanzamiento de dados para la computadora
    computer_dice1 = random.choice(option)
    computer_dice2 = random.choice(option)
    computer_total = computer_dice1 + computer_dice2

    print(f"\nUsuario: Dado 1 = {user_dice1}, Dado 2 = {user_dice2}, Total = {user_total}")
    print(f"Computadora: Dado 1 = {computer_dice1}, Dado 2 = {computer_dice2}, Total = {computer_total}")

    if user_total > computer_total:
        user_wins += 1
        print("El usuario gana esta ronda")
    elif computer_total > user_total:
        computer_wins += 1
        print("La computadora gana esta ronda")
    else:
        print("Esta ronda es un empate")

# Determinar al ganador de los 2 de 3 juegos
if user_wins > computer_wins:
    print("\n¡El usuario gana el juego!")
elif computer_wins > user_wins:
    print("\n¡La computadora gana el juego!")
else:
    print("\n¡Es un empate en el juego!")
