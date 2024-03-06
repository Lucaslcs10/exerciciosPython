#  Função que descobre o maior
from random import sample, randint
from time import sleep


def maior(*num):  # número de argumentos
    for v in num:
        if (len(v) * 2) < 18:  # ajuste de '-' com len de lista
            print('-' * 22)
        else:
            print('-' * (len(v) * 3))
        print('Analisando os valores:')
        print(f'{v}')  # mostra lista de números gerados
        sleep(3)
        print(f'Valores gerados: {len(v)}')  # mostra quantidade de números gerados
        print(f'Maior valor gerado: {max(v)}')  # mostra maior valor gerado


#  programa principal
# números que podem ser sorteados, quantos números podem ser sorteados
maior(sample(range(0, 9), (randint(1, 9))))
maior(sample(range(0, 9), (randint(1, 9))))
maior(sample(range(0, 9), (randint(1, 9))))
