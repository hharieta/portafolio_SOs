#!/bin/bash
# Condicionales

VARIABLE=45

if [ ${VARIABLE} -gt 0 ]
then
    echo "${VARIABLE} es mayor que 0"
fi

# Podemos meter el then en la siguiente linea
if [ -e /etc/shadow ];then
    echo "OK, parece que tienes un sistema con shadow pass"
fi

## Estructura if else
OTRA=23
if [ ${OTRA} -lt 0 ]; then
    echo "${OTRA} es menor que 0"
else
    echo "${OTRA} es mayor que 0";
fi

## Estructura if elseif
# Vamos a usar "read" para pedirle datos al usuario

echo n "Mete un valor: "
read VALOR1
echo n "Mete otro valor: "
read VALOR2
echo "Has introducido los valores ${VALOR1} y ${VALOR2} "

if [ ${VALOR1} -gt ${VALOR2} ]; then
    echo "${VALOR1} es mayor que ${VALOR2}"
elif [ ${VALOR1} -lt ${VALOR2} ]; then
    echo "${VALOR1} es menor que ${VALOR2}"
else
    echo "${VALOR1} y ${VALOR2} son iguales"
fi

## Estructura test
# Ejecutar operacion si no se cumple la condición
# test condición || operacion
# Ejecutar operación si se cumple
# test condición && operacion
# Este test crea un fichero si no existe.

test -f './fichero.txt' || touch fichero.txt


