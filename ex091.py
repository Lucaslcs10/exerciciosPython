from random import randint
from time import sleep
#  Jogo de Dados em Python
c = 1
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
ranking = {}
print('* ' * 20)
print(f'{'JOGADAS':-^39}')
for k, v in jogadores.items():
    print(f'{k} - Tirou{v:.>22}')
    sleep(1)
print(f'{'RANKING':-^39}')
ranking = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
for k, v in (ranking.items()):
    print(f'   {c}º Lugar: {k} com {v} pontos!')
    c = c + 1
