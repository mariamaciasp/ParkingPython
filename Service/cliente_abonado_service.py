from datetime import datetime
from Models.Vehiculo import Vehiculo
from Models.ClienteAbonado import ClienteAbonado
from Models.Abono import Abono

class cliente_abonado_service():
    def __init__(self, abonados):
        self.__abonados = abonados

    @property
    def abonados(self):
        return self.__abonados

    @abonados.setter
    def abonados(self, abonados):
        self.__abonados = abonados

    def dar_alta_abonado(self, id_cliente, matricula, dni, tarjeta, tipo_abono, tipo_plaza,
                         cliente_abonado_repositorio, abono_repositorio, servicio_parking):

        if(servicio_parking.plaza_disponible(tipo_plaza)!= -1):
            nuevo_vehiculo = Vehiculo(matricula, tipo_plaza, servicio_parking.plaza_disponible(tipo_plaza),"1234", None, None)
            nuevo_cliente_abonado = ClienteAbonado(id_cliente, nuevo_vehiculo, dni)
            nuevo_abono = Abono(nuevo_cliente_abonado, tarjeta, tipo_abono, datetime.now(), self.calcular_fecha_cancelacion(tipo_abono))

            cliente_abonado_repositorio.add_cliente_abonado(nuevo_cliente_abonado)
            abono_repositorio.add_abono(nuevo_abono)
            return True

        else:
            print("No hay plazas disponibles de tipo " + tipo_plaza)
            return False


    def calcular_fecha_cancelacion(self, tipo_abono):

        fecha_finalizacion = datetime.now()

        if(tipo_abono == "mensual"):

            if(fecha_finalizacion.month == 12):
                fecha_finalizacion = fecha_finalizacion.replace(year=(fecha_finalizacion.year+1))
                fecha_finalizacion = fecha_finalizacion.replace(month=1)
            else:
                fecha_finalizacion = fecha_finalizacion.replace(month=(fecha_finalizacion.month+1))

        if(tipo_abono == "trimestral"):
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
            if(fecha_finalizacion.month >= 7):
                fecha_finalizacion = fecha_finalizacion.replace(month=(fecha_finalizacion.month-6))
                fecha_finalizacion = fecha_finalizacion.replace(year=(fecha_finalizacion.year+1))
            else:
                fecha_finalizacion = fecha_finalizacion.replace(month=(fecha_finalizacion.month+6))

        if(tipo_abono == "anual"):
            fecha_finalizacion = fecha_finalizacion.replace(year=(fecha_finalizacion.year+1))

        return fecha_finalizacion

