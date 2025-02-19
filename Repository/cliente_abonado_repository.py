import pickle

class cliente_abonado_repository():

    def __init__(self, lista_clientes_abonados=[]):
        self.__lista_clientes_abonados = lista_clientes_abonados

    @property
    def lista_clientes_abonados(self):
        return self.__lista_clientes_abonados

    @lista_clientes_abonados.setter
    def lista_clientes_abonados(self, lista_clientes_abonados):
        self.__lista_clientes_abonados = lista_clientes_abonados

    def __str__(self):
        for i in self.lista_clientes_abonados:
            print(i)
        return ""

    def add_cliente_abonado(self, cliente_abonado):
        self.lista_clientes_abonados.append(cliente_abonado)
        pickle_cliente_abonado = open("./DataBase/cliente_abonado", "wb")
        pickle.dump(self.lista_clientes_abonados, pickle_cliente_abonado)
        pickle_cliente_abonado.close()

    def buscar_vehiculo_matricula_dni(self, matricula, dni):
        for i in self.lista_clientes_abonados:
            if(i.dni == dni and i.vehiculo.matricula == matricula):
                return i.vehiculo
        print("Datos introducidos incorrectos\n")
        return None

    def buscar_vehiculo_matricula(self, matricula):
        for i in self.lista_clientes_abonados:
            if(i.vehiculo.matricula == matricula):
                return i.vehiculo
        return None

    def buscar_cliente_dni(self, dni):
        for i in self.lista_clientes_abonados:
            if(i.dni == dni):
                return i
        return None

    def borrar_cliente_dni(self, dni):
        cliente = self.buscar_cliente_dni(dni)
        if(cliente!=None):
            self.lista_clientes_abonados.remove(cliente)
            pickle_cliente_abonado = open("./DataBase/cliente_abonado", "wb")
            pickle.dump(self.lista_clientes_abonados, pickle_cliente_abonado)
            pickle_cliente_abonado.close()
            return True
        return False
