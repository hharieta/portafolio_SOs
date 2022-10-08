#!/bin/bash

# Colores
verde_negrita="\033[1;32m"
cian_debil="\033[2;36m"
amarillo_negrita="\033[1;33m"
morado_negrita="\033[1;35m"
rojo_negrita="\033[1;31m"
fin_color='\033[0;m'

clave=396540


function jail {
    bash -c " chmod 755 comedor/.miau; exec /usr/bin/env bash --rcfile <(echo 'PS1=\"${rojo_negrita}(gatovsky-jail) ${verde_negrita}\${PS1}\"') -i"
}


while [[ $pass -ne $clave ]]
do 
  jail

  echo -e "${amarillo_negrita}Te la creíste wey!! \n${cian_debil}Ingresa la clave para salir: "
  read pass
  
done

# No te wa dejar ver fuera de aquí
chmod 111 comedor/.miau

echo -e "${morado_negrita}[*] Adiós... vuelva pronto.${fin_color}"