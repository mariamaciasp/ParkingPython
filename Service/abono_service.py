from datetime import datetime, timedelta
import calendar

class abono_service():

    def caducidad_abono_mes(self, abono_repository, mes_caducidad):
        lista_caducidad_mes = []
        for i in abono_repository.lista_abonos:
            if(i.fecha_cancelacion.month == mes_caducidad):
                lista_caducidad_mes.append(i)
        if(len(lista_caducidad_mes) != 0):
            for i in lista_caducidad_mes:
                print(i)
        else:
            print("No existen abonos con esa fecha de caducidad")

    def caducidad_proximos_10_dias(self, abono_repository):
        lista_10_dias = []
        fecha_actual = datetime.now()
        mes_actual = fecha_actual.month
        dia_actual = fecha_actual.day
        anio_actual = fecha_actual.year
        proximos_10_dias_normal = dia_actual + 10

        if(mes_actual == 12):
            proximo_mes = 1
        else:
            proximo_mes = mes_actual + 1

        for i in abono_repository.lista_abonos:
            mes_abono = i.fecha_cancelacion.month

            if(mes_actual in [4, 6, 9, 11]): # meses con 30 días
                dias_mes_proximo = 10 - (30 -dia_actual)
                if(dia_actual > 20):
                    if((dia_actual <= i.fecha_cancelacion.day <= 30 and mes_actual == mes_abono)
                            or (1 <= i.fecha_cancelacion.day <= dias_mes_proximo and proximo_mes == mes_abono)):
                        lista_10_dias.append(i)

                else:
                    if(dia_actual <= i.fecha_cancelacion.day <= proximos_10_dias_normal and mes_actual == mes_abono):
                        lista_10_dias.append(i)

            if(mes_actual in [1, 3, 5, 7, 8, 10, 12]):
                dias_mes_proximo = 10 - (31 -dia_actual)
                if(dia_actual > 21):
                    if((dia_actual <= i.fecha_cancelacion.day <= 31 and mes_actual == mes_abono)
                            or (1 <= i.fecha_cancelacion.day <= dias_mes_proximo and proximo_mes == mes_abono)):
                        lista_10_dias.append(i)

                else:
                    if(dia_actual <= i.fecha_cancelacion.day <= proximos_10_dias_normal and mes_actual == mes_abono):
                        lista_10_dias.append(i)

            if(mes_actual == 2):
                ultimo_dia_mes_tupla = calendar.monthrange(fecha_actual.year, 2)
                ultimo_dia_mes = ultimo_dia_mes_tupla[1]

                if(mes_actual > i.fecha_cancelacion.month):
                    if(ultimo_dia_mes == 28):
                        dias_mes_proximo = 10 - (28 -dia_actual)
                        if(dia_actual > 18):
                            if((dia_actual <= i.fecha_cancelacion.day <= 28 and mes_actual == mes_abono
                                and i.fecha_cancelacion.year == anio_actual+1)
                                    or (1 <= i.fecha_cancelacion.day <= dias_mes_proximo and proximo_mes == mes_abono
                                        and i.fecha_cancelacion.year == anio_actual)):
                                lista_10_dias.append(i)

                        else:
                            if(dia_actual <= i.fecha_cancelacion.day <= proximos_10_dias_normal and mes_actual == mes_abono
                            and i.fecha_cancelacion.year == anio_actual+1):
                                lista_10_dias.append(i)
                    else:
                        dias_mes_proximo = 10 - (29 -dia_actual)
                        if(dia_actual > 19):
                            if((dia_actual <= i.fecha_cancelacion.day <= 29 and mes_actual == mes_abono
                                and i.fecha_cancelacion.year == anio_actual+1)
                                    or (1 <= i.fecha_cancelacion.day <= dias_mes_proximo and proximo_mes == mes_abono
                                        and i.fecha_cancelacion.year == anio_actual+1)):
                                lista_10_dias.append(i)

                        else:
                            if(dia_actual <= i.fecha_cancelacion.day <= proximos_10_dias_normal and mes_actual == mes_abono
                                    and i.fecha_cancelacion.year == anio_actual+1):
                                lista_10_dias.append(i)
                else:
                    if(ultimo_dia_mes == 28):
                        dias_mes_proximo = 10 - (28 -dia_actual)
                        if(dia_actual > 18):
                            if((dia_actual <= i.fecha_cancelacion.day <= 28 and mes_actual == mes_abono
                                and i.fecha_cancelacion.year == anio_actual)
                                    or (1 <= i.fecha_cancelacion.day <= dias_mes_proximo and proximo_mes == mes_abono)):
                                lista_10_dias.append(i)

                        else:
                            if(dia_actual <= i.fecha_cancelacion.day <= proximos_10_dias_normal and mes_actual == mes_abono
                                    and i.fecha_cancelacion.year == anio_actual):
                                lista_10_dias.append(i)
                    else:
                        dias_mes_proximo = 10 - (29 -dia_actual)
                        if(dia_actual > 19):
                            if((dia_actual <= i.fecha_cancelacion.day <= 29 and mes_actual == mes_abono
                                and i.fecha_cancelacion.year == anio_actual)
                                    or (1 <= i.fecha_cancelacion.day <= dias_mes_proximo and proximo_mes == mes_abono
                                        and i.fecha_cancelacion.year == anio_actual)):
                                lista_10_dias.append(i)

                        else:
                            if(dia_actual <= i.fecha_cancelacion.day <= proximos_10_dias_normal and mes_actual == mes_abono
                                    and i.fecha_cancelacion.year == anio_actual):
                                lista_10_dias.append(i)
            else:
                print("El mes no existe")


        if(len(lista_10_dias) != 0):
            for i in lista_10_dias:
                print(i)
        else:
            print("No existen abonos con esa fecha de caducidad")

    def caducidad_proximos_10_dias_timedelta(self, abono_repository):
        proximos_10_dias = timedelta(days=10)
        lista_caducidad = []
        fecha_actual = datetime.now()
        #fecha_actual = fecha_actual.replace(day=20)
        #fecha_actual = fecha_actual.replace(month=1)
        #fecha_actual = fecha_actual.replace(year=2021)
        final_caducidad = fecha_actual + proximos_10_dias

        for i in abono_repository.lista_abonos:
            if(final_caducidad>=i.fecha_cancelacion>=fecha_actual):
                lista_caducidad.append(i)

        if(len(lista_caducidad) != 0):
            for i in lista_caducidad:
                print(i)
        else:
            print("No existen abonos que caduquen en los próximos 10 días")
