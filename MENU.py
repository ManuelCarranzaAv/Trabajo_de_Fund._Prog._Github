

if __name__ == '__main__':
	opc = str()
	while True:# no hay 'repetir' en python
		print("          MENU        ")
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
			print("") 
			print("")
			print("esta es la opcion 1")
			print("!!Has elegido Arroz con pollo!!")
			input() 
		elif opc=="2":
			print("") 
			print("")
			print("esta es la opcion 2")
			print("!!Has elegido Aji de gallina!!")
			input() 
		elif opc=="3":
			print("") 
			print("")
			print("esta es la opcion 3")
			print("!!Has elegido Arroz chaufa!!")
			input() 
		elif opc=="4":
			print("") 
			print("")
			print("esta es la opcion 4")
			print("!!Has elegido Seco de pollo!!")
			input() 
		elif opc=="0":
			print("") 
			print("Muchas gracias por su visita")
		else:
			print("") 
			print(opc,"no se una opcion correcta, Intentalo de nuevo")
			print("Pulsa una tecla para continuar")
			input() 
		if (opc=="0"): break

