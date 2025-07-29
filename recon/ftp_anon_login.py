#!/usr/bin/env python3

from ftplib import FTP
import argparse
from termcolor import colored

def get_argument():
    
    parser = argparse.ArgumentParser(description="Script para comprobar FTP anonymous")
    parser.add_argument("-t", "--target", required=True, dest="target", help="-t: Seleciona un target")

    args = parser.parse_args()
    return args.target



def anon(host):
    try:
        ftp = FTP(host, timeout=10)
        ftp.login(user="anonymous", passwd="hacked")
        print(colored("\n[+] Acceso como ususario anonymous permitido!\n","green"))
        ftp.quit()
        return True
    except Exception as e:
        print(f"[!] Error: {e}")
        return False


if __name__ == "__main__":
    target = get_argument()
    anon(target)
