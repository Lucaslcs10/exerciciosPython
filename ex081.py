#  Extraindo dados de uma Lista
lista = []
n = lista.append(int(input('Digite um valor: ')))
print('Valor adicionado')
contador = 1
while True:
    c = ' '
    while c != 'S' and c != 'N':
        c = input('Deseja continuar? [S/N] ').upper().strip()
    if c == 'S':
        n = (int(input('Digite um valor: ')))
        lista.append(n)
        print('Valor adicionado!')
        lista.sort(reverse=True)
        contador = contador + 1
    else:
        break
if contador == 1:
    print(f'Você digitou apenas 1 valor!')
else:
    print(f'Você digitou {contador} valores!')
print(f'Valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 FOI encontrado na lista!')
else:
    print('O valor 5 NÃO FOI encontrado na lista!')
