from Models.Cliente import Cliente

class ClienteAbonado(Cliente):
    def __init__(self, id, vehiculo, dni):
        Cliente.__init__(id, vehiculo)
        self.__dni = dni

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
