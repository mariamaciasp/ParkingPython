class abono_repository():

    def __init__(self, lista_abonos):
        self.__lista_abonos = lista_abonos

    @property
    def lista_abonos(self):
        return self.__lista_abonos

    @lista_abonos.setter
    def lista_abonos(self, lista_abonos):
        self.__lista_abonos = lista_abonos

    def add_abono(self, abono):
        self.lista_abonos.append(abono)
