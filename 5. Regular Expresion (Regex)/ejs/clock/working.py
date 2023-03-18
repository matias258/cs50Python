import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^([0-1]?[0-9]) (AM|PM) to ([0-1]?[0-9]) (AM|PM)", s)
    if match:

        hora1, dia1, hora2, dia2 = match.groups()

        if (dia1 == "PM"):
            hora1 = int(hora1) + 12
            if (hora1 > 23):
                hora1 = hora1 - 12
        if (dia2 == "PM"):
            hora2 = int(hora2) + 12
            if (hora2 > 23):
                hora2 = hora2 - 12

        return f"{hora1} to {hora2}"
    
    elif re.search(r"^([0-1]?[0-9])(:[0-5]?[0-9])? (AM|PM) to ([0-1]?[0-9])(:[0-5]?[0-9])? (AM|PM)", s):

        match = re.search(r"^([0-1]?[0-9])(:[0-5]?[0-9])? (AM|PM) to ([0-1]?[0-9])(:[0-5]?[0-9])? (AM|PM)", s)
        if match:
            hora1, min1, dia1, hora2, min2, dia2 = match.groups()

            if (dia1 == "PM"):
                hora1 = int(hora1) + 12
                if (hora1 > 23):
                    hora1 = hora1 - 12
            if (dia2 == "PM"):
                hora2 = int(hora2) + 12
                if (hora2 > 23):
                    hora2 = hora2 - 12

            return f"{hora1}{min1} to {hora2}{min2}"






if __name__ == "__main__":
    main()