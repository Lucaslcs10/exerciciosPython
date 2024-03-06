#  Progressão Aritmética
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pt + 9 * r
for c in range(pt, termo + r, r):
    print(f'{c} 🠖', end=' ')
print('FIM!')
