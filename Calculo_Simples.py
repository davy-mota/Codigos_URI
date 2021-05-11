A = input().split(sep=' ')
B = input().split(sep=' ')
vetB = []
vetA = []

for i in A:
    vetA.append(i)

codA = int(vetA[0])
numA = int(vetA[1])
valorA = float(vetA[2])

for i in B:
    vetB.append(i)

codB = int(vetB[0])
numB = int(vetB[1])
valorB = float(vetB[2])

total = (numA * valorA) + (numB * valorB)

print("VALOR A PAGAR: R$ {:.2f}".format(total))
