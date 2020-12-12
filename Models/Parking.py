class Parking():
    def __init__(self, lista_coches, lista_motos, lista_minusvalidos):
        self.__lista_coches = lista_coches
        self.__lista_motos = lista_motos
        self.__lista_minusvalidos = lista_minusvalidos

    @property
    def lista_motos(self):
        return self.__lista_motos

    @lista_motos.setter
    def lista_motos(self, lista_motos):
        self.__lista_motos = lista_motos

    @property
    def lista_coches(self):
        return self.__lista_coches

    @lista_coches.setter
    def lista_coches(self, lista_coches):
        self.__lista_coches = lista_coches

    @property
    def lista_minusvalidos(self):
        return self.__lista_minusvalidos

    @lista_minusvalidos.setter
    def lista_minusvalidos(self, lista_minusvalidos):
        self.__lista_minusvalidos = lista_minusvalidos

    def __str__(self):
        for i in self.lista_coches:
            print(i)
        for i in self.lista_motos:
            print(i)
        for i in self.lista_minusvalidos:
            print(i)
        return ""
