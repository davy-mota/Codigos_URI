renda = float(input())

if renda >= 0 and renda <= 2000:
    print('ISENTO')

elif renda > 2000 and renda <= 3000:
    renda = renda - 2000
    total = renda * 0.08
    print('R$ {:.2f}'.format(total))

elif renda > 3000 and renda <= 4500:
    renda1 = 2000 - 1000
    total = renda1 * 0.08
    renda2 = renda - 3000
    total2 = renda2 * 0.18
    total2 = total + total2
    print('R$ {:.2f}'.format(total2))

elif renda > 4500:
    renda1 = 2000 - 1000
    total = renda1 * 0.08
    renda2 = 3000 - 1500
    total2 = renda2 * 0.18
    renda3 = renda - 4500
    total3 = renda3 * 0.28
    total3 = total + total2 + total3
    print('R$ {:.2f}'.format(total3))