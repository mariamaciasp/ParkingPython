import pickle

class facturacion_abonos_repository():

    def __init__(self, lista_facturacion=[]):
        self.__lista_facturacion = lista_facturacion

    @property
    def lista_facturacion(self):
        return self.__lista_facturacion

    @lista_facturacion.setter
    def lista_facturacion(self, lista_facturacion):
        self.__lista_facturacion = lista_facturacion

    def __str__(self):
        for i in self.lista_facturacion:
            print(i)
        return ""

    def add_facturacion(self, facturacion):
        self.lista_facturacion.append(facturacion)
        pickle_facturacion = open("./DataBase/facturacion", "wb")
        pickle.dump(self.lista_facturacion, pickle_facturacion)
        pickle_facturacion.close()
