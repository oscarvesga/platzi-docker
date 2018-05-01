import json

class HitosIV(object):
	"""Una clase para los hitos del curso arquitectura con docker """
	
	hitos=[]

	def __init__(self, arg):
		try:
			with open('hitos.json') as data_file:
				self.hitos = json.load(data_file)
		except IOError as e:
			print "Error {0} leyendo hitos.json: {1}", format(e.errno,e.strerror)