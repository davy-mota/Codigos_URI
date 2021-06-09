A = input().split(sep=' ')
vet = []

for i in A:
    vet.append(float(i))

n1 = float(vet[0])
n2 = float(vet[1])
n3 = float(vet[2])
n4 = float(vet[3])

n1 = n1*2
n2 = n2*3
n3 = n3*4
n4 = n4*1

media = (n1+n2+n3+n4)/10

print('Media: {:.1f}'.format(media))

if media >= 7:
    print('Aluno aprovado')
elif media < 5:
    print('Aluno reprovado')
elif media >= 5 and media < 6.9:
    print('Aluno em exame')
    exame = float(input())
    print('Nota do exame {}'.format(exame))
    media = (exame + media)/2
    if media >= 5:
        print('Aluno aprovado')
        print('Media final: {:.1f}'.format(media))




