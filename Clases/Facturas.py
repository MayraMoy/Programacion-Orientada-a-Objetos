import os
class Factura():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Factura Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aCliente, aProveedor, aProductos, aTotal):
        self._total = None
        self._productos = None
        self._proveedor = None
        self._cliente = None
        self._cliente = aCliente
        self._proveedor = aProveedor
        self._productos = aProductos
        self._total = aTotal

    #------------------------
    # INTERFACE
    #------------------------
    def setCliente(self, aCliente):
        wasSet = False
        self._cliente = aCliente
        wasSet = True
        return wasSet

    def setProveedor(self, aProveedor):
        wasSet = False
        self._proveedor = aProveedor
        wasSet = True
        return wasSet

    def setProductos(self, aProductos):
        wasSet = False
        self._productos = aProductos
        wasSet = True
        return wasSet

    def setTotal(self, aTotal):
        wasSet = False
        self._total = aTotal
        wasSet = True
        return wasSet

    def getCliente(self):
        return self._cliente

    def getProveedor(self):
        return self._proveedor

    def getProductos(self):
        return self._productos

    def getTotal(self):
        return self._total

    def delete(self):
        pass

    def __str__(self):
        return str(super().__str__()) + "[" + "total" + ":" + str(self.getTotal()) + "]" + str(os.linesep) + "  " + "cliente" + "=" + str((((self.getCliente().__str__().replaceAll("  ", "    ")) if not self.getCliente() == self else "this") if not (self.getCliente() is None) else "null")) + str(os.linesep) + "  " + "proveedor" + "=" + str((((self.getProveedor().__str__().replaceAll("  ", "    ")) if not self.getProveedor() == self else "this") if not (self.getProveedor() is None) else "null")) + str(os.linesep) + "  " + "productos" + "=" + (((self.getProductos().__str__().replaceAll("  ", "    ")) if not self.getProductos() == self else "this") if not (self.getProductos() is None) else "null")