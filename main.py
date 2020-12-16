from Service.parking_service import parking_service
from Models.Parking import Parking
from Models.Plaza import Plaza
from Models.Abono import Abono
from Models.ClienteAbonado import ClienteAbonado
from Models.Vehiculo import Vehiculo
from Repository.vehiculo_repository import vehiculo_repository
from Repository.cliente_repository import cliente_repository
from Repository.cliente_abonado_repository import cliente_abonado_repository
from Repository.abono_repository import abono_repository
from Repository.facturacion_abonos_repository import facturacion_abonos_repository
from Service.vehiculo_service import vehiculo_service
from Service.cliente_abonado_service import cliente_abonado_service
from Service.abono_service import abono_service
from datetime import datetime

parking = Parking([],[],[])
repositorio_vehiculo = vehiculo_repository([])
repositorio_cliente = cliente_repository([])
repositorio_cliente_abonado = cliente_abonado_repository([])
repositorio_abono = abono_repository([])
repositorio_facturacion = facturacion_abonos_repository([])
servicio_parking = parking_service(parking, [])
servicio_parking.asignar_plazas()
servicio_cliente_abonado = cliente_abonado_service([])
servicio_abono = abono_service()
servicio_cliente_abonado.dar_alta_abonado(1,"1234abc","dni","María","Macías","maria@mail.com","tarjeta","trimestral","coche", repositorio_cliente_abonado, repositorio_abono, servicio_parking, repositorio_vehiculo)
print(repositorio_cliente_abonado)
#print(servicio_cliente_abonado.calcular_fecha_cancelacion("anual", datetime.now()) )
print(parking)
servicio_parking.ingresar_vehiculo_abonado("1234abc","dni",repositorio_cliente_abonado)
id_cliente = 1
servicio_parking.ingresar_vehiculo(1,"dfsadf","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(2,"10","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(3,"dfsadfsdfsdf","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(4,"1","moto", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(4,"dfssdfsdfadf","moto", repositorio_vehiculo, repositorio_cliente)

servicio_parking.ingresar_vehiculo(6,"2","minusvalido", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(6,"dfasdfssdfsdfasdfssadf","minusvalido", repositorio_vehiculo, repositorio_cliente)
print("mirar diferencia")
print(repositorio_cliente_abonado)
servicio_cliente_abonado.modificar_datos_abonado("dni", "dni2", "Pepe", "Botella", "nuevaTarjeta", "nuevoEmail",repositorio_cliente_abonado)
print(repositorio_cliente_abonado)
print(parking)
servicio_parking.retirar_vehiculo_abonado("1234abc",1,"1234", repositorio_cliente_abonado)
op = int(input("pulse 1"))
if(op ==1):
    servicio_parking.retirar_vehiculo("dfsadf", 1,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("10", 2,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("1", 15,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("2", 18,"1234", repositorio_vehiculo)

print(parking)

print(servicio_parking.lista_precios)
vehiculo_abonado_1 = Vehiculo("dfsadf","coche", 5, "1234", None, None)
cliente_abonado_1 = ClienteAbonado(1, vehiculo_abonado_1, "44243716L","María","Padilla","tarjeta2","mensual","asfd", [])
abono_prueba = Abono(cliente_abonado_1, datetime.now(), servicio_cliente_abonado.calcular_fecha_cancelacion("mensual", datetime.now(), cliente_abonado_1))
repositorio_abono.add_abono(abono_prueba)
repositorio_cliente_abonado.add_cliente_abonado(cliente_abonado_1)
abono_prueba.fecha_cancelacion = abono_prueba.fecha_cancelacion.replace(month=(12))
abono_prueba.fecha_cancelacion = abono_prueba.fecha_cancelacion.replace(day=(16))
#abono_prueba.fecha_cancelacion = abono_prueba.fecha_cancelacion.replace(year=(2021))

print(repositorio_cliente_abonado)

servicio_cliente_abonado.modificar_abono("dni2", repositorio_abono)
print("1")
print(repositorio_cliente_abonado)
print("aqui")
print(repositorio_abono)
servicio_cliente_abonado.baja_abono("dni2", repositorio_abono, repositorio_cliente_abonado, repositorio_facturacion)
repositorio_abono.borrar_abono("dni2")
print("ahora")
print(repositorio_abono)
print()
print(repositorio_cliente_abonado)
print(repositorio_facturacion)

print("caducidad por mes")
servicio_abono.caducidad_abono_mes(repositorio_abono, 1)
print("fin caducidad mes")

#servicio_abono.caducidad_proximos_10_dias(repositorio_abono)
print("2.0")
print(servicio_abono.caducidad_proximos_10_dias_timedelta(repositorio_abono))
