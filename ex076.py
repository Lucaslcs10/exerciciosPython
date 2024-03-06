#  Lista de Preços com Tupla
lista = ('Caneta', 1.50,
         'Caderno', 15,
         'Mochila', 60,
         'Estojo', 10,
         'Lápis', 1,
         'Livro', 25,
         'Apontador', 2,
         'Borracha', 2,
         'Garrafa', 10)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}'.upper(), end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
