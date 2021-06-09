A = str(input()).split(sep=(' '))
vet = []

for i in A:
    vet.append(float(i))

x = float(vet[0])
y = float(vet[1])

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
elif x > 0 or x < 0 and y == 0:
    print('Eixo X')
elif x == 0 and y > 0 or y < 0:
    print('Eixo Y')
else:
    print('Origem')