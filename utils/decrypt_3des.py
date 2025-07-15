#!/usr/bin/env python3

# Decodificacion de cifrado 3DES KEY MODE (CBC) 

from Crypto.Util.Padding import unpad
from Crypto.Cipher import DES3
import base64

message_b64 = "L7Rv00A8TuwJAr67kITxxcSgnIk25Am/" #Mensaje a desencriptar (Modificar con vuestro menaje)
des_key = b"rcmail-!24ByteDESkey*Str" # Clave de desencriptado (Modificar con vuestra clave)

def check():

    if len(des_key) in (16, 24):
        return True
    
    return None


def run():

    message_decode = base64.b64decode(message_b64)
    
    iv = message_decode[:8]

    ciphertext = message_decode[8:]

    cipher = DES3.new(des_key, DES3.MODE_CBC, iv)

    decrypted_bytes = cipher.decrypt(ciphertext)

    decrypted_bytes = decrypted_bytes.rstrip(b'\0') # No usa padding estandar, quitamos los ceros a la derecha.

    return decrypted_bytes.decode('utf-8', errors='ignore')


if __name__ == '__main__':

    result_checker = check()
    
    if result_checker == True:
        textplain = run()
        print(textplain)
    

