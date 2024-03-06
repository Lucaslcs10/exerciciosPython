print('Analisando Triângulos v2.0')
r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível criar um triângulo!')
    if r1 == r2 == r3:
        print(f'Esse é um triângulo equilátero! (todos os lados iguais)')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print(f'Esse é um triângulo isósceles! (dois lados iguais)')
    elif r1 != r2 != r3 != r1:
        print(f'Esse é um triângulo escaleno! (todos os lados diferentes)')
else:
    print('Não é possível criar um triângulo!')
