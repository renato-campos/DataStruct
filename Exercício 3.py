# Exercício 3
pilha1 = [1, 2, 1, 3, 2, 4, 1, 7, 7, 3]
pilha2 = []
for valor in pilha1:
    if valor not in pilha2:
        pilha2.append(valor)
print(pilha1, pilha2, sep='\n')
