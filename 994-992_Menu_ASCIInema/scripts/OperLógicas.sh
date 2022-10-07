#!/bin/bash
## operaciones lógicas
# && : and
# || : or
# ! : not
booleano=true
# Si la variable booleano es true veremos por pantalla "OK"
$booleano && echo "OK" || echo "no es true"
otrobool=!${booleano}

test ${otrobool} || echo "Ahora es falso"
# Mediante && podemos encadenar comandos
#who && ps axf && echo "OK"
## comparaciones : eq, ne, lt, le, gt, or ge
valor=6
test $valor -le 6 && echo "Se cumple"
# Asignaciones
nuevo=${valor}
test ${nuevo} -eq ${valor} && echo "Son los mismo"
echo "Ahora ${nuevo} es lo mismo que ${valor}"
