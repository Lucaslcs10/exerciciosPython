#  Lista composta e análise de dados
pessoas = []
dados = []
ml = mp = 0
c = ' '
pml = []
pmp = []
while c != 'N':
    c = ' '
    dados.append(input('Nome: ').strip().title())
    dados.append(float(input('Peso: ')))
    if not ml:
        ml = mp = dados[1]
    else:
        if dados[1] < ml:
            ml = dados[1]
        if dados[1] > mp:
            mp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while c != 'N' and c != 'S':
        c = input('Quer continuar? [S/N] ').upper().replace(' ', '')
for c in pessoas:
    if c[1] == ml:
        pml.append(c[0])
    if c[1] == mp:
        pmp.append(c[0])
print('*' * 30)
print(f'{len(pessoas)} Pessoas foram cadastradas.')
print(f'O maior peso foi de {mp:.1f}Kg de {pmp}.')
print(f'O menor peso foi de {ml:.1f}Kg de {pml}.')
