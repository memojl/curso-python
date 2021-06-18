#Ejemplo condicionales
opc=input("Quieres ingresar a las preguntas [si/no]:")
opc=str(opc)
while (opc=="si"):
	pregunta=input("¿Trabajas desde casa?")
	pregunta=str(pregunta)
	if(pregunta=="si"):
		print("Eres afortunado")
	if(pregunta=="no"):
		print("Trabajas fuera de casa")

	tiempo=input("Cuantos minutos haces al trabajo?")
	tiempo=int(tiempo)
	if(tiempo==0):
		print("Trabajas desde casa")
	elif(tiempo<=20):
		print("Es poco tiempo")
	elif(tiempo>=21 and tiempo<=45):
		print("Es un tiempo razonable")
	else:
		print("Debes buscar otras rutas")

	opc=input("Quiere volver a la pregunta:")
	opc=str(opc)