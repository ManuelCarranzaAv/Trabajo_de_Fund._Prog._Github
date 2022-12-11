# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducci�n no es correcta.

def pedido():
	opc = str()
	opc = input()
	print("El cliente realizo el pedido: "+opc)

def cuenta():
	cta = str()
	cta = input()
	print("La cuenta es de 20 soles")

if __name__ == '__main__':
	print("Realizar pedido:")
	pedido()
	print("�Desea pedir la cuenta?")
	cuenta()

