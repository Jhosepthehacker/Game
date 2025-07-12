import random
from time import sleep

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

options = [f"######################",
    GREEN + "       Adivinanza     ",
      RED + "       Combate        ",
    RESET + "######################"
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
            number = random.randint(1, 100)
            trys = 0
            while True:
                try:
                    user = int(input(f"Adivina un número del 1 al 100: "))
                except ValueError:
                    print("Ingrese por favor solo números")

                if user > number:
                    print("Demasiado alto")
                elif user < number:
                    print("Demasiado bajo")
                elif user == number:
                    print(f"Felicidades has encontrado el número {number}, en {trys} intentos")
                    break

if __name__ == '__main__':
    game()
