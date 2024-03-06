#  Contagem de pares
n = int(input('Digite um número PAR de 0 a 50: '))
if n <= 50 and n % 2 == 0:
    for c in range(n, 51, 2):
        print(f'{c}', end=" ")
else:
    print('Número inválido!')
print('\nFIM')
