class Admin():
    def __init__(self, usuario, password):
        self.__usuario = usuario
        self.__password = password

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        return "Usuario: %s, contraseña: %s" %(self.usuario, self.password)
