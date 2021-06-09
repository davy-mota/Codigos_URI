A = str(input()).split(sep=' ')
lista = []
listaC = []

for i in A:
    lista.append(int(i))
    listaC.append(int(i))

listaC.sort()
print(listaC[0])
print(listaC[1])
print(listaC[2])
print(lista[0])
print(lista[1])
print(lista[2])