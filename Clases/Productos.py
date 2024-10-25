class Producto():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Producto Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNombre, aPrecio):
        self._precio = None
        self._nombre = None
        self._nombre = aNombre
        self._precio = aPrecio

    #------------------------
    # INTERFACE
    #------------------------
    def setNombre(self, aNombre):
        wasSet = False
        self._nombre = aNombre
        wasSet = True
        return wasSet

    def setPrecio(self, aPrecio):
        wasSet = False
        self._precio = aPrecio
        wasSet = True
        return wasSet

    def getNombre(self):
        return self._nombre

    def getPrecio(self):
        return self._precio

    def delete(self):
        pass

    def __str__(self):
        return str(super().__str__()) + "[" + "nombre" + ":" + str(self.getNombre()) + "," + "precio" + ":" + str(self.getPrecio()) + "]"