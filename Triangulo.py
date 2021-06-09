A = str(input()).split(sep=' ')
vet = []


for i in A:
    vet.append(float(i))

A = float(vet[0])
B = float(vet[1])
C = float(vet[2])

modulo1 = B - C
modulo2 = A - C
modulo3 = A - B


if modulo1 < A < B+C and modulo2 < B < A+C and modulo3 < C < A+B:
    P = A + B + C
    print('Perimetro = {:.1f}'.format(P))
else:
    Area = ((A+B)/2)*C
    print('Area = {:.1f}'.format(Area))
