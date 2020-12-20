import pickle

class ticket_repository():

    def __init__(self, lista_ticket=[]):
        self.__lista_ticket = lista_ticket

    @property
    def lista_ticket(self):
        return self.__lista_ticket

    @lista_ticket.setter
    def lista_ticket(self, lista_ticket):
        self.__lista_ticket = lista_ticket

    def __str__(self):
        for i in self.lista_ticket:
            print(i)
        return ""

    def add_ticket(self, ticket):
        self.lista_ticket.append(ticket)
        pickle_ticket = open("./DataBase/ticket", "wb")
        pickle.dump(self.lista_ticket, pickle_ticket)
        pickle_ticket.close()
