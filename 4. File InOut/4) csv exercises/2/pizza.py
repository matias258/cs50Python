import sys
import os
import csv

from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit(1)
elif len(sys.argv) > 2 :
    print("Too many arguments")
    sys.exit(1)

name = sys.argv[1]

if not os.path.exists(name):
    print("File doesn't exist")
    sys.exit(1)

if (not name.endswith(".csv") ):
    print("File is not a .csv")
    sys.exit(1)


pizzas =[]

with open(name, newline="") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		pizzas.append(row)



tabla = tabulate(pizzas, headers="keys", tablefmt="pipe")
print(tabla)