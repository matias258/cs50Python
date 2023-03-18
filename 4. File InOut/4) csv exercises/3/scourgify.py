import sys
import os
import csv

columnas_antiguas = ["name", "house"]
columnas_nuevas = ["first", "last", "house"]

nuevos_datos = []

from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit(1)
elif len(sys.argv) > 2 :
    print("Too many arguments")
    sys.exit(1)

nombre = sys.argv[1]

if not os.path.exists(nombre):
    print("File doesn't exist")
    sys.exit(1)

if (not nombre.endswith(".csv") ):
    print("File is not a .csv")
    sys.exit(1)

with open(nombre, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #strip me soluciona que no haya sangrias antes de los nombres
        #y split me splitea name para que sean first y last names
        fullName = [part.strip() for part in row["name"].split(",")]
        nuevoDict = {
            "first" : fullName[1],
            "last" : fullName[0],
            "house" : row["house"]
        }
        nuevos_datos.append(nuevoDict)

#escribo la solucion en un nuevo .csv
with open("new.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=columnas_nuevas)
    writer.writeheader()  # esto me importa las headers "first,last,house"

    #copio en el orden de los nuevos datos
    for row in nuevos_datos:
        writer.writerow(row)



