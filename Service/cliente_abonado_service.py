from datetime import datetime
from Models.Vehiculo import Vehiculo
from Models.ClienteAbonado import ClienteAbonado
from Models.Abono import Abono
from Models.FacturacionAbonos import FacturacionAbonos

class cliente_abonado_service():
    def __init__(self, abonados):
        self.__abonados = abonados

    @property
    def abonados(self):
        return self.__abonados

    @abonados.setter
    def abonados(self, abonados):
        self.__abonados = abonados

    def dar_alta_abonado(self, id_cliente, matricula, dni, nombre, apellidos, email, tarjeta, tipo_abono, tipo_plaza,
                         cliente_abonado_repositorio, abono_repositorio, servicio_parking, vehiculo_repositorio):

        if(servicio_parking.plaza_disponible(tipo_plaza)!= -1):
            nuevo_vehiculo = Vehiculo(matricula, tipo_plaza, servicio_parking.plaza_disponible(tipo_plaza),"1234", None, None)
            nuevo_cliente_abonado = ClienteAbonado(id_cliente, nuevo_vehiculo, dni, nombre, apellidos, tarjeta, tipo_abono, email,)
            nuevo_abono = Abono(nuevo_cliente_abonado, datetime.now(), self.calcular_fecha_cancelacion(tipo_abono, datetime.now(), nuevo_cliente_abonado))

            vehiculo_repositorio.add_vehiculo(nuevo_vehiculo)
            cliente_abonado_repositorio.add_cliente_abonado(nuevo_cliente_abonado)
            abono_repositorio.add_abono(nuevo_abono)
            self.asignar_plaza_abonado(servicio_parking, tipo_plaza, nuevo_vehiculo)

            return True

        else:
            print("No hay plazas disponibles de tipo " + tipo_plaza)
            return False


    def calcular_fecha_cancelacion(self, tipo_abono, fecha_finalizacion, cliente):
        precio_mesual = 25
        precio_trimestral =70
        precio_semestral = 130
        precio_anual = 200

        if(tipo_abono == "mensual"):
            cliente.facturado.append(precio_mesual)
            if(fecha_finalizacion.month == 12):
                fecha_finalizacion = fecha_finalizacion.replace(year=(fecha_finalizacion.year+1))
                fecha_finalizacion = fecha_finalizacion.replace(month=1)
            else:
                fecha_finalizacion = fecha_finalizacion.replace(month=(fecha_finalizacion.month+1))

        if(tipo_abono == "trimestral"):
            cliente.facturado.append(precio_trimestral)
            if(fecha_finalizacion.month >= 10):
                fecha_finalizacion = fecha_finalizacion.replace(year=(fecha_finalizacion.year+1))

                if(fecha_finalizacion.month == 10):
                    fecha_finalizacion = fecha_finalizacion.replace(month=1)
                elif(fecha_finalizacion.month == 11):
                    fecha_finalizacion = fecha_finalizacion.replace(month=2)
                else:
                    fecha_finalizacion = fecha_finalizacion.replace(month=3)
            else:
                fecha_finalizacion = fecha_finalizacion.replace(month=(fecha_finalizacion.month+3))

        if(tipo_abono == "semestral"):
            cliente.facturado.append(precio_semestral)
            if(fecha_finalizacion.month >= 7):
                fecha_finalizacion = fecha_finalizacion.replace(month=(fecha_finalizacion.month-6))
                fecha_finalizacion = fecha_finalizacion.replace(year=(fecha_finalizacion.year+1))
            else:
                fecha_finalizacion = fecha_finalizacion.replace(month=(fecha_finalizacion.month+6))

        if(tipo_abono == "anual"):
            cliente.facturado.append(precio_anual)
            fecha_finalizacion = fecha_finalizacion.replace(year=(fecha_finalizacion.year+1))

        return fecha_finalizacion


    def asignar_plaza_abonado(self, servicio_parking, tipo_plaza, vehiculo):

        if(servicio_parking.plaza_disponible(tipo_plaza)!= -1):
            longitud_coches = len(servicio_parking.parking.lista_coches)
            longitud_motos = len(servicio_parking.parking.lista_motos)

            if (tipo_plaza == "coche"):
                servicio_parking.parking.lista_coches[vehiculo.num_plaza - 1].vehiculo = vehiculo
                servicio_parking.parking.lista_coches[vehiculo.num_plaza - 1].reservada = True

            elif (tipo_plaza == "moto"):
                servicio_parking.parking.lista_motos[vehiculo.num_plaza - longitud_coches - 1].vehiculo = vehiculo
                servicio_parking.parking.lista_motos[vehiculo.num_plaza - longitud_coches - 1].ocupada = True

            elif (tipo_plaza == "minusvalido"):
                servicio_parking.parking.lista_minusvalidos[
                    vehiculo.num_plaza - longitud_coches - longitud_motos - 1].vehiculo = vehiculo
                servicio_parking.parking.lista_minusvalidos[
                    vehiculo.num_plaza - longitud_coches - longitud_motos - 1].ocupada = True
            else:
                print("Tipo incorrecto")


    def modificar_datos_abonado(self, dni, nuevo_dni, nombre, apellidos, tarjeta, email, cliente_abonado_repositorio):
        cliente = cliente_abonado_repositorio.buscar_cliente_dni(dni)

        if(cliente != None):
            cliente.dni = nuevo_dni
            cliente.nombre = nombre
            cliente.apellidos = apellidos
            cliente.num_tarjeta = tarjeta
            cliente.email = email
            return True
        else:
            print("Cliente incorrecto")
            return False

    def modificar_abono(self, dni_cliente, abono_repositorio):
        abono = abono_repositorio.buscar_abono(dni_cliente)
        abono.fecha_cancelacion = self.calcular_fecha_cancelacion(abono.cliente.tipo_abono, abono.fecha_cancelacion, abono.cliente)
        print(abono)

    def sumar_array(self, dni_cliente, abono_repositorio):
        cliente_lista_facturacion = abono_repositorio.buscar_abono(dni_cliente).cliente.facturado
        suma = 0
        for i in cliente_lista_facturacion:
            suma += i
        return suma

    def baja_abono(self, dni_cliente, abono_repositorio, cliente_abonado_repositorio, facturacion_repositorio):
        cliente_borrar = abono_repositorio.buscar_abono(dni_cliente).cliente
        abono_cliente_borrar = abono_repositorio.buscar_abono(dni_cliente)
        crear_facturacion = FacturacionAbonos(cliente_borrar.dni, cliente_borrar.nombre, cliente_borrar.apellidos,
                                              self.sumar_array(dni_cliente, abono_repositorio),
                                              abono_cliente_borrar.fecha_activacion, abono_cliente_borrar.fecha_cancelacion)
        facturacion_repositorio.add_facturacion(crear_facturacion)
        abono_repositorio.borrar_abono(dni_cliente)
        cliente_abonado_repositorio.borrar_cliente_dni(dni_cliente)

