#!/usr/bin/env python3

import argparse
from termcolor import colored

def get_arguemnts():
    parser = argparse.ArgumentParser(description="Script para crear nombres de usuaio personalizados.")
    parser.add_argument("-n", "--name", dest="name", required=True, help=" Nombre (Ex: Jhon Deep == Jhon)")
    parser.add_argument("-l", "--last-name", dest="last_name", required=True, help=" Aplellido (Ex: Jhon Deep == Deep)")

    options = parser.parse_args()

    return options.name, options.last_name



def trat_data(name, last_name):
    trat_name = name.lower()
    trat_last_name = last_name.lower()
    return trat_name, trat_last_name


def combinations(name, last_name):

    trat_name, trat_last_name = trat_data(name, last_name)

    combinations = []

    combinations.append(trat_name)
    combinations.append(trat_last_name)
    combinations.append(trat_name + trat_last_name)
    combinations.append(trat_last_name + trat_name)
    combinations.append(trat_name[0] + trat_last_name)
    combinations.append(trat_last_name[0] + trat_name)
    combinations.append(trat_name[0] + "." + trat_last_name)
    combinations.append(trat_name[0] + "-" + trat_last_name)
    combinations.append(trat_last_name[0] + "." + trat_name)
    combinations.append(trat_last_name[0] + "-" + trat_name)


    return combinations


def presentations(combinations):
    for comb in combinations:
        print(comb)


def export_file(combinations):
    with open("users.txt", "w") as f:
        for comb in combinations:
            f.write(comb + "\n")


def main():
    print(colored("\n[+] Creando lista de posibles nombres de usuario...\n", "green"))
    name, last_name = get_arguemnts()
    combi_list = combinations(name, last_name)
    presentations(combi_list)
    export_file(combi_list)


if __name__ == "__main__":
    main()
