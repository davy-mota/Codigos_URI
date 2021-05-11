import math

value = input().split(sep=' ')

vet = []

for i in value:
    vet.append(int(i))

A = vet[0]
B = vet[1]
C = vet[2]

MaiorAB = int((A + B + abs(A - B)) / 2)
MaiorAB = int((MaiorAB + C + abs(MaiorAB - C)) / 2)

print("{} eh o maior".format(MaiorAB))
