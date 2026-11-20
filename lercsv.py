import csv

with open("Clientes.csv", "r") as ficheiro:
    ficheiro_csv = csv.reader(ficheiro, delimiter=";")
    for linha in ficheiro_csv:
        print(linha)