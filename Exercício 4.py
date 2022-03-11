# Exercício 4
def repetidos():                            # função p/ inclusão dos repetidos
    compactado.append(byte_spc)
    compactado.append(compactar[i])
    compactado.append(contador)


byte_spc = 'RPT'
compactar = [22, 23, 24, 24, 24, 24, 24, 24, 24, 25, 27, 27, 27, 27, 27, 27, 25]
compactado = []
contador = 1
for i in range(len(compactar)):             # tratamento para último dado
    if i == len(compactar) - 1:
        if compactar[i] == compactar[i-1]:
            repetidos()
        else:
            compactado.append(compactar[i])
    elif compactar[i] != compactar[i+1]:    # inclusão só qdo não tiver + repetição
        if contador > 1:                    # qdo houve repetição
            repetidos()
            contador = 1
        else:                               # qdo não houve repetição
            compactado.append(compactar[i])
    else:                                   # contagem das repetições
        contador += 1
print(compactar, compactado, sep='\n')
