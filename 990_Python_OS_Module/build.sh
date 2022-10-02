#!/bin/bash
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
ENV=env/bin

if [[ $(pwd) = $DIR ]] && [[ -d env ]]; then
		echo -e "${greenColor}[*]${endColor}${turquoiseColor} 'env' ya existe. Activando entorno virtual...${endColor}"
		sleep 0.5
		source $DIR/$ENV/activate
else
    echo -e "${greenColor}[*]${endColor}${turquoiseColor} Creando entorno virtual...${endColor}"
    sleep 0.5

    python3 -m venv env

	echo -e "${greenColor}[*]${endColor}${turquoiseColor} Activando entorno virtual...${endColor}"
    sleep 0.5

    source $DIR/$ENV/activate
fi


