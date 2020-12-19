import pickle

class abono_repository():

    def __init__(self, lista_abonos=[]): #= open("./DataBase/abono", "rb")
        self.__lista_abonos = lista_abonos

    @property
    def lista_abonos(self):
        return self.__lista_abonos

    @lista_abonos.setter
    def lista_abonos(self, lista_abonos):
        self.__lista_abonos = lista_abonos

    def __str__(self):
        for i in self.lista_abonos:
            print(i)
        return ""

    def add_abono(self, abono):
        self.lista_abonos.append(abono)
        pickle_abono = open("./DataBase/abono", "wb")
        pickle.dump(self.lista_abonos, pickle_abono)
        pickle_abono.close()

    def buscar_abono(self, dni):
        for i in self.lista_abonos:
            if(i.cliente.dni == dni):
                return i
        return None

    def borrar_abono(self, dni):
        abono = self.buscar_abono(dni)
        if( abono != None):
            self.lista_abonos.remove(abono)
            pickle_abono = open("./DataBase/abono", "wb")
            pickle.dump(self.lista_abonos, pickle_abono)
            pickle_abono.close()
            return True
        return False


 #self.lista_abonos.close()
        #datos_abono = open('./DataBase/abono','r')
            #pickle.load(open("./DataBase/abono", "r"))
        #datos2 = pickle.load(self.lista_abonos)
        #lista = datos_abono.readlines()
        #print(datos_abono)
        #lista_datos = pickle.load(self.lista_abonos)



        #with open('./DataBase/abono', mode='rb') as f:
        #    bytes = f.read()
         #   texto = bytes.decode('utf-8', 'ignore')

#        for i in texto:
#
 #           if(b'(i.cliente.dni)'.decode("utf-8") == dni):
            #if(i.cliente.dni == dni):
  #              print("entrar")
                #str(b'hello',"utf-8")
                #datos_abono.close()
   #             b"abcde".decode("utf-8")
    #            self.lista_abonos = open("./DataBase/abono", "r")
     #           return i
      #  return None
#print()
    #    with open("./DataBase/abono", "rb") as f:
     #       unpickled_obj = pickle.load(f)

      #  print(unpickled_obj)
       # print("holi")
        #if(str(unpickled_obj.cliente.dni) == dni):
         #   print("entrando")
          #  print(dni, "hola")
          #  return unpickled_obj
      #  print("fin")
      #  return None
