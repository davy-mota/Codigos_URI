N = int(input())

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
restoUm = restoDois % 1
notaUm = int((restoDois - restoUm)/1)




print(N)
print("{} nota(s) de R$ 100,00".format(notaCem))
print("{} nota(s) de R$ 50,00".format(notaCin))
print("{} nota(s) de R$ 20,00".format(notaVin))
print("{} nota(s) de R$ 10,00".format(notaDez))
print("{} nota(s) de R$ 5,00".format(notaCinco))
print("{} nota(s) de R$ 2,00".format(notaDois))
print("{} nota(s) de R$ 1,00".format(notaUm))



