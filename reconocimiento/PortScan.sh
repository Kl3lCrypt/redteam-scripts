#!/bin/bash

# Ctrl_c
function ctrl_c(){
  echo -e "\n\n[!] Saliendo del programa ..... \n"
  tput cnorm; exit 1
}

# ctrl+c
trap ctrl_c INT

#Ocultar cursos
tput civis
for port in $(seq 1 65535); do
  (echo '' > /dev/tcp/127.0.0.1/$port) 2>/dev/null && echo "[+] $port -- ABIERTO" &
done; wait
tput cnorm
