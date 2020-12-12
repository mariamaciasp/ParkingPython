class Plaza():
    def __init__(self, num_plaza, vehiculo, ocupada, reservada):
        self.__num_plaza = num_plaza
        self.__vehiculo = vehiculo
        self.__ocupada = ocupada
        self.__reservada = reservada

    @property
    def num_plaza(self):
        return self.__num_plaza

    @num_plaza.setter
    def num_plaza(self, num_plaza):
        self.__num_plaza = num_plaza

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

    @property
    def reservada(self):
        return self.__reservada

    @reservada.setter
    def reservada(self, reservada):
        self.__reservada = reservada

    def __str__(self):
        return "(%s, %s, %s, %s)" %(self.num_plaza, self.vehiculo, self.ocupada, self.reservada)
