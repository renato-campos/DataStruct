# a estrutura com dados
dados = [7, 8, 10, 20, 30, 40, 50, 60, 70, 80]

# impressão como fila
print(f'Ordem dos dados em fila:', end=' ')
for i in dados:
    print(i, end=' ')

# impressão como pilha
print(f'\nOrdem dos dados em pilha:', end=' ')
for j in range(len(dados)-1, -1, -1):
    print(dados[j], end=' ')
