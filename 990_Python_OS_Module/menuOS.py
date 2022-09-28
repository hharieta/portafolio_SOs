import os
import asyncio
import sys
from sys import stderr, stdout

"""
Menú para interactuar con el módulo OS
"""

def opciones(opcion):
    match opcion:
        case "1":
            print(os.name)
            
        case "2":
            # imprime todas las variables de entorno del sistma
            # intente os.environ['VARIABLE_ENTORNO'] 
            print(os.environ)
            print("\033[1;32m"+"[*] \033[2;36m"+"variables de entorno del sistema"+'\033[0;m')
        case _:
            exit
        

def menu():
    while True:
        input("Presione ENTER para continuar > ")
        os.system('clear')

        print("""
        Uso: """ + os.path.basename(__file__) + """ [OPCIONES]
        Puede elegir entre las siguientes opciones :
            --1) os.name
            --2) os.environ
            --0) exit
        """)
        opcion = input("\n> ")

        if opcion == "0": break
        else:
            opciones(opcion)


def main():
    menu()


if __name__ == '__main__':
    main()
