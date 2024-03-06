#  Progressão Aritmética v2.0
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
prog = t1
contador = 0
while contador != 10:
    if contador < 9:
        print(f'{prog}', '→ ', end='')
    else:
        print(f'{prog}  FIM!')
    prog = prog + r
    contador = contador + 1
