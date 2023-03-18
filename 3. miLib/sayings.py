
#declaramos un main para testear si funciona mi nueva libreria
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#main()#
#me devuelve:
# hello, world
# goodbye, world
# hello, matias

#por eso no podemos ejecutar main al final del codigo, para esto tenemos:

if __name__ == "__main_":
	main()

#esta variable __name__ es un simbolo especial en python cuyo valor se setea automaticamente por python para ser "main" cuando corremos una file desde el cmd.
