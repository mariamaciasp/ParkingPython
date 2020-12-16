class FacturacionAbonos():

    def __init__(self, dni, nombre, apellidos, total_facturado, fecha_inicio, fecha_final):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__total_facturado = total_facturado
        self.__fecha_inicio = fecha_inicio
        self.__fecha_final = fecha_final

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def total_facturado(self):
        return self.__total_facturado

    @total_facturado.setter
    def total_facturado(self, total_facturado):
        self.__total_facturado = total_facturado

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_final(self):
        return self.__fecha_final

    @fecha_final.setter
    def fecha_final(self, fecha_final):
        self.__fecha_final = fecha_final

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" %(self.dni, self.nombre, self.apellidos, self.total_facturado,
                                          self.fecha_inicio, self.fecha_final)
