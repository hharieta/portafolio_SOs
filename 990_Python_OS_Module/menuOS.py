from fileinput import fileno
import os
import asyncio
import sys
from sys import stderr, stdout
import re, fileinput, pathlib


# Colores
verde_negrita = "\033[1;32m"
cian_debil = "\033[2;36m"
amarillo_negrita = "\033[1;33m"
morado_negrita = "\033[1;35m"
rojo_negrita = "\033[1;31m"
fin_color = '\033[0;m'


def opciones(opcion):
    match opcion:
        case "1":
            print(os.name)
            print("\n{}[*] {}nombre del módulo dependiente del sistema operativo importado{}".format(verde_negrita, cian_debil, fin_color))
        case "2":
            print(os.uname())
            print("\n{}[*] {}información que identifica el sistema operativo actual{}".format(verde_negrita, cian_debil, fin_color))
        case "3":
            print(os.ctermid())
            print("\n{}[*] {}terminal de control del proceso{}".format(verde_negrita, cian_debil, fin_color))
        case "4":
            # intente os.environ['VARIABLE_ENTORNO'] 
            print(os.environ)
            print("\n{}[*] {}variables de entorno del sistema{}".format(verde_negrita, cian_debil, fin_color))
        case "5":
            # Bytes version of os.environ
            print(os.environb)
            print("\n{}[*] {}variables de entorno del sistema en bytes{}".format(verde_negrita, cian_debil, fin_color))
            print("\n{}[*] {}environb solo está disponible si support_bytes_environ es {}True {}".format(rojo_negrita, amarillo_negrita, morado_negrita, fin_color))
        case "6":
            os.chdir("/home/"+os.getlogin())
            print(os.getcwd())
            print("\n{}[*] {}cambio de derectorio a $HOME del usuario{}".format(verde_negrita, cian_debil, fin_color))
        case "7":
            fd = os.open("/home/"+os.getlogin()+"/portafolio_SOs", os.O_RDONLY)
            os.fchdir(fd)
            print(os.getcwd())
            print("\n{}[*] {}cambio de derectorio con un file descriptor{}".format(verde_negrita, cian_debil, fin_color))
        case "8":
            print(os.getcwd())
            print("\n{}[*] {}devuelve un string de la ruta actual {}".format(verde_negrita, cian_debil, fin_color))
        case "9":
            print(os.fsencode("hola2.txt"))
            print("\n{}[*] {}codifica el nombre de archivo similar a una ruta; devuelve bytes sin cambios{}".format(verde_negrita, cian_debil, fin_color))
        case "10":
            print(os.fsdecode("hola2.txt"))
            print("\n{}[*] {}decodifica el nombre de archivo similar a una ruta; devuelve str sin cambios{}".format(verde_negrita, cian_debil, fin_color))
        case "11":
            print(os.fspath(os.getcwd()))
            print("\n{}[*] {}Devuelve la representación del sistema de archivos de la ruta.{}".format(verde_negrita, cian_debil, fin_color))
        case "12":
            pass
        case _:
            print("\n{}[*] {}Opción no válida {}".format(rojo_negrita, amarillo_negrita, fin_color))
            exit
        

def menu():
    while True:
        input("Presione ENTER para continuar > ")
        os.system('clear')

        print("""
        **************************************
        Menú para interactuar con el módulo OS
        **************************************

        +++ Opciones en """ + os.path.splitext(os.path.basename(__file__))[0] + """ +++
        
        Parámetros de procesos:
            1)  os.name
            2)  os.uname()
            3)  os.ctermid()
            4)  os.environ
            5)  os.environb
            6)  os.chdir()
            7)  os.fchdir()
            8)  os.getcwd()
            9)  os.fsencode()
            10) os.fsdecode()
            11) os.fspath()
            12) Class os.PathLike()
            0) exit
        """)
        opcion = input("\n> ")

        if opcion == "0": break
        elif opcion.isnumeric():
            opciones(opcion)
        else:
            print("\n{}[*] {}Opción no renococida{}".format(rojo_negrita, amarillo_negrita, fin_color))


def main():
    menu()


if __name__ == '__main__':
    main()
