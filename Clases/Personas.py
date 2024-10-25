class Persona():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Persona Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNombre, aApellido, aDni, aEdad):
        self._edad = None
        self._apellido = None
        self._nombre = None
        self._nombre = aNombre
        self._apellido = aApellido
        self._edad = aEdad

    #------------------------
    # INTERFACE
    #------------------------
    def setNombre(self, aNombre):
        wasSet = False
        self._nombre = aNombre
        wasSet = True
        return wasSet

    def setApellido(self, aApellido):
        wasSet = False
        self._apellido = aApellido
        wasSet = True
        return wasSet

    def setEdad(self, aEdad):
        wasSet = False
        self._edad = aEdad
        wasSet = True
        return wasSet

    def getNombre(self):
        return self._nombre

    def getApellido(self):
        return self._apellido

    def getEdad(self):
        return self._edad

    def delete(self):
        pass

    def __str__(self):
        return str(super().__str__()) + "[" + "nombre" + ":" + str(self.getNombre()) + "," + "apellido" + ":" + str(self.getApellido()) + "," + "edad" + ":" + str(self.getEdad()) + "]"