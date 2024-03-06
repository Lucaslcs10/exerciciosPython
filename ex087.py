#  Mais sobre Matriz em Python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = maior = 0
for l in range(0, 3):  # quantidade de linhas
    for c in range(0, 3):  # quantidade de colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))  # valores para linhas e colunas
        if matriz[l][c] % 2 == 0:  # soma dos valores pares
            soma = soma + matriz[l][c]
        soma3 = soma3 + matriz[l][2]  # soma dos valores da terceira coluna
        if maior == 0:
            maior = matriz[l][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]
print('*' * 27)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
print('*' * 27)
print(f'Soma dos valores pares: {soma}')
print(f'Soma dos valores da 3ª coluna: {soma3}')
print(f'O maior valor da 2ª linha: {maior}')
