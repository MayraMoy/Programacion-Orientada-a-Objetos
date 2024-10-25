from Personas import Persona

class Cliente(Persona):
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Cliente Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNombre, aApellido, aEdad, aDni):
        self._dni = None
        self._edad = None
        self._apellido = None
        self._nombre = None
        self._nombre = aNombre
        self._apellido = aApellido
        self._edad = aEdad
        self._dni = aDni

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

    def setDni(self, aDni):
        wasSet = False
        self._dni = aDni
        wasSet = True
        return wasSet

    def getNombre(self):
        return self._nombre

    def getApellido(self):
        return self._apellido

    def getEdad(self):
        return self._edad

    def getDni(self):
        return self._dni

    def delete(self):
        pass

    def __str__(self):
        return str(super().__str__()) + "[" + "nombre" + ":" + str(self.getNombre()) + "," + "apellido" + ":" + str(self.getApellido()) + "," + "edad" + ":" + str(self.getEdad()) + "]" 