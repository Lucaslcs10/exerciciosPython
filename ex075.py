nove = pc = p = 0
n1 = n2 = n3 = n4 = 10
while n1 not in range(0, 10):
    n1 = int(input('De 0 a 9 digite o 1º valor : '))
while n2 not in range(0, 10):
    n2 = int(input('De 0 a 9 digite o 2º valor: '))
while n3 not in range(0, 10):
    n3 = int(input('De 0 a 9 digite o 3º valor: '))
while n4 not in range(0, 10):
    n4 = int(input('De 0 a 9 digite o último valor: '))
tu = (n1, n2, n3, n4)
for c in tu:
    if c == 9:
        nove = nove + 1
print(f'Você digitou os valores {tu}')
if 9 not in tu:
    print('O valor 9 não foi digitado!')
elif nove == 1:
    print(f'O valor 9 aparece {nove} vez!')
else:
    print(f'O valor 9 aparece {nove} vezes!')
if 3 in tu:
    print(f'O valor 3 aparece na {tu.index(3) + 1}ª posição!')
else:
    print('O valor 3 não foi digitado!')
print('Os valores pares são:', end=' ')
for p in tu:
    if p % 2 == 0:
        pc = pc + 1
        print(f'{p} ', end='')
if pc == 0:
    print('Nenhum valor PAR foi digitado!')
