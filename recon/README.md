# 🛰️ Recon

Esta carpeta contiene scripts orientados a tareas de reconocimiento y enumeración pasiva o activa de servicios.

## 📄 Script incluido

- **`smtp_email_verification.py`**  
  Realiza verificación de direcciones de correo electrónico utilizando consultas DNS para obtener registros MX y conexión directa al servidor SMTP para validar destinatarios. Útil para reconocimiento en fases iniciales de engagement.

## 📦 Dependencias

Este script requiere los siguientes módulos de Python:

- [`dnspython`](https://pypi.org/project/dnspython/) – Resolución DNS  
  ```bash
  pip install dnspython

