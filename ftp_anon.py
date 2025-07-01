#!/usr/bin/env python3

from ftplib import FTP

def anon(host):
    try:
        ftp = FTP(host, timeout=10)
        ftp.login(user="anonymous", passwd="caraculo")
        print("[+] Acceso como ususario anonymous permitido!")
        ftp.quit()
        return True
    except Exception as e:
        print(f"[!] Error: {e}")
        return False

if __name__ == "__main__":
    host = "10.129.1.14"
    anon(host)
