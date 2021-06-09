Astr = input()
A = int(float(Astr))
Bstr = input()
B = int(float(Bstr))
Cstr = input()
C = int(float(Cstr))
Dstr = input()
D = int(float(Dstr))

if B>C and D>A and C+D>A+B and C%2==0 and D%2==0 and A%2==0:
    print("Valores aceitos")

else:
    print("Valores não aceitos")