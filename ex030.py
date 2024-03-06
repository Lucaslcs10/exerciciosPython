print('Par ou Ímpar?')
n = int(input('Digite um número: '))
rn = n % 2
if rn == 1:
    print(f'{n} é um número ímpar!')
else:
    print(f'{n} é um número par!')
