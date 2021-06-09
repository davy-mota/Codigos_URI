A = str(input()).split(sep=' ')
vet = []


for i in A:
    vet.append(int(i))

horaInicial= vet[0]
horaFinal = vet[1]

if horaInicial == horaFinal:
    print('O JOGO DUROU 24 HORA(S)')
elif horaInicial < horaFinal:
    total = horaFinal - horaInicial
    print('O JOGO DUROU {} HORA(S)'.format(total))
else:
    total = (24 - horaInicial) + horaFinal
    print('O JOGO DUROU {} HORA(S)'.format(total))



