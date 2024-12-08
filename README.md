# BashPentools
Colección de scripts Bash para automatizar tareas en todas las etapas de un test de intrusión: reconocimiento, explotación y post-explotación. Diseñado para pentesters y estudiantes, estos scripts son ligeros, prácticos y creados durante retos en plataformas de ciberseguridad.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **Reconocimiento**: Herramientas para descubrir servicios, escanear puertos, enumerar subdominios, etc.
- **Explotación**: Scripts para realizar ataques y explotación de vulnerabilidades.
- **Post-explotación**: Herramientas para la recolección de datos y mantenimiento del acceso.
- **Auxiliar**: Herramientas generales que ayudan en varias etapas del pentesting.

## Instalación

Para comenzar, clona este repositorio a tu máquina local:

```bash
git clone https://github.com/Kl3lCrypt/BashPenTools
cd BashPenTools
```
## Requisitos

Todos los script de este proyecto estaran porgramados en bash, lo que hace indispensáble su disponibilidad.

## Usos

Aquí mostramos algunos usos de estos script:

DecodeBrainFuck
```bash
[+] Uso: ./auxiliar/DecodeBrainFuck.sh <archivo.bf>
```
DecodeRecursiveBase64
```bash
[+] Uso: ./auxiliar/DecodeRecursiveBase64.sh <file_encode>
```
PortScan
```bash
[+] Uso: ./reconocimiento/PortScan.sh
```
## Advertencia Legal

**Este proyecto está destinado únicamente a fines educativos y de investigación en entornos autorizados.** No se debe usar ninguna de las herramientas o scripts contenidos en este repositorio en sistemas, redes o dispositivos para los que no se tenga explícito consentimiento.

El uso no autorizado de estas herramientas en sistemas ajenos es **ilegal** y está prohibido. El autor de este repositorio no se hace responsable de ningún daño, pérdida de datos, o cualquier consecuencia derivada del uso indebido de estas herramientas.
