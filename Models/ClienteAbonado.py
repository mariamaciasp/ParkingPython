from Models.Cliente import Cliente

class ClienteAbonado(Cliente):

    def __init__(self, id, vehiculo, dni, nombre, apellidos, num_tarjeta, tipo_abono, email, facturado=[]):
        Cliente.__init__(self, id, vehiculo)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__num_tarjeta = num_tarjeta
        self.__tipo_abono = tipo_abono
        self.__email = email
        self.__facturado = facturado

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
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self.__num_tarjeta = num_tarjeta

    @property
    def tipo_abono(self):
        return self.__tipo_abono

    @tipo_abono.setter
    def tipo_abono(self, tipo_abono):
        self.__tipo_abono = tipo_abono

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email  = email

    @property
    def facturado(self):
        return self.__facturado

    @facturado.setter
    def facturado(self, facturado):
        self.__facturado = facturado

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" %(self.id, self.vehiculo, self.dni, self.nombre, self.apellidos,
                                                      self.email, self.num_tarjeta, self.tipo_abono, self.facturado)
