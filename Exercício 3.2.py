# variáveis
dados = []
maior = soma = menor = 0
# entrada dos dados
for i in range(5):
    while True:
        try:
            dados.append(int(input(f'Digite o valor de índice {i}: ')))
        except:
            continue
        else:
            break
    print('Dado incluído com sucesso.')
# imprimindo a lista e cálculos
print('Lista completa: ', end=' ')
for i in range(len(dados)):
    print(dados[i], end=' ')
    if i == 0:
        maior = dados[i]
        menor = dados[i]
        soma += dados[i]
    else:
        if dados[i] > maior:
            maior = dados[i]
        if dados[i] < menor:
            menor = dados[i]
        soma += dados[i]
# exibindo resultados
print(f'''\nMaior valor digitado foi o {maior}
Menor valor foi o {menor}
A média é de {soma/5:.2f}''')
