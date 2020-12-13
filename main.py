from Service.parking_service import parking_service
from Models.Parking import Parking
from Models.Plaza import Plaza
from Models.ClienteAbonado import ClienteAbonado
from Models.Vehiculo import Vehiculo
from Repository.vehiculo_repository import vehiculo_repository
from Repository.cliente_repository import cliente_repository
from Repository.cliente_abonado_repository import cliente_abonado_repository
from Service.vehiculo_service import vehiculo_service

parking = Parking([],[],[])
repositorio_vehiculo = vehiculo_repository([])
repositorio_cliente = cliente_repository([])
repositorio_cliente_abonado = cliente_abonado_repository([])
servicio_parking = parking_service(parking, [])
servicio_parking.asignar_plazas()
print(parking)

id_cliente = 1
servicio_parking.ingresar_vehiculo(1,"dfsadf","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(2,"10","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(3,"dfsadfsdfsdf","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(4,"1","moto", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(4,"dfssdfsdfadf","moto", repositorio_vehiculo, repositorio_cliente)

servicio_parking.ingresar_vehiculo(6,"2","minusvalido", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(6,"dfasdfssdfsdfasdfssadf","minusvalido", repositorio_vehiculo, repositorio_cliente)

print(parking)
op = int(input("pulse 1"))
if(op ==1):
    servicio_parking.retirar_vehiculo("dfsadf", 1,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("10", 2,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("1", 15,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("2", 18,"1234", repositorio_vehiculo)

print(parking)

print(servicio_parking.lista_precios)
vehiculo_abonado_1 = Vehiculo("dfsadf","coche", 5, "1234", None, None)
cliente_abonado_1 = ClienteAbonado(1, vehiculo_abonado_1, "44243716L")

repositorio_cliente_abonado.add_cliente_abonado(cliente_abonado_1)

print(repositorio_cliente_abonado)
print(cliente_abonado_1)
