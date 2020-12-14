class vehiculo_repository():

    def __init__(self, lista_vehiculos):
        self.__lista_vehiculos = lista_vehiculos

    @property
    def lista_vehiculos(self):
        return self.__lista_vehiculos

    @lista_vehiculos.setter
    def lista_vehiculos(self, lista_vehiculos):
        self.__lista_vehiculos = lista_vehiculos

    def add_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)

    def buscar_vehiculo_matricula(self, matricula):
        for i in self.lista_vehiculos:
            if (i.matricula == matricula):
                return i
        return None
