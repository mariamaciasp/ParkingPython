class cliente_abonado_repository():

    def __init__(self, lista_clientes_abonados):
        self.__lista_clientes_abonados = lista_clientes_abonados

    @property
    def lista_clientes_abonados(self):
        return self.__lista_clientes_abonados

    @lista_clientes_abonados.setter
    def lista_clientes_abonados(self, lista_clientes_abonados):
        self.__lista_clientes_abonados = lista_clientes_abonados

    def add_cliente_abonado(self, cliente_abonado):
        self.lista_clientes_abonados.append(cliente_abonado)
