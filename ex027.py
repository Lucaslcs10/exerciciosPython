print('Primeiro e último nome de uma pessoa')
nome = input('Digite seu nome completo: ').strip().title().split()
print('Olá! Prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}!')
print(f'E seu último nome é {nome[-1]}!')
