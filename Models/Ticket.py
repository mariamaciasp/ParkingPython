class Ticket():
    def __init__(self, matricula, fecha_entrada, num_plaza, pin):
        self.__matricula = matricula
        self.__fecha_entrada = fecha_entrada
        self.__num_plaza = num_plaza
        self.__pin = pin

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

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

    def __str__(self):
        print("-----------Ticket Parking Triana-----------")
        print(f"Matrícula: {self.matricula}\nNúmero de plaza: {self.num_plaza}")
        print(f"Fecha de entrada: {self.fecha_entrada.day}/{self.fecha_entrada.month}/{self.fecha_entrada.year} "
              f"{self.fecha_entrada.hour}:{self.fecha_entrada.minute}")
        print(f"Código pin: {self.pin}")
        print("-----------Gracias por su confianza--------")
        return ""
