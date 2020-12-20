from Models.Plaza import Plaza
from Models.Vehiculo import Vehiculo
from Models.Ticket import Ticket
from datetime import datetime
from Repository.vehiculo_repository import vehiculo_repository
from Models.Cliente import Cliente
from Service.vehiculo_service import vehiculo_service


class parking_service():
    def __init__(self, parking, facturacion_no_abonados):
        self.__parking = parking
        self.__facturacion_no_abonados = facturacion_no_abonados

    @property
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, parking):
        self.__parking = parking

    @property
    def facturacion_no_abonados(self):
        return self.__facturacion_no_abonados

    @facturacion_no_abonados.setter
    def facturacion_no_abonados(self, facturacion_no_abonados):
        self.__facturacion_no_abonados = facturacion_no_abonados

    #def __str__(self):
    #    return "%s" %(self.facturacion_no_abonados)

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

    def ingresar_vehiculo(self, id_cliente, matricula, tipo, vehiculo_repositorio, cliente_repositorio, ticket_repositorio):
        servicio_vehiculo = vehiculo_service()

        if (self.plaza_disponible(tipo) != -1):
            servicio_vehiculo.calcular_pin()
            entrada = datetime.now()
            nuevo_vehiculo = Vehiculo(matricula, tipo, self.plaza_disponible(tipo), servicio_vehiculo.calcular_pin(), entrada, None)

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
            ticket = Ticket(nuevo_vehiculo.matricula, nuevo_vehiculo.fecha_entrada, nuevo_vehiculo.num_plaza, nuevo_vehiculo.pin)
            ticket_repositorio.add_ticket(ticket)
            print(ticket)
        else:
            print("No quedan plazas disponibles de " + tipo + "\n")


    def retirar_vehiculo(self, matricula, num_plaza, pin, vehiculo_repositorio):

        buscar_vehiculo = vehiculo_repositorio.buscar_vehiculo_matricula(matricula)

        if (buscar_vehiculo != None and buscar_vehiculo.num_plaza == num_plaza and buscar_vehiculo.pin == pin):
            salida = buscar_vehiculo.fecha_salida = datetime.now()
            self.calcular_precio(buscar_vehiculo)
            print(f"El importe de su estancia es de {self.calcular_precio(buscar_vehiculo)} €")
            print("¡Pago realizado con éxito!\nPuede recoger su vehículo\nQue pase un buen día\n")
            factura_vehiculo = [buscar_vehiculo.fecha_entrada, salida, self.calcular_precio(buscar_vehiculo)]
            self.facturacion_no_abonados.append(factura_vehiculo)

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
        if buscar_vehiculo.num_plaza != num_plaza:
            print("Número de plaza incorrecta")
        if buscar_vehiculo.pin != pin:
            print("Código pin incorrecto")

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

        #self.facturacion_no_abonados.append(precio_total)

        return precio_total


    def ingresar_vehiculo_abonado(self, matricula, dni, cliente_abonado_repositorio):

        vehiculo = cliente_abonado_repositorio.buscar_vehiculo_matricula_dni(matricula, dni)
        #vehiculo_parking = self.encontrar_vehiculo_abonado_parking(matricula)
        longitud_coches = len(self.parking.lista_coches)
        longitud_motos = len(self.parking.lista_motos)
        if(vehiculo != None):# and vehiculo_parking != None
            #creo que lo mejor será pillar el tipo y a partir de ahí modificarlo directamente en la lista
            if(vehiculo.tipo == "coche"):
                self.parking.lista_coches[vehiculo.num_plaza -1].ocupada = True
            if(vehiculo.tipo == "moto"):
                self.parking.lista_motos[vehiculo.num_plaza -longitud_coches -1].ocupada = True
            if(vehiculo.tipo == "minusvalido"):
                self.parking.lista_minusvalidos[vehiculo.num_plaza -longitud_coches -longitud_motos -1].ocupada = True
            print("Puede depositar su vehículo\nQue pase un buen día\n")

    def retirar_vehiculo_abonado(self, matricula, num_plaza, pin, cliente_abonado_repositorio):
        vehiculo = cliente_abonado_repositorio.buscar_vehiculo_matricula(matricula)
        longitud_coches = len(self.parking.lista_coches)
        longitud_motos = len(self.parking.lista_motos)
        if(vehiculo != None and vehiculo.pin == pin and vehiculo.num_plaza == num_plaza):
            if(vehiculo.tipo == "coche"):
                self.parking.lista_coches[vehiculo.num_plaza -1].ocupada = False
            if(vehiculo.tipo == "moto"):
                self.parking.lista_motos[vehiculo.num_plaza -longitud_coches -1].ocupada = False
            if(vehiculo.tipo == "minusvalido"):
                self.parking.lista_minusvalidos[vehiculo.num_plaza -longitud_coches -longitud_motos -1].ocupada = False
            print("Datos introducidos correctamente\nPuede retirar su vehículo\n")
        else:
            print("Datos incorrectos\n")

    def consultar_facturacion_fechas(self, fecha1, fecha2):
        lista_facturacion_fechas = []
        for i in self.facturacion_no_abonados:
            if(fecha1<=i[1]<=fecha2):
                lista_facturacion_fechas.append(i)

        if(len(lista_facturacion_fechas)!=0):
            for i in lista_facturacion_fechas:
                print(i)
        else:
            print("No hay registros de facturación en el rango de fechas seleccionado")

    def consultar_estado_parking(self):
        libre = 0
        ocupada = 0
        abono_libre = 0
        abono_ocupada = 0

        for i in self.parking.lista_coches:
            if(i.ocupada == False and i.reservada == False):
                libre += 1
            elif(i.ocupada == True and i.reservada == False):
                ocupada += 1
            elif(i.ocupada == False and i.reservada == True):
                abono_libre += 1
            else:
                abono_ocupada += 1
        for i in self.parking.lista_motos:
            if(i.ocupada == False and i.reservada == False):
                libre += 1
            elif(i.ocupada == True and i.reservada == False):
                ocupada += 1
            elif(i.ocupada == False and i.reservada == True):
                abono_libre += 1
            else:
                abono_ocupada += 1

        for i in self.parking.lista_minusvalidos:
            if(i.ocupada == False and i.reservada == False):
                libre += 1
            elif(i.ocupada == True and i.reservada == False):
                ocupada += 1
            elif(i.ocupada == False and i.reservada == True):
                abono_libre += 1
            else:
                abono_ocupada += 1

        print(f"Plazas libres: {libre} \nPlazas ocupadas: {ocupada} \nPlazas abono libre: {abono_libre} "
              f"\nPlazas abono ocupada: {abono_ocupada}")
