#!/bin/bash
## El bucle until
# Un bucle until se ejecuta hasta que el test resulte falso

echo "Estructura until"

cont=15
until [ $cont -lt 0 ]
do
  cont=`expr $cont - 1`
  echo "Valor del contador: ${cont}"
done

echo "Valor final del contador: ${cont}"
