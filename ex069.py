#  Análise de dados do grupo
print('-'*19)
print('CADASTRO DE USUÁRIO')
print('-'*19)
c = ' '
s = ' '
tm = qh = qm = 0
while True:
    i = int(input('Idade: '))
    while s != 'M' and s != 'F':
        s = input('SEXO: [M/F] ').upper().replace(' ', '')
    while c != 'S' and c != 'N':
        c = input('Continuar? [S/N] ').upper().replace(' ', '')
    if i >= 18:
        tm = tm + 1
    if s == 'M':
        qh = qh + 1
    if i < 20 and s == 'F':
        qm = qm + 1
    if c == 'N':
        break
    print('-' * 19)
    print('CADASTRO DE USUÁRIO')
    print('-' * 19)
    s = c = ' '
print(f'Total de usuários com mais de 18 anos: {tm}')
print(f'Quantidade de homens cadastrados: {qh}')
print(f'Quantidade de mulheres cadastradas com menos de 20 anos: {qm}')
