# EXERCÍCIO 01
pilha = []
# carregando dados na pilha
for i in range(10):
    flag = True
    while flag:
        dado = input('Digite um número: ')
        flag = False if dado.isnumeric() else True      # verificação da entrada
    pilha.append(float(dado))                           # transformação em real
print('Estado da pilha:', pilha)
# remoção da pilha
for i in range(10):
    print('Dado removido:', pilha[-1])
    pilha.pop()
    print('Estado da pilha:', pilha)
print('Pilha vazia: ', len(pilha) == 0, pilha)
