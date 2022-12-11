
def pedido():
	opc = str()
	opc = input()
	print("El cliente realizo el pedido: "+opc)

def cuenta():
	cta = str()
	cta = input()
	print("La cuenta es de 20 soles")

if __name__ == '__main__':
	print("Buenas tardes, ¿Que desea pedir? ")
	pedido()
	print("¿Desea pedir la cuenta?")
	cuenta()

