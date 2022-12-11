# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	opc = str()
	while True:# no hay 'repetir' en python
		print(" MENU ")
		print("----------------------")
		print("(1) Arroz con pollo")
		print("(2) Aji de gallina")
		print("(3) Arroz chaufa")
		print("(4) Seco de pollo")
		print("(0) salir")
		print("-----------------------")
		print("Elige una opcion(0-4).......", end="")
		opc = input()
		if opc=="1":
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("")
			print("esta es la opcion 1")
			print("!!Has elegido Arroz con pollo!!")
			input() # a diferencia del pseudocodigo, espera un Enter, no cualquier tecla
		elif opc=="2":
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("")
			print("esta es la opcion 2")
			print("!!Has elegido Aji de gallina!!")
			input() # a diferencia del pseudocodigo, espera un Enter, no cualquier tecla
		elif opc=="3":
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("")
			print("esta es la opcion 3")
			print("!!Has elegido Arroz chaufa!!")
			input() # a diferencia del pseudocodigo, espera un Enter, no cualquier tecla
		elif opc=="4":
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("")
			print("esta es la opcion 4")
			print("!!Has elegido Seco de pollo!!")
			input() # a diferencia del pseudocodigo, espera un Enter, no cualquier tecla
		elif opc=="0":
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print("Muchas gracias por su visita")
		else:
			print("") # no hay forma directa de borrar la pantalla con Python estandar
			print(opc,"no se una opcion correcta, Intentalo de nuevo")
			print("Pulsa una tecla para continuar")
			input() # a diferencia del pseudocodigo, espera un Enter, no cualquier tecla
		if (opc=="0"): break

