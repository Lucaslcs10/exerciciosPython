#  Cadastro de Jogador de Futebol
cadastro = {}
gols = []
cadastro['Nome:'] = str(input('Nome do jogador: ')).strip().title().split()[0]
partidas = int(input(f'Quantas partidas {cadastro["Nome:"]} jogou: '))
for p in range(partidas):
    gols.append(int(input(f'Quantos gols {cadastro["Nome:"]} fez na {p + 1}ª partida? ')))
cadastro['Gols:'] = gols[:]
cadastro['Total:'] = sum(gols)
print('* ' * 30)
print(cadastro)
print('* ' * 30)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}')
print('* ' * 30)
print(f'O jogador {cadastro["Nome:"]} fez {sum(gols)} gols em {partidas} partidas!')
for g in range(partidas):
    print(f'    -> Na {g + 1}ª partida:{gols[g]} ')
while True:
    pass
