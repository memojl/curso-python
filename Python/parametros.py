
class Persona:
	def __init__(self,edad,nombre):
		self.edad=edad
		self.nombre=nombre
		print("Se ha acreado a ",self.nombre," de ",self.edad)

	def hablar(self,*palabras):
		for frase in palabras:
			print(self.nombre,": ",frase)

juan=Persona(18,"Juan")
juan.hablar("Hola estoy hablando","Este soy yo")

luis=Persona(20,"Luis")
luis.hablar("Hola estoy hablando","Este soy yo")
