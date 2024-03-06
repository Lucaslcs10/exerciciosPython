#  Lista ordenada sem repetições
lista = []
for c in range(0, 5):
    v = (int(input('Digite um valor: ')))
    if c == 0 or v > lista[-1]:
        lista.append(v)
        print('Valor adicionado na última posição')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                break
            pos = pos + 1
print(lista)
