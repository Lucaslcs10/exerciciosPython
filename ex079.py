#  Valores únicos em uma Lista
lista = []
num = lista.append(int(input('Digite um valor: ')))
print('Valor adicionado')
while True:
    c = ' '
    while c != 'S' and c != 'N':
        c = input('Deseja continuar? [S/N] ').upper().strip()
    if c == 'S':
        n = (int(input('Digite um valor: ')))
        if n in lista:
            print('Valor duplicado! Não adicionado!')
        else:
            lista.append(n)
            print('Valor adicionado!')
        lista.sort()
    else:
        break
print(f'Valores digitados {lista}')
