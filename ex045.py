import random
from time import sleep

normal = '\033[m'
amarelo = '\033[33m'
ciano = '\033[36m'
print(f'{amarelo}GAME:{ciano} Pedra Papel e Tesoura{normal}')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Sua escolha: '))
print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOOOURA!')
computador = random.randint(0, 2)
print(computador)
if jogador == 0:  # JOGADOR PEDRA
    if computador == 0:
        print('EMPATE! O computador também jogou PEDRA!')
    elif computador == 1:
        print('PERDEU! O computador jogou PAPEL!')
    elif computador == 2:
        print('GANHOU! O computador jogou TESOURA!')
if jogador == 1:  # JOGADOR PAPEL
    if computador == 0:
        print('GANHOU! O computador jogou PEDRA!')
    elif computador == 1:
        print('EMPATE! O computador também jogou PAPEL!')
    elif computador == 2:
        print('PERDEU! O computador TESOURA!')

if jogador == 2:  # JOGADOR TESOURA
    if computador == 0:
        print('PERDEU! O computador jogou PEDRA!')
    elif computador == 1:
        print('GANHOU! O computador jogou PAPEL!')
    elif jogador == 2 and computador == 2:
        print('EMPATE! O computador também jogou TESOURA!')
else:
    print('OPÇÃO INVÁLIDA!')
