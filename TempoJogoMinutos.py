vet = []
totalHora = int()
totalMinutos = int()

A = str(input()).split(sep=' ')

for i in A:
    vet.append(int(i))

horaInicial = vet[0]
minutoInicial = vet[1]
horaFinal = vet[2]
minutoFinal = vet[3]

if horaInicial == 0 and horaFinal == 0 and minutoInicial < minutoFinal:
    totalHora = 0
    totalMinutos = minutoFinal - minutoInicial

elif horaInicial == 0 and horaFinal == 0 and minutoInicial > minutoFinal:
    totalHora = 24
    totalMinutos = (60 - minutoInicial) + minutoFinal
    totalHora = totalHora - 1

elif horaInicial == 0 and horaFinal == 0 and minutoInicial == minutoFinal:
    totalHora = 24
    totalMinutos = 0

elif horaInicial == horaFinal and minutoInicial == minutoFinal:
    totalHora = 24
    totalMinutos = 0

elif horaInicial == horaFinal and minutoInicial > minutoFinal:
    totalHora = 24
    totalMinutos = (60 - minutoInicial) + minutoFinal
    totalHora = totalHora - 1

elif horaInicial == horaFinal and minutoInicial < minutoFinal:
    totalHora = 0
    totalMinutos = minutoFinal - minutoInicial

elif horaInicial < horaFinal and minutoInicial > minutoFinal:
    totalHora = horaFinal - horaInicial
    totalMinutos = (60 - minutoInicial) + minutoFinal
    totalHora = totalHora - 1

elif horaInicial < horaFinal and minutoInicial < minutoFinal:
    totalHora = horaFinal - horaInicial
    totalMinutos = minutoFinal - minutoInicial

elif horaInicial > horaFinal and minutoInicial > minutoFinal:
    totalHora = (24 - horaInicial) + horaFinal
    totalMinutos = (60 - minutoInicial) + minutoFinal
    totalHora = totalHora - 1

elif horaInicial > horaFinal and minutoInicial < minutoFinal:
    totalHora = (24 - horaInicial) + horaFinal
    totalMinutos = minutoInicial - minutoFinal

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(totalHora,totalMinutos))




