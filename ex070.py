#  Estatísticas em produtos
print('='*16)
print('SALDÃO DO LUCÃO')
print('='*16)
c = npmb = ' '
pmc = pmb = s = 0
while True:
    n = input('Nome do produto: ')
    p = float(input('Preço: R$'))
    s = s + p
    c = ' '
    if npmb == ' ' or p < pmb:
        npmb = n
    if pmb == 0 or p < pmb:
        pmb = p
    if p >= 1000:
        pmc = pmc + 1
    while c != 'S' and c != 'N':
        c = input('Continuar? [S/N] ').upper().replace(' ', '')
    if c == 'N':
        break
print('*'*13)
print('FIM DA COMPRA')
print('*'*13)
print(f'O total foi de: R$:{s:.2f}')
print(f'O total de produtos com o preço acima de R$1000 foi: {pmc}')
print(f'O produto mais barato foi: {npmb.title()} por R${pmb:.2f}')
