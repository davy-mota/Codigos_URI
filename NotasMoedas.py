#---------------------------Entrada de Dados----------------------------

N = float(input())

#---------------------------Cálculo das Notas------------------------------------

restoCem = N % 100
notaCem = int((N - restoCem)/100)
restoCin = restoCem % 50
notaCin = int((restoCem - restoCin)/50)
restoVin = restoCin % 20
notaVin = int((restoCin - restoVin)/20)
restoDez = restoVin % 10
notaDez = int((restoVin - restoDez)/10)
restoCinco = restoDez % 5
notaCinco = int((restoDez - restoCinco)/5)
restoDois = restoCinco % 2
notaDois = int((restoCinco - restoDois)/2)
restoDois = restoCinco % 2
notaDois = int((restoCinco - restoDois)/2)

#-------------------------Cálculo das Moedas----------------------------------

restoUm = restoDois % 1
restoUm = round(restoUm, 2)
moedaUm = restoDois - restoUm
moedaUm = round(moedaUm, 2)
moedaUm = int(moedaUm / 1)
restoCinquenta = restoUm % 0.5
restoCinquenta = round(restoCinquenta, 2)
moedaCinquenta = restoUm - restoCinquenta
moedaCinquenta = round(moedaCinquenta, 2)
moedaCinquenta = int(moedaCinquenta / 0.5)
restoVinteCinco = restoCinquenta % 0.25
restoVinteCinco = round(restoVinteCinco, 2)
moedaVinteCinco = restoCinquenta - restoVinteCinco
moedaVinteCinco = round(moedaVinteCinco, 2)
moedaVinteCinco = int(moedaVinteCinco / 0.25)
restoDezCentavos = restoVinteCinco % 0.1
restoDezCentavos = round(restoDezCentavos, 2)
moedaDezCentavos = restoVinteCinco - restoDezCentavos
moedaDezCentavos = round(moedaDezCentavos, 2)
moedaDezCentavos = int(moedaDezCentavos / 0.1)
restoCincoCentavos = restoDezCentavos % 0.05
restoCincoCentavos = round(restoCincoCentavos, 2)
moedaCincoCentavos = restoDezCentavos - restoCincoCentavos
moedaCincoCentavos = round(moedaCincoCentavos, 3)
moedaCincoCentavos = int(moedaCincoCentavos / 0.05)
restoUmCentavo = restoCincoCentavos % 0.1
restoUmCentavo = round(restoUmCentavo, 3)
moedaUmCentavo = int(restoCincoCentavos/0.01)

#-------------------------Plotagem de Dados----------------------------

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(notaCem))
print("{} nota(s) de R$ 50.00".format(notaCin))
print("{} nota(s) de R$ 20.00".format(notaVin))
print("{} nota(s) de R$ 10.00".format(notaDez))
print("{} nota(s) de R$ 5.00".format(notaCinco))
print("{} nota(s) de R$ 2.00".format(notaDois))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(moedaUm))
print("{} moeda(s) de R$ 0.50".format(moedaCinquenta))
print("{} moeda(s) de R$ 0.25".format(moedaVinteCinco))
print("{} moeda(s) de R$ 0.10".format(moedaDezCentavos))
print("{} moeda(s) de R$ 0.05".format(moedaCincoCentavos))
print("{} moeda(s) de R$ 0.01".format(moedaUmCentavo))


