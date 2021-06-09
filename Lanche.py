A = str(input()).split(sep=' ')
vet = []

for i in A:
    vet.append(int(i))

cod = vet[0]
quant = vet[1]

codstr = str(cod)

prod = {'1': 4.00, '2': 4.50, '3': 5.00, '4': 2.00, '5': 1.50}

total = prod[codstr] * quant
print('Total: R$ {:.2f}'.format(total))