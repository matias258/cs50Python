import sys
import os

#name toma valor del archivo que ingresamos
name = sys.argv[1]

# el archino no existe
if not os.path.exists(name):
    print("File doesn't exist")
    sys.exit(1)

# Les pasamos muchos o ningun codigos extra
if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit(1)
elif len(sys.argv) > 2 :
    print("Too many arguments")
    sys.exit(1)
    

#Si no es un archivo python
if (not name.endswith(".py") ):
    print("File is not a .py")
    sys.exit(1)


counter = 0
with open(f"{name}", "r") as file:
    #en cada linea nos fijamos si esta escrita o no
    for line in file:
        if line[0] != "#" and line != "":
            counter += 1
            
if counter > 1:
    print(f"El archivo tiene {counter} lineas de codigo.")
else:
    print(f"El archivo tiene {counter} linea de codigo.")
