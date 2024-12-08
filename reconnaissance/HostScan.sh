#!/bin/bash

# Ctrl_c
function ctrl_c(){
  echo -e "\n\n[!] Saliendo del programa ..... \n"
  exit 1
}

# ctrl+c
trap ctrl_c INT

# Obtener los host
echo "$(for i in $(seq 1 254); do
  timeout 1 bash -c "ping -c 1 192.168.1.$i &>/dev/null" && echo "[+] El Host 192.168.1.$i esta ABIERTO" &
done; wait)" | sort -u 





