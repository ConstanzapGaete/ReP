import random

options = ["Piedra", "Papel", "Tijeras"]

print("Bienvenido a piedra, papel o tijeras")
print("Elige uno y escribelo")
print("El computador elegirá también y competirá contra ti")
print("Buena suerte!")
print("")

player_choice = input(
    "Qué vas a elegir? Piedra, papel o tijeras: ").capitalize()
print("")

computer_choice = random.choice(options)

print(f"Elegiste '{player_choice}'")
print(f"El computador eligió '{computer_choice}'")
print("")

if player_choice == "Piedra" and computer_choice == "Papel":
    print("El computador ganó!")
elif player_choice == "Papel" and computer_choice == "Piedra":
    print("Ganaste!")
elif player_choice == "Tijeras" and computer_choice == "Piedra":
    print("El computador ganó!")
elif player_choice == "Piedra" and computer_choice == "Tijeras":
    print("Ganaste!")
elif player_choice == "Papel" and computer_choice == "Tijeras":
    print("El computador ganó!")
elif player_choice == "Tijeras" and computer_choice == "Papel":
    print("Ganaste!")
else:
    print("Empate!")