from random import choice
lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
menor = maior = ''
print('Números sorteados: ', end='')
for r in range(5):
    n = (choice(lista))
    print(n, end=' ')
    if menor == '':
        menor = maior = n
    if menor > n:
        menor = n
    if maior < n:
        maior = n
print(f'\nO menor número: {menor}')

print(f'O maior número: {maior}')


