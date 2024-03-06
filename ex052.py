#  Números primos
verde = '\033[32m'
vermelho = '\033[31m'
normal = '\033[m'
total = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print(verde, end=' ')
        total = total + 1
    else:
        print(vermelho, end=' ')
    print(c, end=' ')
if total == 2:
    print(f'{normal}\nO número {num} foi divisível {total} vezes!')
    print('Ele é um número primo!')
else:
    print(f'\n{normal}O número {num} foi divisível {total} vezes!')
    print('Ele não é um número primo!')
