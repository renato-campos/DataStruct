# Exercício 5
compactar = [32, 33, 34, 34, 34, 34, 34, 34, 34, 35, 37, 37, 37, 37, 37, 37, 35, 34, 35]
compactado = []
byte_spc = 'RPT'
contador = 1
for valor in compactar:
    contador = compactar.count(valor)
    if valor not in compactado and contador > 1:
        compactado.append(byte_spc)
        compactado.append(valor)
        compactado.append(contador)
        contador = 1
    elif contador == 1:
        compactado.append(valor)
print('Dados compactados:', compactado)
