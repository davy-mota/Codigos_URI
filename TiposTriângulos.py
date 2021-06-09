entrada = str(input()).split(sep=' ')
vet = []


for i in entrada:
    vet.append(float(i))

vet.sort(reverse=(True))

A = vet[0]
B = vet[1]
C = vet[2]

print(A)
print(B)
print(C)

if A >= B+C:
    print("NAO FORMA TRIANGULO")
else:
    if A*A == B*B + C*C:
        print("TRIANGULO RETANGULO")
    if A*A > B*B + C*C:
        print("TRIANGULO OBTUSANGULO")
    if A*A < B*B + C*C:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B != C or B == C != A or A == C != B:
        print('TRIANGULO ISOSCELES')
