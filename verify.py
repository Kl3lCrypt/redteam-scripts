import smtplib
import dns.resolver
import re

def validar_formato(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def obtener_mx(dominio):
    try:
        respuestas = dns.resolver.resolve(dominio, 'MX')
        return str(respuestas[0].exchange)
    except Exception as e:
        print(f"[!] No se pudo obtener MX: {e}")
        return None

def verificar_smtp(email, mx_host):
    try:
        servidor = smtplib.SMTP(timeout=10)
        servidor.connect(mx_host)
        servidor.helo('example.com')
        servidor.mail('verificador@example.com')
        code, mensaje = servidor.rcpt(email)
        servidor.quit()
        return code
    except Exception as e:
        print(f"[!] Error SMTP: {e}")
        return None

# === Email a verificar ===
email = "info@grupopapilio.es"

print(f"🔎 Verificando: {email}")

if not validar_formato(email):
    print("❌ Formato inválido")
else:
    dominio = email.split('@')[1]
    mx_host = obtener_mx(dominio)

    if not mx_host:
        print("❌ El dominio no tiene MX (no puede recibir correos)")
    else:
        print(f"🌐 MX encontrado: {mx_host}")
        code = verificar_smtp(email, mx_host)

        if code == 250 or code == 251:
            print("✅ El email **existe** (respuesta SMTP válida)")
        elif code == 550:
            print("❌ El email **no existe** (550 User not found)")
        elif code is None:
            print("⚠️ No se pudo verificar (el servidor no respondió)")
        else:
            print(f"⚠️ Respuesta inesperada del servidor: {code}")

