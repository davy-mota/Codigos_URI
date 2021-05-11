import math

p1 = str(input()).split(sep=' ')
p2 = str(input()).split(sep=' ')

vet1 = []
vet2 = []

for i in p1:
    vet1.append(float(i))

for i in p2:
    vet2.append(float(i))

x1 = vet1[0]
y1 = vet1[1]
x2 = vet2[0]
y2 = vet2[1]

dist = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print("{:.4f}".format(dist))