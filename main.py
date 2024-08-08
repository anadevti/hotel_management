from datetime import datetime

class Quarto:
    def __init__(self, numero, tipo, ocupado=False):
        self.numero = numero
        self.tipo = tipo
        self.ocupado = ocupado

    def reservar_quarto(self):
        self.ocupado = True
        print(f"Quarto {self.numero} reservado com sucesso!")

    def desocupar_quarto(self):
        self.ocupado = False
        print(f"Quarto {self.numero} desocupado com sucesso!")


class Cliente:
    def __init__(self, nome, cpf, data_checkIn, data_checkOut):
        self.__nome = nome
        self.__cpf = cpf
        self._data_checkIn = data_checkIn
        self._data_checkOut = data_checkOut

    def realizar_checkIn(self):
        if self._data_checkIn == None:
            self._data_checkIn = datetime.now()
        print(f"Check-in realizado com sucesso para o cliente {self.__nome}!")

    def realizar_checkOut(self):
        if self._data_checkOut == None:
            self._data_checkOut = datetime.now()
        print(f"Check-out realizado com sucesso para o cliente {self.__nome}!")

    def calculo_diarias(self):
        if self._data_checkIn != None and self._data_checkOut != None:
            diarias = self._data_checkOut - self._data_checkIn
            return diarias.days


class Hotel:
    def __init__(self, lista_quartos, lista_clientes):
        self.__lista_quartos = lista_quartos
        self.__lista_clientes = lista_clientes

    def adicionar_novo_quarto(self, quarto):
        self.__lista_quartos.append(quarto)
        return f"Quarto {quarto.numero} adicionado com sucesso!"

    def listar_quartos_disponiveis(self):
        quartos_disponiveis = [quarto for quarto in self.__lista_quartos if not quarto.ocupado]
        return [f"Quarto {quarto.numero} está disponível!" for quarto in quartos_disponiveis]


cliente1 = Cliente("João", "123.456.789-00", datetime(2024, 5, 20), datetime(2024, 5, 30))
cliente1.realizar_checkIn()
cliente1.realizar_checkOut()
print(cliente1.calculo_diarias())