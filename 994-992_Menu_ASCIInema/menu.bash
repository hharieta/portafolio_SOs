#!/usr/bin/env bash
#
# Author: Gatovsky
#
# Me menu interactivo para los scripts de la guía
# Taller Shell, comandos y programación de 4Party


# Colores
verde_negrita="\033[1;32m"
cian_debil="\033[2;36m"
amarillo_negrita="\033[1;33m"
morado_negrita="\033[1;35m"
rojo_negrita="\033[1;31m"
fin_color='\033[0;m'

garage=scripts

function opciones {
    cat << EOF
    **************************************
            Menu de Scripts Shell
    **************************************

    1)  HolaMundo.sh               11) For.sh
    2)  HolaMundoVars.sh           12) While.sh
    3)  Variables.sh               13) Unitl.sh
    4)  Arrays.sh                  14) Select.sh
    5)  VariablesUso.sh            15) Funciones.sh
    6)  OperAritméticas.sh         16) Librerías.sh
    7)  OperLógicas.sh             17) Señales.sh
    8)  Condicionales.sh           18) ColoresANSI.sh
    9)  ComprobarFicheros.sh       0)  SALIR
    10) CASE.sh
  
EOF
}


### MAIN ####

while true
do
    opciones

    echo -e "${morado_negrita}Seleciona el script ${cian_debil} 1-19 ${fin_color} | ${cian_debil} 0: ${amarillo_negrita}Salir del menú ${fin_color} | >"
    read input

    case $input in
        "0")
            break
            ;;
        "1")
            source $garage/HolaMundo.sh
            ;;
        "2")
            source $garage/HolaMundoVars.sh
            ;;
        "3")
            source $garage/Variables.sh
            ;;
        "4")
            source $garage/Arrays.sh
            ;;
        "5")
            source $garage/VariablesUso.sh
            ;;
        "6")
            source $garage/OperAritméticas.sh
            ;;
        "7")
            source $garage/OperLógicas.sh
            ;;
        "8")
            source $garage/Condicionales.sh
             ;;
         "9")
             source $garage/ComprobarFicheros.sh hola
             ;;
         "10")
             source $garage/CASE.sh
             ;;
         "11")
             source $garage/For.sh
             ;;
         "12")
             source $garage/While.sh
             ;;
         "13")
             source $garage/Unitl.sh
             ;;
         "14")
             source $garage/Select.sh
             ;;
         "15")
             source $garage/Funciones.sh
             ;;
         "16")
             source $garage/Librerías.sh
             ;;
         "17")
             source $garage/Señales.sh
             ;;
         "18")
             source $garage/ColoresANSI.sh
             ;;
        *) 
            set -a
            ;;
    esac

    sleep 0.4

done

