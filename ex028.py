from random import choice
print('Jogo da Adivinhação v.1.0')
nu = int(input('Estou pensando em um número de 0 a 5. Qual número estou pensando? '))
lista = [1, 2, 3, 4, 5]
nc = choice(lista)
if nc == nu:
    print(f'Você acertou! Eu estava pensando no número {nc}!')
else:
    print(f'Você errou! Eu estava pensando no número {nc}!')
print('FIM')
