fila1 = []
# inserindo
fila1.append(1)
fila1.append(2)
fila1.append(3)
fila1.append(4)
fila1.append(5)
# imprimindo a fila
for i in fila1:
    print(i, end=" -> ")
print('\b\b\b')
# removendo
print(fila1.pop(0))
print(fila1.pop(0))
# imprimindo o que sobrou
for i in fila1:
    print(i, end=" -> ")
print("\b\b\b")
# inserindo
fila1.append(6)
fila1.append(7)
# imprimindo a fila atual
for i in fila1:
    print(i, end=" -> ")
print("\b\b\b")
