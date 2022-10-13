import os
import PARAMETROS_PROCESOS as P
import colors as c


def llamar_submenu(op):
    match op:
        case "A":
            P.submenup()
        case _:
            pass


def menu():
    while True:
        print("""
        **************************************
        Menú para interactuar con el módulo OS
        **************************************

        +++ Opciones en """ + os.path.splitext(os.path.basename(__file__))[0] + """ +++
        
        A) Parámetros de procesos:
        S) exit
        """)
        opcion = input("\n> ")

        if opcion == "S": break
        elif opcion.isalpha:
            llamar_submenu(opcion)
        else:
            print("\n{}[*] {}Opción no válida {}".format(c.rojo_negrita(), c.amarillo_negrita(), c.fin_color()))
        
        os.system('clear')


def main():
    menu()


if __name__ == '__main__':
    main()
