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
servicio_cliente_abonado = cliente_abonado_service()
servicio_parking = parking_service(parking, [])
servicio_parking.asignar_plazas()
servicio_abono = abono_service()

# Repo cliente abonado
vehiculo_abonado2 = Vehiculo("intento2","coche", 5, "1234", None, None)
vehiculo_abonado1 = Vehiculo("dfsadf","coche", 5, "1234", None, None)
lista_vehiculo=[vehiculo_abonado1, vehiculo_abonado2]

bd_vehiculo_repo_w = open("./DataBase/vehiculo", "wb")
pickle.dump(lista_vehiculo, bd_vehiculo_repo_w)
bd_vehiculo_repo_w.close()
bd_vehiculo_repo_r = open("./DataBase/vehiculo", "rb")
lista_vehiculo_db = pickle.load(bd_vehiculo_repo_r)
bd_vehiculo_repo_r.close()
repositorio_vehiculo = vehiculo_repository(lista_vehiculo_db)
#

#Repo cliente abonado
cliente_abonado1 = ClienteAbonado(1, vehiculo_abonado1, "44243716L","María","Padilla","tarjeta2","mensual","asfd", [])
cliente_abonado2 = ClienteAbonado(1, vehiculo_abonado2, "dni1","María","Padilla","tarjeta2","mensual","asfd", [])
lista_clientes_abonados = [cliente_abonado1, cliente_abonado2]

bd_cliente_abonado_repo_w = open("./DataBase/cliente_abonado", "wb")
pickle.dump(lista_clientes_abonados, bd_cliente_abonado_repo_w)
bd_cliente_abonado_repo_w.close()
bd_cliente_abonado_repo_r = open("./DataBase/cliente_abonado", "rb")
lista_clientes_abonados_bd = pickle.load(bd_cliente_abonado_repo_r)
bd_cliente_abonado_repo_r.close()
repositorio_cliente_abonado = cliente_abonado_repository(lista_clientes_abonados_bd)
#

# Repo abonado
abono_cliente1 = Abono(cliente_abonado1, datetime.now(), servicio_cliente_abonado.calcular_fecha_cancelacion("mensual", datetime.now(), cliente_abonado1))
abono_cliente2 = Abono(cliente_abonado2, datetime.now(), servicio_cliente_abonado.calcular_fecha_cancelacion("mensual", datetime.now(), cliente_abonado2))
lista_abonos = [abono_cliente1, abono_cliente2]

bd_abono_repo_w = open("./DataBase/abono", "wb")
pickle.dump(lista_abonos, bd_abono_repo_w)
bd_abono_repo_w.close()
bd_abono_repo_r = open("./DataBase/abono", "rb")
lista_abonos_bd = pickle.load(bd_abono_repo_r)
bd_abono_repo_r.close()
repositorio_abono = abono_repository(lista_abonos_bd)
#

# Repo facturacion abonos
bd_facturacion_repo_w = open("./DataBase/facturacion", "wb")
pickle.dump([], bd_facturacion_repo_w)
bd_facturacion_repo_w.close()
bd_facturacion_repo_r = open("./DataBase/facturacion", "rb")
lista_facturacion = pickle.load(bd_facturacion_repo_r)
bd_facturacion_repo_r.close()
repositorio_facturacion = facturacion_abonos_repository(lista_facturacion)
#

print("¡Bienvenido a parking Triana!\n")
#opcion = int(input("pulse 1"))
id = 0

while True:
    try:
        opcion = int(input("Seleccione la opción que desee:\n1- Cliente \n2- Administrador \n"))
        if opcion == 1:
            try:
                zona_cliente = int(input("1- Depositar vehículo\n2- Retirar vehículo "
                                         "\n3- Depositar vehículo abonado\n4- Retirar vehículo abonado\n0- Salir \n"))
                while True:
                    if zona_cliente == 1:
                        print()
                        id += 1
                        matricula = input("Introduzca la matrícula del vehículo\n")
                        while True:
                            try:
                                seleccion_tipo = int(input("Seleccione el tipo de vehículo:\n1- Coche\n2- Moto\n3- Movilidad reducida\n"))
                                if seleccion_tipo == 1:
                                    tipo = "coche"
                                    break
                                elif seleccion_tipo == 2:
                                    tipo = "moto"
                                    break
                                elif seleccion_tipo == 3:
                                    tipo = "minusvalido"
                                    break
                                else:
                                    print("Opción incorrecta")
                            except ValueError:
                                print("Introduzca un valor numérico\n")

                        servicio_parking.ingresar_vehiculo(id, matricula, tipo, repositorio_vehiculo, repositorio_cliente)
                        print(parking)

                    elif zona_cliente == 0:
                        print("Volver..")
                        break
            except ValueError:
                print("Introduzca un valor numérico\n")


        elif opcion ==2:
            print("opcion2")
        elif opcion == 0:
            print("Saliendo..")
            break
        else:
            print("Opción incorrecta")
    except ValueError:
        print("Introduzca un valor numérico\n")


