
class Persona:
	def __init__(self):
		self.edad=18
		self.nombre="Juan"
		print("Se ha acreado a ",self.nombre," de ",self.edad)

	def hablar(self,palabras="No se que decir"):
		print(self.nombre,": ",palabras)

escribe=Persona()
escribe.hablar()
escribe.hablar("Hola estoy hablando")