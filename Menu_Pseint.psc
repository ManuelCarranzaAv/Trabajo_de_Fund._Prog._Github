Algoritmo crear_Menu
	
	Definir opc Como Caracter
	Repetir
	Escribir "    MENU    "
	Escribir "------------"
	Escribir "(1)Lomo saltado"
	Escribir "(2)Aji de gallina"
	Escribir "(3)Estofado de pollo"
	Escribir "(4)Papa a la huancaina"
	Escribir "(0) Salir"
	Escribir "Elige una opcion (0-4)..."Sin Saltar
	Leer opc
	Segun opc Hacer
		"1":
			Limpiar Pantalla
			Escribir ""
			Escribir "esta es la opcion 1"
			Escribir "　Has elegido Lomo Saltado!!"
			Esperar Tecla
		"2":
			Limpiar Pantalla
			Escribir ""
			Escribir "esta es la opcion 2"
			Escribir "　Has elegido Aji de gallina!!"
			Esperar Tecla
		"3":
			Limpiar Pantalla
			Escribir ""
			Escribir "esta es la opcion 3"
			Escribir "　Has elegido Estofado de pollo!!"
			Esperar Tecla
		"4":
			Limpiar Pantalla
			Escribir ""
			Escribir "esta es la opcion 4"
			Escribir "　Has elegido Papa a la huancaina!!"
			Esperar Tecla
		"0":
			Limpiar Pantalla
			Escribir "Muchas gracias por su visita"
		De Otro Modo:
			Limpiar Pantalla
			Escribir opc, "no se una opcion correcta, Intentalo de nuevo"
			Escribir "Pulsa una tecla para continuar"
			Esperar Tecla
			
	FinSegun
Hasta Que(opc=="0")
FinAlgoritmo
