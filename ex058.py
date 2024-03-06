import random
from time import sleep
print('Estou pensando em um número de 0 a 10...')
sleep(1.5)
n = random.randint(0, 1)
p = int(input('Qual número estou pensando? '))
contador = 1
while n != p:
    contador = contador + 1
    if p > n:
        print('Menos... Tente novamente!')
    else:
        print('Mais... Tente novamente!')
    p = int(input('Qual número estou pensando? '))
if contador == 1:
    print('Parabéns! Você acertou de primeira!')
else:
    print(f'Parabéns! Eu estava pensando no número {n}')
    print(f'Você acertou na {contador}ª tentativa!')
