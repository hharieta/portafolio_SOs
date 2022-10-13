from ast import Bytes
import os
import sys
import colors as c
from sys import stderr, stdout

def submenup():
    while True:
        input("Presione ENTER para continuar > ")
        os.system('clear')

        print("""
        **************************************
        PÁRAMETROS DE PROCESOS MÓDULO OS
        **************************************

        +++ Opciones en """ + os.path.splitext(os.path.basename(__file__))[0] + """ +++
            
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
            12) os.getenv()
            13) os.getenvb()
            14) os.get_exec_path()
            15) os.getegid()
            16) os.geteuid()
            17) os.getgid()
            18) os.getgrouplist()
            19) os.getgroups()
            20) os.getlogin()
            21) os.getpgid()
            22) os.getpgrp()
            0) exit
        """)
        opcion = input("\n> ")

        if opcion == "0": break
        elif opcion.isnumeric():
            process(opcion)
        else:
            print("\n{}[*] {}Opción no renococida{}".format(c.rojo_negrita(), c.amarillo_negrita(), c.fin_color()))


def process(op):
    match op:
        case "1":
            print(os.name)
            print("\n{}[*] {}nombre del módulo dependiente del sistema operativo importado{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "2":
            print(os.uname())
            print("\n{}[*] {}información que identifica el sistema operativo actual{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "3":
            print(os.ctermid())
            print("\n{}[*] {}terminal de control del proceso{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "4":
            # intente os.environ['VARIABLE_ENTORNO'] 
            print(os.environ)
            print("\n{}[*] {}variables de entorno del sistema{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "5":
            # Bytes version of os.environ
            print(os.environb)
            print("\n{}[*] {}variables de entorno del sistema en bytes{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
            print("\n{}[*] {}environb solo está disponible si support_bytes_environ es {}True {}".format(c.rojo_negrita(), c.amarillo_negrita(), c.morado_negrita(), c.fin_color()))
        case "6":
            os.chdir("/home/"+os.getlogin())
            print(os.getcwd())
            print("\n{}[*] {}cambio de derectorio a $HOME del usuario{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "7":
            fd = os.open("/home/"+os.getlogin()+"/portafolio_SOs", os.O_RDONLY)
            os.fchdir(fd)
            print(os.getcwd())
            print("\n{}[*] {}cambio de derectorio con un file descriptor{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "8":
            print(os.getcwd())
            print("\n{}[*] {}devuelve un string de la ruta actual {}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "9":
            print(os.fsencode("hola2.txt"))
            print("\n{}[*] {}codifica el nombre de archivo similar a una ruta; devuelve bytes sin cambios{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "10":
            print(os.fsdecode("hola2.txt"))
            print("\n{}[*] {}decodifica el nombre de archivo similar a una ruta; devuelve str sin cambios{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "11":
            print(os.fspath(os.getcwd()))
            print("\n{}[*] {}Devuelve la representación del sistema de archivos de la ruta.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "12":
            i = input("Escribe una variable de entorno Unix: ")
            print(os.getenv(i))
            print("\n{}[*] {}Devuelve el valor de la clave de la variable de entorno como una cadena si existe.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "13":
            i = input('Escribe una variable de entorno Unix: ')
            key = bytes(i, 'utf-8')
            print(os.getenvb(key))
            print("\n{}[*] {}Devuelve el valor de la clave de la variable de entorno en bytes si existe.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "14":
            print(os.get_exec_path(env=None))
            print("\n{}[*] {}Devuelve la lista de directorios en los que se buscará un ejecutable.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "15":
            print(os.getegid())
            print("\n{}[*] {}Devuelve el ID de grupo efectivo del proceso actual.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "16":
            print(os.geteuid())
            print("\n{}[*] {}Devuelve el ID de usuario efectivo del proceso actual.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "17":
            print(os.getgid())
            print("\n{}[*] {}Devuelve el ID de grupo real del proceso actual.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "18":
            print(os.getgrouplist(os.getlogin(), os.getegid()))
            print("\n{}[*] {}Devuelve la lista de ID de grupo a los que pertenece el usuario.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "19":
            print(os.getgroups())
            print("\n{}[*] {}Devuelve una lista de ID de grupo complementarios asociados con el proceso actual.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "20":
            print(os.getlogin())
            print("\n{}[*] {}Devuelve el nombre del usuario que inició sesión en el terminal de control del proceso.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "21":
            print(os.getpgid(os.getegid()))
            print("\n{}[*] {}Devuelve el ID de proceso de grupo de los procesos con el PID.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case "22":
            print(os.getpgrp())
            print("\n{}[*] {}Devuelve el id del grupo de procesos actual.{}".format(c.verde_negrita(), c.cian_debil(), c.fin_color()))
        case _:
            print("\n{}[*] {}Opción no válida {}".format(c.rojo_negrita(), c.amarillo_negrita(), c.fin_color()))
            exit