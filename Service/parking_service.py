from Models.Plaza import Plaza
from Models.Vehiculo import Vehiculo
from datetime import datetime
from Repository.vehiculo_repository import vehiculo_repository
from Models.Cliente import Cliente
from Service.vehiculo_service import vehiculo_service


class parking_service():
    def __init__(self, parking, lista_precios):
        self.__parking = parking
        self.__lista_precios = lista_precios

    @property
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, parking):
        self.__parking = parking

    @property
    def lista_precios(self):
        return self.__lista_precios

    @lista_precios.setter
    def lista_precios(self, lista_precios):
        self.__lista_precios = lista_precios

    #def __str__(self):
    #    return "%s" %(self.lista_precios)

    # total 20 plazas, 14 coches, 3 minusválidos y 3 motos

    def asignar_plazas(self):
        num_plaza = 1
        cantidad_coches = 14
        cantidad_motos = 3
        cantidad_minusvalidos = 3

        self.parking.lista_coches = []
        self.parking.lista_motos = []
        self.parking.lista_minusvalidos = []

        for i in range(cantidad_coches):
            nueva_plaza_coche = Plaza(num_plaza, None, False, False)
            self.parking.lista_coches.append(nueva_plaza_coche)
            num_plaza += 1

        for i in range(cantidad_motos):
            nueva_plaza_moto = Plaza(num_plaza, None, False, False)
            self.parking.lista_motos.append(nueva_plaza_moto)
            num_plaza += 1

        for i in range(cantidad_minusvalidos):
            nueva_plaza_minusvalidos = Plaza(num_plaza, None, False, False)
            self.parking.lista_minusvalidos.append(nueva_plaza_minusvalidos)
            num_plaza += 1

        cantidad_plazas_totales = cantidad_coches + cantidad_motos + cantidad_minusvalidos

        if (20 == cantidad_plazas_totales):
            return True
        else:
            return False

    def plaza_disponible(self, tipo):
        if (tipo == "coche"):
            for i in self.parking.lista_coches:
                if (i.ocupada == False and i.reservada == False):
                    return i.num_plaza


        elif (tipo == "moto"):
            for i in self.parking.lista_motos:
                if (i.ocupada == False and i.reservada == False):
                    return i.num_plaza

        elif (tipo == "minusvalido"):
            for i in self.parking.lista_minusvalidos:
                if (i.ocupada == False and i.reservada == False):
                    return i.num_plaza

        return -1

    def ingresar_vehiculo(self, id_cliente, matricula, tipo, vehiculo_repositorio, cliente_repositorio):
        servicio_vehiculo = vehiculo_service()

        if (self.plaza_disponible(tipo) != -1):
            # servicio_vehiculo.calcular_pin()
            entrada = datetime.now()
            nuevo_vehiculo = Vehiculo(matricula, tipo, self.plaza_disponible(tipo), "1234", entrada, None)

            vehiculo_repositorio.add_vehiculo(nuevo_vehiculo)
            longitud_coches = len(self.parking.lista_coches)
            longitud_motos = len(self.parking.lista_motos)
            if (tipo == "coche"):
                self.parking.lista_coches[nuevo_vehiculo.num_plaza - 1].vehiculo = nuevo_vehiculo
                self.parking.lista_coches[nuevo_vehiculo.num_plaza - 1].ocupada = True

            elif (tipo == "moto"):
                self.parking.lista_motos[nuevo_vehiculo.num_plaza - longitud_coches - 1].vehiculo = nuevo_vehiculo
                self.parking.lista_motos[nuevo_vehiculo.num_plaza - longitud_coches - 1].ocupada = True

            elif (tipo == "minusvalido"):
                self.parking.lista_minusvalidos[
                    nuevo_vehiculo.num_plaza - longitud_coches - longitud_motos - 1].vehiculo = nuevo_vehiculo
                self.parking.lista_minusvalidos[
                    nuevo_vehiculo.num_plaza - longitud_coches - longitud_motos - 1].ocupada = True
            else:
                print("Tipo incorrecto")

            cliente = Cliente(id_cliente, nuevo_vehiculo)
            cliente_repositorio.add_cliente(cliente)

        else:
            print("No quedan plazas disponibles de " + tipo + "\n")

    def retirar_vehiculo(self, matricula, num_plaza, pin, vehiculo_repositorio):

        buscar_vehiculo = vehiculo_repositorio.buscar_vehiculo_matricula(matricula)

        if (buscar_vehiculo != None and buscar_vehiculo.num_plaza == num_plaza and buscar_vehiculo.pin == pin):
            buscar_vehiculo.fecha_salida = datetime.now()
            print(buscar_vehiculo)
            self.calcular_precio(buscar_vehiculo)
            print(self.calcular_precio(buscar_vehiculo))
            self.lista_precios.append(self.calcular_precio(buscar_vehiculo))
            print(self.lista_precios)
            if (buscar_vehiculo.tipo == "coche"):
                for i in self.parking.lista_coches:
                    if (i.vehiculo == buscar_vehiculo):
                        i.vehiculo = None
                        i.ocupada = False

            if (buscar_vehiculo.tipo == "moto"):
                for i in self.parking.lista_motos:
                    if (i.vehiculo == buscar_vehiculo):
                        i.vehiculo = None
                        i.ocupada = False

            if (buscar_vehiculo.tipo == "minusvalido"):
                for i in self.parking.lista_minusvalidos:
                    if (i.vehiculo == buscar_vehiculo):
                        i.vehiculo = None
                        i.ocupada = False

    def calcular_precio(self, vehiculo):
        precio = 0
        tiempo = vehiculo.fecha_salida - vehiculo.fecha_entrada

        minutos = round((tiempo.seconds % 3600) / 60)

        if (vehiculo.tipo == "coche"):
            precio = 0.12

        elif (vehiculo.tipo == "moto"):
            precio = 0.08

        elif (vehiculo.tipo == "minusvalido"):
            precio = 0.10

        precio_total = round(precio * minutos,2)

        #self.lista_precios.append(precio_total)

        return precio_total


    def ingresar_vehiculo_abonado(self, matricula, dni):
        return

