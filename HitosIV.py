import json

class HitosIV:
	"""Una clase para los hitos del curso arquitectura con docker """

	def __init__(self):
		try:  # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
			with open('hitos.json') as data_file:
				self.hitos = json.load(data_file)
		except IOError as e:
			print("Error %d leyendo hitos.json: %s", e.errno,e.strerror)

	def todos_hitos(self):
		return self.hitos

	def cuantos(self):
		return len(self.hitos['hitos'])

	def uno(self,hito_id):
		if hito_id > len(self.hitos['hitos']) or hito_id < 0:
			raise IndexError("Indice fuera del rango")
		return self.hitos['hitos'][hito_id]