from random import sample
from time import sleep
#  Palpites para a Mega Sena
n = list(range(1, 61))
print('*' * 30)
print(f'{'MEGA SENA':-^30}')
print('*' * 30)
j = int(input('Quantos jogos você quer sortear? '))
print(f'Sorteando {j} jogos!'.upper())
for s in range(1, j+1):
    print(f'{s}ª Jogo: {sorted(sample(n, 6))}')
    sleep(1)
