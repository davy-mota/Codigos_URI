import math


date = str(input()).split(sep=' ')
vet = []

for i in date:
    vet.append(float(i))

A = float(vet[0])
B = float(vet[1])
C = float(vet[2])

parte1 = (B*B)-4*A*C

if parte1 <= 0 or A == 0:
    print("Impossivel calcular")

elif A != 0:
    raiz = math.sqrt(parte1)
    x1 = (-B + raiz)/(2*A)
    x2 = (-B - raiz)/(2*A)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))




