PI=3.141516

#Area del cuadrado
def acuadrado():
	lado=input("Cual es el valor del lado?")
	lado=float(lado)
	x=lado*2
	print("El area del cuadrado es ",x," unidades cuadradas")

#Area del triangulo
def atriangulo():
	base=input("Cual es el valor de la base?")
	base=float(base)
	altura=input("Cual es el valor de la altura?")
	altura=float(altura)
	y=(base*altura)/2
	print("El area del triangulo es ",y," unidades cuadradas")

#Area del circulo
def acirculo():
	radio=input("Cual es valor del radio?")
	radio=float(radio)
	z=(PI*radio)**2
	print("El area del circulo es ",z," unidades cuadradas")


x=str("si")
while(x=="si"):
	opc=input("Elije la figura geometrica para calcular su area Cuadrado=1 Triangulo=2 Circulo=3:")
	opc=int(opc)
	if(opc==1):
		acuadrado()
	elif(opc==2):
		atriangulo()
	elif(opc==3):
		acirculo()
	else:
		print("Ingresa una opcion valida:")

	x=input("Quieres calcular el area de otra figura [si/no]:")
	x=str(x)