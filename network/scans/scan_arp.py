#!/usr/bin/env python3

import argparse
from scapy.all import ARP, Ether, srp
from termcolor import colored


def get_arguments():

    parser = argparse.ArgumentParser(description="Escaner ARP para detectar host activos en la red local.")
    parser.add_argument("-t", "--target", required=True, dest="target", help="IP objetivo o rango (Ex: 192.168.1.0/24)")
    args = parser.parse_args()
    return args.target


def scan_arp(ip_range):

    arp_request = ARP(pdst=ip_range)
    brodcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = brodcast/arp_request
    answered, _ = srp(packet, timeout=2, verbose=False)
    
    hosts = []

    for sent, received in answered:
        hosts.append(
            {
                "ip": received.psrc,
                "mac": received.hwsrc
            }
        )

    return hosts
    
    
def show_hosts(hosts):
    
    print(colored("\n[+] Host detectados\n", "green"))
    print(f"{'IP': <18}{'MAC': <22}")
    print("-" * 40)

    for host in hosts:
        print(f"{host['ip']:<18}{host['mac']:<22}")


def main():

    target = get_arguments()
    print(colored(f"\n[+] Iniciando escaner en {target}\n", "green"))
    hosts = scan_arp(target)
    show_hosts(hosts)


if __name__ == '__main__':
    main()

