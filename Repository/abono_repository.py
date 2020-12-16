class abono_repository():

    def __init__(self, lista_abonos):
        self.__lista_abonos = lista_abonos

    @property
    def lista_abonos(self):
        return self.__lista_abonos

    @lista_abonos.setter
    def lista_abonos(self, lista_abonos):
        self.__lista_abonos = lista_abonos

    def __str__(self):
        for i in self.lista_abonos:
            print(i)
        return ""

    def add_abono(self, abono):
        self.lista_abonos.append(abono)

    def buscar_abono(self, dni):
        for i in self.lista_abonos:
            if(i.cliente.dni == dni):
                return i
        return None

    def borrar_abono(self, dni):
        abono = self.buscar_abono(dni)
        if( abono != None):
            self.lista_abonos.remove(abono)
            return True
        return False


