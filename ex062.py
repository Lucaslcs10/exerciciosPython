#  Super Progressão Aritmética v3.0
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
prog = t1
contador = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais  # total = 10
    while contador <= total - 1:
        print(f'{prog}', '→ ', end='')
        prog = prog + r
        contador = contador + 1
    print(f'PAUSA!')
    mais = int(input('Quantos termos a mais? '))
print(f'Finalizado! {total} termos usados.')
