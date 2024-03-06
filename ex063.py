#  Sequência de Fibonacci v1.0
n = int(input('Quantidade de termos: '))
t1 = 0
t2 = 1
contador = 2
print(f'{t1} → {t2} → ', end='')
while contador != n:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    contador = contador + 1
    t1 = t2
    t2 = t3
print('FIM')
