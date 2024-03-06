#  Cálculo do Fatorial
from math import factorial
from time import sleep
n = int(input('Digite um número: '))
contador = n
print(f'Calculando {n}!')
sleep(1.5)
print('...')
sleep(1.5)
print(f'{contador}! = ', end='')
while contador > 0:
    print(f'{contador} ', end='')
    if contador > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    contador = contador - 1
f = factorial(n)
print(f)
