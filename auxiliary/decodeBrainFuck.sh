#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"


function ctrl_c(){
  echo -e "${redColour}[!] Saliendo...\n${endColour}"
  exit 1
}

#ctrl_c
trap ctrl_c SIGINT

#Cinta de memoria: 30000 celdas inicializadas en 0

myarray=()

for i in {0..30000}; do
  myarray+=(0)
done

#puntero a la posicion incial de la celda

ptr=0
stack=()

#Leer el codigo Brainfuck como un archivo proporcionado como argumento

if [[ -z $1 ]];then
  echo -e "${yellowColour}[+]${endColour}${grayColour} Uso:${endColour}${blueColour} $0 <archivo.bf>${endColour}"
  exit 2
fi

# Erro por directorio o archivo vacio

if [[ ! -f $1 || ! -s $1 ]]; then
  echo -e "${redColour}[!] Error $1 no es un archivo o su contenido esta vacio${endColour}"
  exit 3
fi

# Codigo y logitud
code=$(cat $1)
len=${#code}

#Mostrando codifo barainfuck a desencodear
echo -ne "\n${yellowColour}[+]${endColour}${grayColour} Mostrando el contenido del archivo a decodear ====>${endColour}${blueColour} $code${endColour}"
echo -e "\n\n${yellowColour}[+]${endColour}${grayColour} El codigo decodeado es:${endColour}"

#Logiga de sistema

i=0
while [[ $i -lt $len ]]; do
  case ${code:$i:1} in

    '>') #Mover el puntero a la derecha
      ((ptr++))
      if [[ $ptr -ge ${#myarray[@]} ]]; then
        echo -e "${redColour}[!] Error: Puntero fuera de los limites${endColour}"
        exit 4
      fi
      ;;

    '<')# Mover el puntero a la izquierda
      ((ptr--))
      if [[ $ptr -lt 0 ]]; then
        echo -e "${redColour}[!] Error puntero fuera de los limites${endColour}"
        exit 5
      fi
      ;;

    '+') # Incrementar el valor de la celda actual
      ((myarray[ptr]++))
      ;;

    '-') # Decrementar el valor de la celda actual
      ((myarray[ptr]--))
      ;;

    '.') #Imprime en ASCII el caracter
      printf "${purpleColour}\x$(printf %x ${myarray[ptr]})${endColour}"
      ;;

    ',') # Leer un caracter del ususario
      read -n 1 -s input
      myarray[ptr]=$(printf "%d" "$input")
      ;;

    '[')
      if [[ ${myarray[ptr]} -eq 0 ]];then
        nesting=1

        while [[ $nesting -gt 0 ]]; do
          ((i++))
          if [[ ${code:$i:1} == '[' ]]; then
            ((nesting++))
          elif [[ ${code:$i:1} == ']' ]]; then
            ((nesting--))
          fi
        done
      else
        stack+=($i)
      fi
      ;;

    ']')
      if [[ ${myarray[ptr]} -ne 0 ]];then
        i=${stack[-1]}
      else
        unset stack[-1]
      fi
      ;;
  esac

  ((i++))
done

echo -e "\n\n${yellowColour}[+]${endColour}${grayColour} Ejecución completada${endColour}"

