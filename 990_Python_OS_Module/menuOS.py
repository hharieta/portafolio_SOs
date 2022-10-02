import os
import asyncio
import sys
from sys import stderr, stdout
import re

def opciones(opcion):
    match opcion:
        case "1":
            print(os.name)
            print("\n\033[1;32m"+"[*] \033[2;36m"+"nombre del módulo dependiente del sistema operativo importado"+'\033[0;m')
        case "2":
            print(os.uname())
            print("\n\033[1;32m"+"[*] \033[2;36m"+"información que identifica el sistema operativo actual"+'\033[0;m')
        case "3":
            print(os.ctermid())
            print("\n\033[1;32m"+"[*] \033[2;36m"+"terminal de control del proceso"+'\033[0;m')
        case "4":
            # intente os.environ['VARIABLE_ENTORNO'] 
            print(os.environ)
            print("\n\033[1;32m [*]" + " \033[2;36m variables de entorno del sistema"+'\033[0;m')
        case "5":
            # Bytes version of os.environ
            print(os.environb)
            print("\n\033[1;32m [*]" + " \033[2;36m variables de entorno del sistema en bytes"+'\033[0;m')
            print("\033[1;33m [*]" + " \033[1;33m environb solo está disponible si support_bytes_environ es" + "\033[1;35m True" +'\033[0;m')
        case "6":
            os.chdir("/home/gatovsky")
            print(os.getcwd())

        case _:
            print("\n\033[1;31m [*]" + " \033[1;33m Opción no válida"+'\033[0;m')
            exit
        

def menu():
    while True:
        input("Presione ENTER para continuar > ")
        os.system('clear')

        print("""
        **************************************
        Menú para interactuar con el módulo OS
        **************************************

        Opciones en """ + os.path.splitext(os.path.basename(__file__))[0] + """
        
        Parámetros de procesos:
            1) os.name
            2) os.uname()
            3) os.ctermid()
            4) os.environ
            5) os.environb
            6) os.chdir
            0) exit
        """)
        opcion = input("\n> ")

        if opcion == "0": break
        elif opcion.isnumeric():
            opciones(opcion)
        else:
            print("\n\033[1;31m [*]" + " \033[1;33m Entrada no numérica"+'\033[0;m')


def main():
    menu()


if __name__ == '__main__':
    main()
