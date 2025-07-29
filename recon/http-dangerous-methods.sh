#!/bin/bash

#Colors
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

# Verificar argumento
if [ -z "$1" ]; then
  echo "Uso: $0 <url>"
  exit 1
fi


function ctrl_c(){
  echo -e "${redColour}\n[!] Saliendo...${endColour}\n"
  exit 2
}

trap ctrl_c SIGINT

#url
URL=$1
DANGEROUS_METHODS=("PUT" "DELETE" "TRACE" "CONNECT" "PATCH" "PROPFIND" "SEARCH" "MKCOL" "COPY" "MOVE")

#Ejecutamos scaner de metodos

METHODS=$(curl -s -X OPTIONS "$URL" -i | grep -iE 'public|allow' | cut -d: -f2- | tr -d '\r' | tr ',' '\n' | sed 's/^[ \t]*//' | sort -u)

#Presentacion



echo -e "\n${yellowColour}[+]${endColour}${grayColour} HTTP Methods supothed in ${endColour}${yellowColour}$URL:\n${endColour}"
echo -e "\t${yellowColour}[-]${endColour}${grayColour} $METHODS${endColour}" | tr '\n' ' ' 

echo -e "\n\n${yellowColour}[+]${endColour} ${grayColour}List HTTP Methods pontentialy dangerous\n${endColour}"
for m in $METHODS; do
  for dm in "${DANGEROUS_METHODS[@]}"; do
    if [ $m = $dm ]; then 
      echo -e "\t${redColour}[!] $m${endColour}"
    fi
  done
done



