import re
import sys

#ipv4 address tiene la forma de #.#.#.#. , cada # va del 0 al 255
def main():
    print(validate(input("IPv4 Address: ")))


#Para numeros entre 0 y 199 -> [0-1]?[0-9]{1,2}  ({1,2} significa 1 o 2 digitos del 0 al 9)
#Para numeros entre 200 y 249 -> 2[0-4][0-9]
#Para numeros entre 250 y 255 -> 25[0-5]
#Entonces tengo que escribir que el num esta entre 0 y 199 | 200 y 249 | 250 y 255 (| = or) 4 veces
def validate(ip):
    if re.search(r"^([0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.([0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.([0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.([0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$", ip):
        return True
    #chequear que el num no pase de 255 o sea menor a 0
  
    else:
        return False


if __name__ == "__main__":
    main()