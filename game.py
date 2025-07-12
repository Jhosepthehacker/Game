import random
from time import sleep

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

options = [f"######################",
           f"{GREEN} Adivinanza    ",
           f"{RED}   Combate       ",
           f"######################"
          ]

def game():
    name = input("¿Hola, usuario ¿Cómo te llamas?: ")
    print(f"\n¡Que bonito nombre {name}\n")
    question = input(f"{name}, ¿Quiéres jugar?: ").lower()

    if question == "si" or question == "sí" or question == "si " or question == "sí ":
        print("\nComenzando el juego....\n")
        sleep(1)
        global options # Por si acaso, aunque no creo que sea necesario
        for i in options:
            print(i)
          
        enter = input(f"\n{name} ¿Cuál elijes?: ").lower()

        if enter == "adivinanzas":
            print("\nGenerando el juego....\n")
            sleep(1)
            random.randint(1, 100)
            intentos = 0
            while True:
                try:
                    user = int(input(f"Adivina un número del 1 al 100: "))
                except ValueError:
                    pass
                
