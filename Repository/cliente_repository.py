class cliente_repository():

    def __init__(self, lista_clientes):
        self.__lista_clientes = lista_clientes

    @property
    def lista_clientes(self):
        return self.__lista_clientes

    @lista_clientes.setter
    def lista_clientes(self, lista_clientes):
        self.__lista_clientes = lista_clientes

    def add_cliente(self, cliente):
        self.lista_clientes.append(cliente)
