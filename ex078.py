lista = []
maior = menor = posme = posma = ''
cont = 1
for cont in range(0, 5):
    lista.append(int(input(f'Digite {cont + 1}ª valor: ')))
    if maior == '':
        maior = menor = lista[0]
        posme = posma = 1
    for c, m in enumerate(lista):
        if m > maior:
            maior = m
            posma = c + 1
        if m < menor:
            menor = m
            posme = c + 1
print(f'Você digitou os valores {lista}')
print(f'O maior foi: {maior} na {posma}ª posição!')
print(f'E o menor foi: {menor} na {posme}ª posição!')
