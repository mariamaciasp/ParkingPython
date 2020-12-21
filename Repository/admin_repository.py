import pickle

class admin_repository():

    def __init__(self, lista_admin=[]):
        self.__lista_admin = lista_admin

    @property
    def lista_admin(self):
        return self.__lista_admin

    @lista_admin.setter
    def lista_admin(self, lista_admin):
        self.__lista_admin = lista_admin

    def __str__(self):
        for i in self.lista_admin:
            print(i)
        return ""

    def add_admin(self, admin):
        self.lista_admin.append(admin)
        pickle_admin = open("./DataBase/admin", "wb")
        pickle.dump(self.lista_admin, pickle_admin)
        pickle_admin.close()

    def buscar_admin(self, usuario, password):
        for i in self.lista_admin:
            if(i.usuario == usuario and i.password == password):
                return i
        return None
