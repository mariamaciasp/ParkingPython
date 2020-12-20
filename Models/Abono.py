class Abono():
    def __init__(self, cliente, fecha_activacion, fecha_cancelacion):
        self.__cliente = cliente
        self.__fecha_activacion = fecha_activacion
        self.__fecha_cancelacion = fecha_cancelacion
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def fecha_activacion(self):
        return self.__fecha_activacion

    @fecha_activacion.setter
    def fecha_activacion(self, fecha_activacion):
        self.__fecha_activacion = fecha_activacion

    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion

    @fecha_cancelacion.setter
    def fecha_cancelacion(self, fecha_cancelacion):
        self.__fecha_cancelacion = fecha_cancelacion

    def __str__(self):
        return "[%s], %s, %s" %(self.cliente, self.fecha_activacion, self.fecha_cancelacion)
