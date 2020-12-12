from Service.parking_service import parking_service
from Models.Parking import Parking
from Models.Plaza import Plaza
from Repository.vehiculo_repository import vehiculo_repository
from Repository.cliente_repository import cliente_repository
from Service.vehiculo_service import vehiculo_service

parking = Parking([],[],[])
repositorio_vehiculo = vehiculo_repository([])
repositorio_cliente = cliente_repository([])
servicio_parking = parking_service(parking)
servicio_parking.asignar_plazas()
print(parking)

id_cliente = 1
servicio_parking.ingresar_vehiculo(id_cliente,"dfsadf","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(2,"dfsadfsdfsdf","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(3,"dfsadfsdfsdf","coche", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(4,"dfssadf","moto", repositorio_vehiculo, repositorio_cliente)
servicio_parking.ingresar_vehiculo(6,"dfasdfsdfasdfssadf","minusvalido", repositorio_vehiculo, repositorio_cliente)

print(parking)
