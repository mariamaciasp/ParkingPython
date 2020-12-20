import pickle

class vehiculo_repository():

    def __init__(self, lista_vehiculos=[]):
        self.__lista_vehiculos = lista_vehiculos

    @property
    def lista_vehiculos(self):
        return self.__lista_vehiculos

    @lista_vehiculos.setter
    def lista_vehiculos(self, lista_vehiculos):
        self.__lista_vehiculos = lista_vehiculos

    def __str__(self):
        for i in self.lista_vehiculos:
            print(i)
        return ""

    def add_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)
        pickle_vehiculo = open("./DataBase/vehiculo", "wb")
        pickle.dump(self.lista_vehiculos, pickle_vehiculo)
        pickle_vehiculo.close()

    def buscar_vehiculo_matricula(self, matricula):
        for i in self.lista_vehiculos:
            if (i.matricula == matricula):
                return i
        print("Matrícula incorrecta")
        return None

    def borrar_vehiculo(self, matricula):
        vehiculo = self.buscar_vehiculo_matricula(matricula)
        if( vehiculo != None):
            self.lista_vehiculos.remove(vehiculo)
            pickle_vehiculo = open("./DataBase/vehiculo", "wb")
            pickle.dump(self.lista_vehiculos, pickle_vehiculo)
            pickle_vehiculo.close()
            return True
        return False
