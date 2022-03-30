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

    def insere_depois(self, anterior, novo_dado):
        no_ant = self.busca(anterior)
        # Cria um novo no com o dado desejado.
        novo_no = No(novo_dado)
        # Faz o próximo do novo no ser o próximo do no anterior.
        novo_no.prox_no = no_ant.prox_no
        # Faz com que o novo no seja o próximo do no anterior.
        no_ant.prox_no = novo_no

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

    def busca(self, valor):
        no_atual = self.__main_no
        while no_atual and no_atual.valor != valor:
            no_atual = no_atual.prox_no
        return no_atual



minha_lista = ListaEncadeada()

for i in range(10):
    minha_lista.inserir('nome' + str(i))

minha_lista.exibir()
print('Removendo nome7')
minha_lista.remover('nome7')

minha_lista.exibir()
print('Inserindo no outro_nome no lugar do nome7')
minha_lista.insere_depois('nome6', 'outro_nome10')

minha_lista.exibir()
