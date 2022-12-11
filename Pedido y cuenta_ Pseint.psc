
	SubProceso Pedido
		Definir opc Como Caracter
		Leer opc
		Mostrar "El cliente realizo el pedido: "+opc
		
	FinSubProceso

	SubProceso CUENTA
		Definir cta Como Caracter
		Leer cta
		Mostrar "La cuenta es de 20 soles"
		
FinSubProceso
Proceso PedidodeMenu
	
	
    Escribir "Realizar pedido:"
    Pedido 
	
	Escribir "¿Desea pedir la cuenta?"
	cuenta
FinProceso