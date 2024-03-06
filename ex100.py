from random import sample
from time import sleep
#  Funções para sortear e somar
lista = []


def sortear_valores(valores):  # define a função para sortear valores em [valores]
    print('-' * 31)
    print('Sorteando 5 valores: ')
    for v in valores:  # seleciona um valor em 'valores' como (v)
        print(v, end=' ')  # mostra o valor selecionado(v) sem pular linha
        sleep(1)
        lista.append(v)  # adiciona o valor selecionado(v) a [lista]
    print()


def somar_par(valores):  # define a função para somar os valores em [valores]
    sleep(1)
    print('-' * 31)
    sleep(1)
    print(f'Somando os valores pares temos:')
    sleep(1)
    soma = 0
    for va in valores:  # seleciona um valor em [valores] como (va)
        if va % 2 == 0:  # se o valor selecionado(va) for PAR entra na [lista]
            soma = soma + va  # soma o valor(va) adicionando-o na variável *SOMA*
    print(f'{soma}')
    sleep(1)
    print('-' * 31)
    sleep(1)


# programa principal
# números que podem ser sorteados, quantos números podem ser sorteados
sortear_valores((sample(range(0, 9), 5)))
somar_par(lista)
msg = 'Finalizando...'
for m in msg:
    print(m, end='')
    sleep(0.3)
