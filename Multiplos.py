A = str(input()).split(sep=' ')
vet = []


for i in A:
    vet.append(int(i))

valorA = vet[0]
valorB = vet[1]

if valorA > valorB:
    if valorA % valorB == 0:
        print("Sao Multiplos")
    else:
        print('Nao sao Multiplos')
elif valorA < valorB:
    if valorB % valorA == 0:
        print("Sao Multiplos")
    else:
        print('Nao sao Multiplos')
elif valorA == valorB:
    print('Sao Multiplos')




