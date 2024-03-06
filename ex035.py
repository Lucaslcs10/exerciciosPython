print('Analisando Triângulo v1.0')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print(f'É possível criar um triângulo!')
else:
    print('Não é possível criar um triângulo!')
print(' ')
print('Fim')
