salary = float(input())

if salary >=0 and salary <= 400:
    x = salary * 0.15
    newSalary = x + salary
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual: 15 %')

if salary >=400.01 and salary <= 800:
    x = salary * 0.12
    newSalary = x + salary
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual: 12 %')

if salary >=800.01 and salary <= 1200:
    x = salary * 0.10
    newSalary = x + salary
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual: 10 %')

if salary >=1200.01 and salary <= 2000:
    x = salary * 0.07
    newSalary = x + salary
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual: 7 %')

if salary > 2000:
    x = salary * 0.04
    newSalary = x + salary
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(x))
    print('Em percentual: 4 %')

