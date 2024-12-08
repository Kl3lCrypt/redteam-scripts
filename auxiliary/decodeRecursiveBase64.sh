#!/bin/bash

function ctrl_c(){
  echo -e "[+] Saliendo...\n"
  exit 1
}

#CTRL+C
trap ctrl_c SIGINT


#Verificar si se recibe un archivo o un texto para decodear

if [[ -z "$1" ]];then
  echo "$0 <file_encode>"
  exit 2
fi


# Verificando si es un archivo regular o un codigo base64
if [[ -f "$1" ]];then
  encoded_data=$( cat "$1" )
else
  encoded_data="$1"
fi

#Decode infinity

while true; do
  decode_data=$( echo "$encoded_data" | base64 -d 2>/dev/null )
    if [[ $? -ne 0 ]]; then 
      echo -e "[+] Decodificacion completa:\n"
      echo "$encoded_data"
      break
    fi

  encoded_data="$decode_data"
done
