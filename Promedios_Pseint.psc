
SubProceso prom <- Promedio ( arreglo, cantidad )
    Definir suma Como Entero
	Definir i Como Entero
	suma <- 0
    Para i<-1 Hasta cantidad Hacer
        suma <- suma + arreglo(i)
    FinPara
	Definir prom Como Real
    prom <- suma/cantidad
FinSubProceso

Proceso Principal
	Definir n Como Entero
    Dimension datos[100]
    Escribir "Ingrese la cantidad de datos:"
    Leer n
    
	Definir i Como Entero
	Definir datos Como Entero
    Para i<-1 Hasta n Hacer
        Escribir "Ingrese el dato ",i,":"
        Leer datos(i)
    FinPara
    
    Escribir "El promedio es: ",Promedio(datos,n)
    
FinProceso