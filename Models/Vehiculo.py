class Vehiculo():
    def __init__(self, matricula, tipo, num_plaza, pin, fecha_entrada, fecha_salida):
        self.__matricula = matricula
        self.__tipo = tipo
        self.__num_plaza = num_plaza
        self.__pin = pin
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def num_plaza(self):
        return self.__num_plaza

    @num_plaza.setter
    def num_plaza(self, num_plaza):
        self.__num_plaza = num_plaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    def __str__(self):
        return "[%s, %s, %s, %s, %s, %s]" %(self.matricula, self.tipo, self.num_plaza, self.pin, self.fecha_entrada, self.fecha_salida)
