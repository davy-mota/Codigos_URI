A = str(input()).split(sep=' ')
vet = []

for i in A:
    vet.append(float(i))

A = vet[0]
B = vet[1]
C = vet[2]

pi = 3.14159

triangulo = (A*C)/2
circulo = pi*C*C
atum = (A*C)/2
atdois = (B*C)/2
trapezio = atum + atdois
quadrado = B*B
retangulo = A*B

print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))