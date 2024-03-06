from random import choice
print('SORTEANDO UM ITEM NA LISTA')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
c = choice(lista)
print(f'Escolhido: {c}!')
