class No:
    def __init__(self, valor, prox_no=None):
        self.__valor = valor
        self.prox_no = prox_no

    @property
    def valor(self):
        return self.__valor


class ListaEncadeada:
    def __init__(self):
        self.__main_no = None

    def inserir(self, valor):
        if self.__main_no is None:
            self.__main_no = No(valor)
            return

        no_atual = self.__main_no
        while no_atual.prox_no is not None:
            no_atual = no_atual.prox_no
        no_atual.prox_no = No(valor)

    def remover(self, valor):
        if self.__main_no is None:
            return

        no_ant = None
        no_atual = self.__main_no

        if no_atual.valor == valor:
            self.__main_no = no_atual.prox_no

        while True:
            no_ant = no_atual
            no_atual = no_atual.prox_no

            if no_atual is None:
                break

            if no_atual.valor == valor:
                no_ant.prox_no = no_atual.prox_no

    def exibir(self):
        valores = []
        no_atual = self.__main_no
        while no_atual is not None:
            valores.append(no_atual.valor)
            no_atual = no_atual.prox_no
        print("Lista Encadeada: {}".format(valores))


minha_lista = ListaEncadeada()

minha_lista.inserir(1)
minha_lista.inserir(2)
minha_lista.inserir(3)
minha_lista.inserir(4)
minha_lista.inserir(5)

minha_lista.exibir()

minha_lista.remover(3)

minha_lista.exibir()

minha_lista.inserir(10)

minha_lista.exibir()
