lista = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional',
         'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
         'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG)')
print('-'*250)
print('A lista de times do Brasileirão 2024:')
print(lista)
print('-'*250)
print(f'Os 5 primeiros são: {lista[0:5]}')
print('-'*250)
print(f'Os 4 últimos são: {lista[-4:]}')
print('-'*250)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('-'*250)
print(f'O {lista[10]} está na {lista.index('São Paulo') + 1}ª posição')
