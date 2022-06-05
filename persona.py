class Persona: 
    def __init__(self,apellido,nombre,persona_id=None):
        self._Persona__apellido=apellido
        self._Persona__nombre=nombre 
        self._Persona__persona_id=persona_id

#aca redefino el atributo _Persona__persona_id por el nuevo persona_id
#esto es importante para que a partir de la linea 72 del test lo reconozca
    @property
    def persona_id(self):
        return self._Persona__persona_id

    @persona_id.setter
    def persona_id(self, p):
        self._Persona__persona_id = p

