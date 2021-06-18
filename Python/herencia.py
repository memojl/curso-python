
class Persona:
	def __init__(self,edad,nombre):
		self.edad=edad
		self.nombre=nombre
		print("Se ha acreado a ",self.nombre," de ",self.edad)

	def hablar(self,*palabras):
		for frase in palabras:
			print(self.nombre,": ",frase)


class Deportista(Persona):
	def practicarDeporte(self):
		print(self.nombre,': voy a praticar');


juan=Persona(30,'Juan')
juan.hablar('Hola estoy hablando','Este soy yo')
luis=Deportista(30,'Luis')
luis.hablar('Hola estoy hablando','Este soy yo')
luis.practicarDeporte()
