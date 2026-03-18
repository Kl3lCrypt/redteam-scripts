#!/usr/bin/env python3

def decimal_a_ip(decimal):
    decimal = int(decimal)
    return ".".join(str((decimal >> (8 * i)) & 255) for i in reversed(range(4)))


def ip_a_decimal(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        raise ValueError("IP inválida")

    decimal = 0
    for parte in partes:
        decimal = (decimal << 8) + int(parte)
    return decimal


def main():
    print("Conversor IPv4 ↔ Decimal")
    print("1) Decimal a IP")
    print("2) IP a Decimal")

    opcion = input("Elige opción (1/2): ").strip()

    if opcion == "1":
        d = input("Introduce número decimal: ")
        print("IP:", decimal_a_ip(d))

    elif opcion == "2":
        ip = input("Introduce dirección IP: ")
        print("Decimal:", ip_a_decimal(ip))

    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()

