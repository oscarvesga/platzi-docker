from HitosIV import HitosIV

def test_should_initialize_object_ok():
	hitos = HitosIV()
	assert type(hitos) is HitosIV, "No se ha podido inicializar los hitos"

def test_should_have_hitos_stored_ok():
	hitos = HitosIV()
	assert type(hitos.todos_hitos()) is dict, "hitos no contiene un diccionario"

def test_should_return_hitos_ok_and_raise_err():
	hitos = HitosIV()
	assert hitos.uno(0)["file"] == "0.Repositorio" 