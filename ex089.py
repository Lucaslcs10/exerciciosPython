#   Boletim com listas compostas
from time import sleep
alunos = []
dalunos = [[], [], []]
notas = 20132
while True:
    dalunos[0] = input('Nome: ').split()[0].title().replace(' ', '')
    dalunos[1] = float(input('1ª Nota: '))
    dalunos[2] = float(input('2ª Nota: '))
    c = ''
    alunos.append(dalunos[:])
    while c != 'S' and c != 'N':
        c = input('Continuar? [S/N] ').upper().replace(' ', '')
    if c == 'N':
        break
print('*' * 30)
print('Nº|NOME................|MÉDIA|')
print('-' * 30)
for a in range(len(alunos)):
    print(f'{a + 1}.|{alunos[a][0]:.<20}|{(alunos[a][1] + alunos[a][2]) / 2:^5.1f}|')
while True:
    if notas == 20132:
        notas = int(input('Deseja ver as notas de qual aluno? [999 para sair] ')) - 1
        if notas in range(0, len(alunos)):
            print('- ' * 20)
            print(f'As notas de {alunos[notas][0]} foram: [{alunos[notas][1]:.1f} e {alunos[notas][2]:.1f}]')
            print('- ' * 20)
        while notas not in range(0, len(alunos)) and notas != 998:
            print('Opção inválida!')
            notas = int(input('Deseja ver as notas de qual aluno? [999 para sair] ')) - 1
    if notas == 998:
        for ca in 'Finalizando... Volte sempre!':
            print(ca, end='')
            sleep(0.15)
        break
    notas = 20132
