#!/bin/bash
# señales

funcion () {
  echo "Se ha recibido una señal: ${FUNCNAME} ${0}"
  #exit
}

# Lo primero es establecer que señales se atraparán. Lo hacemos con trap
# Con esto evitaremos que se haga caso a Ctrl C CTRL Z
# trap ":" INT QUIT TSTP
# Esto es similar pero al recibir la señal dirigimos la ejecución a la función

trap "funcion" INT QUIT TSTP

breaker=0
# Un bucle sin fin para probar
while [[ breaker -lt 8 ]]
do
  sleep 1
  echo "ufff qué sueño..."

  ((breaker++))
done
