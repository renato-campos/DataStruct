# Exercício 2
while True:
    try:
        decimal = int(input('Digite um número inteiro: '))
    except:
        print('ERRO!!! Tente novamente!')
        continue
    else:
        break
const_bin = []
conferencia = decimal
# conversão para binário - empilhando
while True:
    const_bin.insert(0, decimal % 2)
    decimal //= 2
    if decimal == 1:
        const_bin.insert(0, 1)
        break
# desempilhando
binario = ''
for b in const_bin:
    binario += str(b)

print(f'O decimal {conferencia} em binário fica', binario)
print(bin(conferencia))