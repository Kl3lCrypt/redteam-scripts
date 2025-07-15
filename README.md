# 🛠️ redteam-scripts

Este repositorio contiene una colección de scripts orientados a tareas de Red Team, pentesting y automatización de técnicas ofensivas. Incluye herramientas para reconocimiento de red, explotación de vulnerabilidades, validación de correos vía SMTP y utilidades varias.

¡Bienvenido! Aquí encontrarás scripts para facilitar tus pruebas de seguridad y aprendizaje en Red Team.

> ⚠️ Estos scripts están creados con fines educativos y deben usarse únicamente en entornos controlados o con autorización explícita.

Este proyecto es open source y se distribuye bajo la licencia [MIT](./LICENSE).

---


## 📁 Estructura del repositorio

```bash
.
├── exploitation/        # Scripts para Explotación de Vulnerabilidades
├── network/             # Escaneos de Red (Hosts y Puertos)
├── post-explotacion/    # Scripts orientados a Post-Explotación
├── recon/               # Reconocimiento y Enumeración de Servicios
├── utils/               # Scripts Auxiliares (Decodificadores, Herramientas Varias)
├── tests/               # Pruebas y Scripts de Desarrollo
└── README.md            # Este archivos
```


## 🚀 Ejecución rápida

### 🐚 Bash

```bash
 $ bash network/scans/scan_hosts.sh
 $ bash exploitation/jwt_alg_none_exploit.sh
```

### 🐍 Python

```bash
 $ python3 network/scans/scan_arp.py
```

✅ Asegúrate de tener los permisos de ejecución necesarios:

```bash
 $ chmod +x script.sh
```

> Revisa cada script individualmente para entender su comportamiento antes de ejecutarlo.


## ✨ Funcionalidades destacadas

- 🖥️ **Escaneo de red**  
  Scripts Bash y Python para descubrir hosts activos y puertos abiertos sin depender de herramientas externas.  
  Más detalles y scripts en [`network/scans/README.md`](./network/scans/README.md)

- 🐍 **Explotación de servicios**  
  - Inyección SQL basada en tiempo (`exploitation/sql_time_based.py`)  
  - Acceso anónimo por FTP (`exploitation/ftp_anon_login.py`)  
  - Fuerza bruta de acceso Telnet sin contraseña (`exploitation/telnet_unauth_bruteforce.py`)  
  - Explotación de JWT con `alg: none` (`exploitation/jwt_alg_none_exploit.sh`)

- 📬 **Verificación de correos vía SMTP**  
  Script para validar formato, obtener registros MX y probar entrega vía SMTP (`recon/smtp_email_verification.py`).

- 🛠️ **Utilidades auxiliares**  
  - Decodificador de Brainfuck (`utils/decode_brainfuck.sh`)  
  - Decodificación recursiva de Base64 (`utils/decode_recursive_base64.sh`)  
  - Descompresión automática de archivos anidados (`utils/descompress_recursive.sh`)
  - Descifrado 3DES en modo CBC (`utils/decrypt_3des.py`)


## 📦 Dependencias

Este repositorio utiliza herramientas y módulos externos para ciertas funcionalidades. Asegúrate de tener instalados los siguientes requisitos generales:

- `bash` (≥ 4.x)
- `python3` (≥ 3.6)

> 💡 Algunos scripts tienen dependencias adicionales específicas. Revisa el `README.md` de cada carpeta o el encabezado de cada script para más detalles.

- [`exploitation`](./exploitation/README.md)
- [`network/scans`](./network/scans/README.md)
- [`recon`](./recon/README.md)
- [`post-exploitation`](./post-exploitation/README.md)
- [`utils`](./utils/README.md)


## [!] Aviso Legal

Este proyecto tiene fines educativos y está orientado a la práctica en entornos controlados y autorizados (como Hack The Box, TryHackMe, laboratorios propios, etc).

El uso indebido de estas herramientas fuera de un marco legal puede ser ilegal.

No me hago responsable del mal uso. Úsalo siempre con responsabilidad y ética profesional.


## 🧠 Autor

Desarrollado por **Kl3lCrypt**
Apasionado de la ciberseguridad ofensiva · Red Team · Python · Linux


## ⭐ ¿Te ha resultado útil?

Si este repositorio te ha servido para aprender o practicar, considera darle una ⭐ para apoyarlo, o clónalo y sigue experimentando por tu cuenta.

¡Gracias por pasarte por aquí! 🚀
