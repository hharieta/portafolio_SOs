#!/usr/bin/env bash
# Author: Gatovsky

# Colors
greenColor="\e[0;32m\033[1m"
endColor="\033[0m\e[0m"
redColor="\e[0;31m\033[1m"
blueColor="\e[0;34m\033[1m"
yellowColor="\e[0;33m\033[1m"
purpleColor="\e[0;35m\033[1m"
turquoiseColor="\e[0;36m\033[1m"
greyColor="\e[0;37m\033[1m"


DIR=$HOME/portafolio_SOs/990_Python_OS_Module
ENV_NAME=env

usage() {
    cat << EOF
        Uso: $0 [ OPTIONS ]

            -v: Crea un entorno virtual de nombre $ENV_NAME por defecto
            -a: Activa el entorno virtual $ENV_NAME
            -d: Desactiva el entorno virtual $ENV_NAME
            -r: Elimina el entorno virtual $ENV_NAME de la ruta actual
            -h: muestra la ayuda

        Ejemplo: $0 -va
EOF
    exit 0
}


### MAIN ###
while getopts "vadrh" arg; do
    case "${arg}" in
        v)
            echo -e "${greenColor}[*]${endColor}${turquoiseColor} Creando entorno virtual...${endColor}"
            sleep 0.5
            python3 -m venv $ENV_NAME
            ;;
        a)
            echo -e "${greenColor}[*]${endColor}${turquoiseColor} Activando entorno virtual...${endColor}"
            sleep 0.5
            source $ENV_NAME/bin/activate
            ;;
        d)
            echo -e "${greenColor}[*]${endColor}${turquoiseColor} Desactivando entorno virtual...${endColor}"
            sleep 0.5
            deactivate
            ;;
        r)
            echo -e "${redColor}[*]${endColor}${yellowColor} Eliminando entorno virtual...${endColor}"
            sleep 0.5
            rm -rf $DIR/$ENV_NAME
            ;;
        h)
            usage
            ;;
        *)
            echo -e "Mira $0 -h\n"
            ;;
    esac
done

