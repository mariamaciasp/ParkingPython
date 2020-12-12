from Models.Plaza import Plaza
from Models.Vehiculo import Vehiculo
from datetime import datetime
from Repository.vehiculo_repository import vehiculo_repository
from Models.Cliente import Cliente
from Service.vehiculo_service import vehiculo_service

class parking_service():
    def __init__(self, parking):
        self.__parking = parking

    @property
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, parking):
        self.__parking = parking

    #total 20 plazas, 14 coches, 3 minusválidos y 3 motos

    def asignar_plazas(self):
        num_plaza = 1
        cantidad_coches = 14
        cantidad_motos = 3
        cantidad_minusvalidos = 3

        self.parking.lista_coches = []
        self.parking.lista_motos = []
        self.parking.lista_minusvalidos = []

        for i in range(cantidad_coches):
            nueva_plaza_coche = Plaza (num_plaza, None, False, False)
            self.parking.lista_coches.append(nueva_plaza_coche)
            num_plaza += 1

        for i in range(cantidad_motos):
            nueva_plaza_moto = Plaza (num_plaza, None, False, False)
            self.parking.lista_motos.append(nueva_plaza_moto)
            num_plaza += 1

        for i in range(cantidad_minusvalidos):
            nueva_plaza_minusvalidos = Plaza (num_plaza, None, False, False)
            self.parking.lista_minusvalidos.append(nueva_plaza_minusvalidos)
            num_plaza += 1

        cantidad_plazas_totales = cantidad_coches + cantidad_motos + cantidad_minusvalidos

        if(20 == cantidad_plazas_totales):
            return True
        else:
            return False

    def plaza_disponible(self, tipo):
        if(tipo=="coche"):
            for i in self.parking.lista_coches:
                if(i.ocupada == False and i.reservada == False):
                    return i.num_plaza


        elif(tipo == "moto"):
            for i in self.parking.lista_motos:
                if(i.ocupada == False and i.reservada == False):
                    return i.num_plaza

        elif(tipo == "minusvalido"):
            for i in self.parking.lista_minusvalidos:
                if(i.ocupada == False and i.reservada == False):
                    return i.num_plaza

        return -1


    def ingresar_vehiculo(self, id_cliente, matricula, tipo, vehiculo_repositorio, cliente_repositorio):
        servicio_vehiculo = vehiculo_service()

        if(self.plaza_disponible(tipo) != -1):

            entrada = datetime.now()
            nuevo_vehiculo = Vehiculo(matricula, tipo, self.plaza_disponible(tipo), servicio_vehiculo.calcular_pin(), entrada, None)

            vehiculo_repositorio.add_vehiculo(nuevo_vehiculo)
            longitud_coches = len(self.parking.lista_coches)
            longitud_motos =len(self.parking.lista_motos)
            if(tipo == "coche"):
                self.parking.lista_coches[nuevo_vehiculo.num_plaza-1].vehiculo = nuevo_vehiculo
                self.parking.lista_coches[nuevo_vehiculo.num_plaza-1].ocupada = True

            elif(tipo == "moto"):
                self.parking.lista_motos[nuevo_vehiculo.num_plaza-longitud_coches-1].vehiculo = nuevo_vehiculo
                self.parking.lista_motos[nuevo_vehiculo.num_plaza-longitud_coches-1].ocupada = True

            elif(tipo == "minusvalido"):
                self.parking.lista_minusvalidos[nuevo_vehiculo.num_plaza-longitud_coches-longitud_motos-1].vehiculo = nuevo_vehiculo
                self.parking.lista_minusvalidos[nuevo_vehiculo.num_plaza-longitud_coches-longitud_motos-1].ocupada = True
            else:
                print("Tipo incorrecto")


            cliente = Cliente(id_cliente, nuevo_vehiculo)
            cliente_repositorio.add_cliente(cliente)

        else:
            print("No quedan plazas disponibles de " + tipo + "\n")


    def retirar_vehiculo(self, matricula, num_plaza, pin):

        return








