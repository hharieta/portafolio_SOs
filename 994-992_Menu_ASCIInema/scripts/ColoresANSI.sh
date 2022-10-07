#!/bin/bash
## Los colores ANSI
# para darle color a los scripts debemos usar los código ANSI
# junto "con echo e". Para meter el carácter especial escape
# usamos \033
# Ejem: \033[0m : volver al color por defecto
# \033[40m: color de fondo negro
# \033[40m\033[32m: fondo negro primer plano verde
# Esta es la muestra de colores, ejecútalo para ver cómo queda
echo -e "\033[40m\033[37m Blanco \033[0m"
echo -e "\033[40m\033[1;37m Gris claro \033[0m"
echo -e "\033[40m\033[30m Negro \033[0m (esto es negro)"
echo -e "\033[40m\033[1;30m Gris \033[0m"
echo -e "\033[40m\033[31m Rojo \033[0m"
echo -e "\033[40m\033[1;31m Rojo claro \033[0m"
echo -e "\033[40m\033[32m Verde \033[0m"
echo -e "\033[40m\033[1;32m Verde claro \033[0m"
echo -e "\033[40m\033[33m Marrón \033[0m"
echo -e "\033[40m\033[1;33m Amarillo \033[0m"
echo -e "\033[40m\033[34m Azul \033[0m"
echo -e "\033[40m\033[1;34m Azul claro \033[0m"
echo -e "\033[40m\033[35m Purpura \033[0m"
echo -e "\033[40m\033[1;35m Rosa \033[0m"
echo -e "\033[40m\033[36m Cyan \033[0m"
echo -e "\033[40m\033[1;36m Cyan claro \033[0m"

# Se pueden poner fondos de otro color:
echo -e "\033[42m\033[31m Navarrux v1.0 \033[0m"
echo -e "\033[40m\033[4;33m Amarillo \033[0m"
