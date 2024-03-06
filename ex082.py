#  Dividindo valores em várias listas
lista = []
listapar = []
listaimpar = []
while True:
    c = ' '
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    print('Valor adicionado')
    while c != 'S' and c != 'N':
        c = input('Deseja continuar? [S/N] ').upper().strip()
    if n % 2 == 0:
        if n not in listapar:
            listapar.append(n) and listapar.sort()
    else:
        if n not in listaimpar:
            listaimpar.append(n) and listaimpar.sort()
    if c == 'S':
        lista.sort()
    else:
        break
print(f'Lista completa: {lista}')
print(f'Lista PAR: {listapar}')
print(f'Lista ÍMPAR: {listaimpar}')
