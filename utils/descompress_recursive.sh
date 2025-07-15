#!/bin/bash

function ctrl_c(){
  echo -e "\n\n[!] Estas saliendo...\n"
  exit 1
}

# Ctrl+c

trap ctrl_c INT

first_file_name="other_name.gz" # En esta linea debes poner el archivo a descomprimir. Ej: "test.gz"

echo -e "\n\n [+] El archivo vale: $first_file_name\n"

descompressed_file_name="$(7z l $first_file_name | tail -n 3 | head -n 1 | awk 'NF{print $NF}')"

7z x $first_file_name &>/dev/null

while [ $descompressed_file_name ]; do
  echo -e "[+] El archivo descomprimido es $descompressed_file_name"
  7z x $descompressed_file_name &>/dev/null
  descompressed_file_name="$(7z l $descompressed_file_name | tail -n 3 | head -n 1 | awk 'NF{print $NF}')"
done 
