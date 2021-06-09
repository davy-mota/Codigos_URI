tipoUm = input()
tipoDois = input()
tipoTres = input()

if tipoUm == 'vertebrado':
    if tipoDois == 'ave':
        if tipoTres == 'carnivoro':
            print('aguia')
        elif tipoTres == 'onivoro':
            print('pomba')

if tipoUm == 'vertebrado':
    if tipoDois == 'mamifero':
        if tipoTres == 'onivoro':
            print('homem')
        elif tipoTres == 'herbivoro':
            print('vaca')

if tipoUm == 'invertebrado':
    if tipoDois == 'inseto':
        if tipoTres == 'hematofago':
            print('pulga')
        elif tipoTres == 'herbivoro':
            print('lagarta')

if tipoUm == 'invertebrado':
    if tipoDois == 'anelideo':
        if tipoTres == 'hematofago':
            print('sanguessuga')
        elif tipoTres == 'onivoro':
            print('minhoca')