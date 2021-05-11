nome = input()
salary = float(input())
vendas = float(input())

comissao = vendas*0.15
total = comissao+salary

print("TOTAL = R$ {:.2F}".format(total))