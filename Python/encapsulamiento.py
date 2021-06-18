
class Persona:
	def __init__(self,edad,nombre):
		self.edad=edad
		self.nombre=nombre
		print("Se ha creado a ",self.nombre," de ",self.edad)

	def hablar(self,*palabras):
		for frase in palabras:
			print(self.nombre,": ",frase)


class Deportista(Persona):

	def __init__(self,edad,nombre,deporte):
		self.edad=edad
		self.nombre=nombre
		self.__deporte=deporte
		print("Se ha creado a ",self.nombre," de ",self.edad )

	def practicarDeporte(self):
		print(self.nombre,': voy a praticar')

    def verMiDeporte(self):
        return self.__deporte


juan=Persona(30,'Juan')
juan.hablar('Hola estoy hablando','Este soy yo')
luis=Deportista(30,'Luis','natacion')
luis.hablar('Hola estoy hablando','Este soy yo')
luis.practicarDeporte()
print ("Luis : practica",luis.verMiDeporte())
