from Service.parking_service import parking_service
from Models.Parking import Parking
from Models.Abono import Abono
from Models.Admin import Admin
from Models.ClienteAbonado import ClienteAbonado
from Models.Vehiculo import Vehiculo
from Repository.vehiculo_repository import vehiculo_repository
from Repository.cliente_repository import cliente_repository
from Repository.cliente_abonado_repository import cliente_abonado_repository
from Repository.abono_repository import abono_repository
from Repository.facturacion_abonos_repository import facturacion_abonos_repository
from Repository.ticket_repository import ticket_repository
from Repository.admin_repository import admin_repository
from Repository.imagen_repository import imagen_repository
from Service.cliente_abonado_service import cliente_abonado_service
from Service.abono_service import abono_service
from datetime import datetime
import pickle

parking = Parking([],[],[])
repositorio_cliente = cliente_repository()
repositorio_imagen = imagen_repository()
servicio_cliente_abonado = cliente_abonado_service()
servicio_parking = parking_service(parking, [])
servicio_parking.asignar_plazas()
servicio_abono = abono_service()

# Repo admin
admin1 = Admin("maria1", "1234")
admin2 = Admin("admin", "1234")
lista_admin = [admin1, admin2]

bd_admin_repo_w = open("./DataBase/admin", "wb")
pickle.dump(lista_admin, bd_admin_repo_w)
bd_admin_repo_w.close()
bd_admin_repo_r = open("./DataBase/admin", "rb")
lista_admin_db = pickle.load(bd_admin_repo_r)
bd_admin_repo_r.close()
repositorio_admin = admin_repository(lista_admin_db)
#

# Repo vehículo
vehiculo_abonado2 = Vehiculo("matricula1","coche", 5, "1234", None, None)
vehiculo_abonado1 = Vehiculo("matricula2","coche", 5, "1234", None, None)
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
#cliente_abonado1 = ClienteAbonado(1, vehiculo_abonado1, "44243716L","María","Padilla","tarjeta1","mensual","mail", [])
#cliente_abonado2 = ClienteAbonado(1, vehiculo_abonado2, "dni_abonado2","Pepe","Acosta","tarjeta2","mensual","mail", [])
lista_clientes_abonados = [] #cliente_abonado1, cliente_abonado2

bd_cliente_abonado_repo_w = open("./DataBase/cliente_abonado", "wb")
pickle.dump(lista_clientes_abonados, bd_cliente_abonado_repo_w)
bd_cliente_abonado_repo_w.close()
bd_cliente_abonado_repo_r = open("./DataBase/cliente_abonado", "rb")
lista_clientes_abonados_bd = pickle.load(bd_cliente_abonado_repo_r)
bd_cliente_abonado_repo_r.close()
repositorio_cliente_abonado = cliente_abonado_repository(lista_clientes_abonados_bd)
#

# Repo abono
#abono_cliente1 = Abono(cliente_abonado1, datetime.now(), servicio_cliente_abonado.calcular_fecha_cancelacion("mensual", datetime.now(), cliente_abonado1))
#abono_cliente2 = Abono(cliente_abonado2, datetime.now(), servicio_cliente_abonado.calcular_fecha_cancelacion("mensual", datetime.now(), cliente_abonado2))
lista_abonos = [] #abono_cliente1, abono_cliente2

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

# Repo ticket
bd_ticket_repo_w = open("./DataBase/ticket", "wb")
pickle.dump([], bd_ticket_repo_w)
bd_ticket_repo_w.close()
bd_ticket_repo_r = open("./DataBase/ticket", "rb")
lista_ticket = pickle.load(bd_ticket_repo_r)
bd_ticket_repo_r.close()
repositorio_ticket = ticket_repository(lista_ticket)


id = 0
servicio_cliente_abonado.dar_alta_abonado(0,"1234abc","dni","María","Macías","maria@mail.com","tarjeta","trimestral","coche", repositorio_cliente_abonado, repositorio_abono, servicio_parking, repositorio_vehiculo)
#servicio_cliente_abonado.dar_alta_abonado(00, cliente_abonado1.vehiculo.matricula,cliente_abonado1.dni, cliente_abonado1.nombre,
 #                                         cliente_abonado1.apellidos, cliente_abonado1.email, cliente_abonado1.num_tarjeta,
  #                                        cliente_abonado1.tipo_abono, cliente_abonado1.vehiculo.tipo, repositorio_cliente_abonado, repositorio_abono, servicio_parking, repositorio_vehiculo)
#servicio_cliente_abonado.dar_alta_abonado(000, cliente_abonado2.vehiculo.matricula,cliente_abonado2.dni, cliente_abonado2.nombre,
   #                                       cliente_abonado2.apellidos, cliente_abonado2.email, cliente_abonado2.num_tarjeta,
    #                                      cliente_abonado2.tipo_abono, cliente_abonado2.vehiculo.tipo, repositorio_cliente_abonado, repositorio_abono, servicio_parking, repositorio_vehiculo)


# Comentar, puesto para saber pin de los abonados dados de alta
#print(repositorio_vehiculo)

print("¡Bienvenido a parking Triana!\n")

while True:
    try:
        opcion = int(input("Seleccione la opción que desee:\n1- Cliente \n2- Administrador \n0- Cerrar programa \n"))
        if opcion == 1:
            try:
                zona_cliente = int(input("1- Depositar vehículo\n2- Retirar vehículo "
                                         "\n3- Depositar vehículo abonado\n4- Retirar vehículo abonado\n0- Salir \n"))
                while True:
                    if zona_cliente == 1:
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
                        servicio_parking.ingresar_vehiculo(id, matricula, tipo, repositorio_vehiculo, repositorio_cliente, repositorio_ticket,
                                                           repositorio_cliente_abonado)
                        break
                    elif zona_cliente == 2:
                        retirar_matricula = input("Introduzca la matrícula del vehículo\n")
                        while True:
                            try:
                                id_plaza = int(input("Introduzca el número de plaza\n"))
                                break
                            except ValueError:
                                print("Plaza incorrecta. Introduzca un número\n")
                        while True:
                            try:
                                retirar_pin = int(input("Introduzca el código pin\n"))
                                break
                            except ValueError:
                                print("Pin incorrecto. Introduzca un número\n")
                        servicio_parking.retirar_vehiculo(retirar_matricula, id_plaza, retirar_pin, repositorio_vehiculo)
                        break
                    elif zona_cliente == 3:
                        ingresar_abonado_matricula = input("Introduzca la matrícula del vehículo\n")
                        ingresar_dni_abonado = input("Introduzca su DNI\n")
                        servicio_parking.ingresar_vehiculo_abonado(ingresar_abonado_matricula, ingresar_dni_abonado, repositorio_cliente_abonado)
                        print()
                        break
                    elif zona_cliente == 4:
                        retirar_abonado_matricula = input("Introduzca la matrícula del vehículo\n")
                        while True:
                            try:
                                id_plaza_abonado = int(input("Introduzca el número de plaza\n"))
                                break
                            except ValueError:
                                print("Plaza incorrecta. Introduzca un número\n")

                        while True:
                            try:
                                retirar_pin_abonado = int(input("Introduzca el código pin\n"))
                                break
                            except ValueError:
                                print("Pin incorrecto. Introduzca un número\n")

                        servicio_parking.retirar_vehiculo_abonado(retirar_abonado_matricula, id_plaza_abonado, retirar_pin_abonado, repositorio_cliente_abonado)
                        break
                    elif zona_cliente == 0:
                        print("Volviendo..\n")
                        break
                    else:
                        print("Opción incorrecta\n")
                        break
            except ValueError:
                print("Introduzca un valor numérico\n")

        elif opcion ==2:
            usuario = input("Introduzca su usuario:\n")
            password = input("Introduzca su contraseña:\n")
            inicio_sesion = repositorio_admin.buscar_admin(usuario, password)

            if(inicio_sesion!=None):
                print("Sesión iniciada con éxito")
                while True:
                    try:
                        opcion_admin = int(input("\nSeleccione la opción que desee:\n1- Consultar estado parking \n2- Facturación \n"
                                        "3- Consulta abonos anuales \n4- Gestionar abonos\n5- Caducidad de abonos\n"
                                        "6- Consulta imágenes\n0- Salir\n"))

                        if opcion_admin == 1:
                            servicio_parking.consultar_estado_parking()
                        elif opcion_admin == 2:
                            while True:
                                try:
                                    print("Introduzca las dos fechas de entre las que desea conocer la facturación\nIntroduzca los siguientes datos:\nFecha inicial")
                                    dia1 = int(input("Día "))
                                    mes1 = int(input("Mes "))
                                    anio1 = int(input("Año "))
                                    hora1 = int(input("Hora "))
                                    minuto1 = int(input("Minuto "))
                                    fecha1 = datetime(anio1, mes1, dia1, hora1, minuto1)
                                    print("Introduzca la fecha final:\n")
                                    dia2 = int(input("Día "))
                                    mes2 = int(input("Mes "))
                                    anio2 = int(input("Año "))
                                    hora2 = int(input("Hora "))
                                    minuto2 = int(input("Minuto "))
                                    fecha2 = datetime(anio2, mes2, dia2, hora2, minuto2)
                                    #hay que formatear esa fecha y ponerla legible, poner el array legible
                                    print(fecha1, "-",fecha2)
                                    servicio_parking.consultar_facturacion_fechas(fecha1, fecha2)
                                    break
                                except ValueError:
                                    print("Introduzca un valor numérico y fecha existente\n")
                        elif opcion_admin == 3:
                            print("Abonos anuales:")
                            servicio_cliente_abonado.consulta_abonos_anual()
                        elif opcion_admin == 4:
                            abonos_opciones = int(input("1- Alta nuevo abono\n2- Modificar abono\n3- Baja abono\n0- Salir\n"))
                            if abonos_opciones == 1:
                                id += 1
                                alta_matricula = input("Matrícula ")
                                alta_dni = input("DNI ")
                                alta_nombre = input("Nombre ")
                                alta_apellidos = input("Apellidos ")
                                alta_email = input("Email ")
                                alta_tarjeta = input("Tarjeta de crédito ")

                                while True:
                                    alta_tipo_abono = int(input("Seleccione el tipo de abono:\n1- Mensual (25€)\n2- Trimestral (70€)\n"
                                                                "3- Semestral (130€)\n4- Anual (200€)\n"))
                                    if alta_tipo_abono == 1:
                                        tipo_abono = "mensual"
                                        break
                                    elif alta_tipo_abono == 2:
                                        tipo_abono = "trimestral"
                                        break
                                    elif alta_tipo_abono == 3:
                                        tipo_abono = "semestral"
                                        break
                                    elif alta_tipo_abono == 4:
                                        tipo_abono = "anual"
                                        break
                                    else:
                                        print("Opción incorrecta\n")

                                while True:
                                    alta_tipo_plaza = int(input("Seleccione el tipo de plaza:\n1- Coche\n2- Moto\n"
                                                                "3- Movilidad reducida "))
                                    if alta_tipo_plaza == 1:
                                        tipo_plaza = "coche"
                                        break
                                    elif alta_tipo_plaza == 2:
                                        tipo_plaza = "moto"
                                        break
                                    elif alta_tipo_plaza == 3:
                                        tipo_plaza = "minusvalido"
                                        break
                                    else:
                                        print("Opción incorrecta\n")

                                servicio_cliente_abonado.dar_alta_abonado(id, alta_matricula, alta_dni, alta_nombre, alta_apellidos, alta_email,
                                                                          alta_tarjeta, tipo_abono, tipo_plaza, repositorio_cliente_abonado,
                                                                          repositorio_abono, servicio_parking, repositorio_vehiculo)

                            elif abonos_opciones == 2:
                                while True:
                                    modificar_abono = int(input("Opciones de modificación: \n1- Modificar datos personales abonado"
                                                                "\n2- Cambiar fecha de cancelación\n0- Salir\n"))
                                    if modificar_abono == 1:
                                        print("Introduzca los siguientes datos:")
                                        dni = input("DNI del abonado a modificar ")
                                        dni_nuevo = input("Nuevo DNI ")
                                        nombre = input("Nombre cliente ")
                                        apellidos = input("Apellidos cliente ")
                                        tarjeta = input("Tarjeta de crédito ")
                                        email = input("Email ")

                                        servicio_cliente_abonado.modificar_datos_abonado(dni, dni_nuevo, nombre, apellidos,
                                                                                         tarjeta, email, repositorio_cliente_abonado)
                                        break
                                    elif modificar_abono == 2:
                                        dni_renovar = input("DNI del abono a renobar ")
                                        servicio_cliente_abonado.modificar_abono(dni_renovar, repositorio_abono)
                                        break
                                    elif modificar_abono == 0:
                                        print("Volviendo..\n")
                                        break
                                    else:
                                        print("Opción incorrecta\n")

                            elif abonos_opciones == 3:
                                dni_cliente_baja = input("Introduzca el DNI del cliente a dar de baja ")
                                servicio_cliente_abonado.baja_abono(dni_cliente_baja, repositorio_abono, repositorio_cliente_abonado,
                                                                    repositorio_facturacion, repositorio_vehiculo)
                            elif abonos_opciones == 0:
                                print("Saliendo..")
                            else:
                                print("Opción incorrecta\n")

                        elif opcion_admin == 5:
                            while True:
                                caducidad_opciones = int(input("Opciones de caducidad:\n1- Caducidad mes\n2- Caducidad próximos 10 días\n0- Salir\n"))
                                if caducidad_opciones == 1:
                                    mes_caducidad = int(input("Introduzca el mes (número) "))
                                    print()
                                    servicio_abono.caducidad_abono_mes(repositorio_abono, mes_caducidad)
                                    break
                                elif caducidad_opciones == 2:
                                    print("En los próximos 10 días:")
                                    servicio_abono.caducidad_proximos_10_dias_timedelta(repositorio_abono)
                                    break
                                elif caducidad_opciones == 0:
                                    print("Saliendo..")
                                    break
                                else:
                                    print("Opción incorrecta\n")
                        elif opcion_admin == 6:
                            print("Matrículas de los últimos 3 vehículos ingresados en el parking:")
                            repositorio_imagen.leer_imagen()
                            #repositorio_imagen.leer_imagen2()

                        elif opcion_admin == 0:
                            print("Saliendo..\n")
                            break
                        else:
                            print("Opción incorrecta\n")
                    except ValueError:
                        print("Introduzca un valor numérico\n")

            else:
                print("Datos incorrectos\n")


        elif opcion == 0:
            usuario = input("Introduzca administrador:\n")
            password = input("Introduzca contraseña administrador:\n")
            cerrar_sesion = repositorio_admin.buscar_admin(usuario, password)

            if(cerrar_sesion!=None):
                print("Cerrando..")
                break
            else:
                print("Administrador incorrecto\n")
        else:
            print("Opción incorrecta\n")
    except ValueError:
        print("Introduzca un valor numérico\n")



