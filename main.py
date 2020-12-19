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
import pickle

parking = Parking([],[],[])
repositorio_cliente = cliente_repository()


vehiculo_abonado2 = Vehiculo("intento2","coche", 5, "1234", None, None)
vehiculo_abonado1 = Vehiculo("dfsadf","coche", 5, "1234", None, None)
lista_vehiculo=[vehiculo_abonado1, vehiculo_abonado2]
# Repo vehículo
bd_vehiculo_repo_w = open("./DataBase/vehiculo", "wb")
pickle.dump(lista_vehiculo, bd_vehiculo_repo_w)
bd_vehiculo_repo_w.close()
bd_vehiculo_repo_r = open("./DataBase/vehiculo", "rb")
lista_vehiculo_db = pickle.load(bd_vehiculo_repo_r)
bd_vehiculo_repo_r.close()
repositorio_vehiculo = vehiculo_repository(lista_vehiculo_db)
#

servicio_cliente_abonado = cliente_abonado_service([])

cliente_abonado1 = ClienteAbonado(1, vehiculo_abonado1, "44243716L","María","Padilla","tarjeta2","mensual","asfd", [])
cliente_abonado2 = ClienteAbonado(1, vehiculo_abonado2, "dni1","María","Padilla","tarjeta2","mensual","asfd", [])
lista_clientes_abonados = [cliente_abonado1, cliente_abonado2]

#Repo cliente abonado
bd_cliente_abonado_repo_w = open("./DataBase/cliente_abonado", "wb")
pickle.dump(lista_clientes_abonados, bd_cliente_abonado_repo_w)
bd_cliente_abonado_repo_w.close()
bd_cliente_abonado_repo_r = open("./DataBase/cliente_abonado", "rb")
lista_clientes_abonados_bd = pickle.load(bd_cliente_abonado_repo_r)
bd_cliente_abonado_repo_r.close()
repositorio_cliente_abonado = cliente_abonado_repository(lista_clientes_abonados_bd)

#
abono_cliente1 = Abono(cliente_abonado2, datetime.now(), servicio_cliente_abonado.calcular_fecha_cancelacion("mensual", datetime.now(), cliente_abonado2))
abono_cliente2 = Abono(cliente_abonado1, datetime.now(), servicio_cliente_abonado.calcular_fecha_cancelacion("mensual", datetime.now(), cliente_abonado1))
#
lista_abonos = [abono_cliente1, abono_cliente2]

# Repo abono
bd_abono_repo_w = open("./DataBase/abono", "wb")
pickle.dump(lista_abonos, bd_abono_repo_w)
bd_abono_repo_w.close()
bd_abono_repo_r = open("./DataBase/abono", "rb")
lista_abonos_bd = pickle.load(bd_abono_repo_r)
bd_abono_repo_r.close()
repositorio_abono = abono_repository(lista_abonos_bd)

# Repo facturacion abonos
bd_facturacion_repo_w = open("./DataBase/facturacion", "wb")
pickle.dump([], bd_facturacion_repo_w)
bd_facturacion_repo_w.close()
bd_facturacion_repo_r = open("./DataBase/facturacion", "rb")
lista_facturacion = pickle.load(bd_facturacion_repo_r)
bd_facturacion_repo_r.close()
repositorio_facturacion = facturacion_abonos_repository(lista_facturacion)


vehiculo_abonado3 = Vehiculo("asfsadf","coche", 5, "1234", None, None)
cliente_abonado_3 = ClienteAbonado(1, vehiculo_abonado3, "16L","Margsdfgía","Padilla","tarjeta2","mensual","asfd", [])
abono_prueba3 = Abono(cliente_abonado_3, datetime.now(), servicio_cliente_abonado.calcular_fecha_cancelacion("mensual", datetime.now(), cliente_abonado_3))
#repositorio_abono.add_abono(abono_prueba)
repositorio_cliente_abonado.add_cliente_abonado(cliente_abonado_3)
repositorio_abono.add_abono(abono_prueba3)

print(repositorio_abono)

servicio_parking = parking_service(parking, [])
servicio_parking.asignar_plazas()
servicio_abono = abono_service()
##servicio_cliente_abonado.dar_alta_abonado(1,"1234abc","dni","María","Macías","maria@mail.com","tarjeta","trimestral","coche", repositorio_cliente_abonado, repositorio_abono, servicio_parking, repositorio_vehiculo)

print("entrar")
print(repositorio_abono.buscar_abono("dni1"))
print("entrar")
print()
print(repositorio_cliente_abonado)
print("mierda")

print(parking)
servicio_parking.ingresar_vehiculo_abonado("1234abc","dni",repositorio_cliente_abonado)
servicio_parking.consultar_estado_parking()
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
print("caracola")
print(parking)
servicio_parking.retirar_vehiculo_abonado("1234abc",1,"1234", repositorio_cliente_abonado)

op = int(input("pulse 1"))
if(op ==1):
    servicio_parking.retirar_vehiculo("dfsadf", 1,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("10", 2,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("1", 15,"1234", repositorio_vehiculo)
    servicio_parking.retirar_vehiculo("2", 18,"1234", repositorio_vehiculo)

print(parking)

print(servicio_parking.facturacion_no_abonados)

print(repositorio_abono.buscar_abono("44243716L"))
print("caracola")

abono_cliente1.fecha_cancelacion = abono_cliente1.fecha_cancelacion.replace(month=(12))
abono_cliente1.fecha_cancelacion = abono_cliente1.fecha_cancelacion.replace(day=(1))
abono_cliente1.fecha_cancelacion = abono_cliente1.fecha_cancelacion.replace(year=(2020))

print(repositorio_cliente_abonado)

##servicio_cliente_abonado.modificar_abono("dni2", repositorio_abono)
print("1")
print(repositorio_cliente_abonado)
print("aqui")
print(repositorio_abono)
##servicio_cliente_abonado.baja_abono("dni2", repositorio_abono, repositorio_cliente_abonado, repositorio_facturacion)
print("es")
print(repositorio_abono.buscar_abono("44243716L"))
print(repositorio_abono.borrar_abono("44243716L"))
print("creo1")
print("ahora")
##print(repositorio_abono)
print()
print(repositorio_cliente_abonado)
print("facturacion")
print(repositorio_facturacion)

print("caducidad por mes")
##servicio_abono.caducidad_abono_mes(repositorio_abono, 1)
print("fin caducidad mes")

##servicio_abono.caducidad_proximos_10_dias(repositorio_abono)
print("2.0")
##servicio_abono.caducidad_proximos_10_dias_timedelta(repositorio_abono)

print("imprimir abonos")
print(servicio_cliente_abonado)

servicio_cliente_abonado.consulta_abonos_anual()
print()
fecha1 = datetime(2020, 12, 17, 13, 56)
print(fecha1)
fecha2 = datetime(2020, 12, 17, 14)
print(fecha2)
servicio_parking.consultar_facturacion_fechas(fecha1,fecha2)
print()
print(parking)
servicio_parking.consultar_estado_parking()
