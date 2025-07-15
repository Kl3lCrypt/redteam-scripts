# 🔧 utils

Esta carpeta contiene utilidades auxiliares que pueden ser útiles durante procesos de explotación, análisis o post-explotación. Son herramientas complementarias orientadas al Red Team y automatización de tareas comunes.

## 📜 Scripts incluidos

- `decode_brainfuck.sh` – Decodifica programas escritos en Brainfuck.
- `decode_recursive_base64.sh` – Decodificación de cadenas Base64 de manera recursiva.
- `descompress_recursive.sh` – Descomprime archivos anidados (gzip, tar, zip, etc.).
- `decrypt_3des.py` – Descifra texto cifrado con 3DES en modo CBC, dada la clave y el IV.

## 📦 Dependencias

- [`pycryptodome`](https://pypi.org/project/pycryptodome/) – Necesaria para operaciones criptográficas en el script `decrypt_3des.py`

> ✅ Todos los scripts están diseñados para ejecutarse en sistemas Linux.

