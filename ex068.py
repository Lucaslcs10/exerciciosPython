from random import randint
#  Jogo do Par ou Ímpar
print('=-='*4)
print('PAR OU ÍMPAR')
print('=-='*4)
cv = resultado = s = 0
e = ' '
while True:
    n = int(input('Digite um valor: '))
    while e != 'P' and e != 'I':
        e = input('PAR OU ÍMPAR [P/I] ').upper().replace(' ', '')
    PI = 0
    pc = randint(1, 10)
    s = n + pc
    if s % 2 == 0:
        PI = 'PAR'
    if s % 2 == 1:
        PI = 'ÍMPAR'
    if e == 'P' and PI == 'PAR':
        print('=-=' * 18)
        print(f'Você jogou {n} e o Computador {pc}. Total de {s} deu {PI}!')
        print('Você ganhou! Vamos jogar novamente...')
        print('=-=' * 18)
        cv = cv + 1
    if e == 'I' and PI == 'ÍMPAR':
        print('=-=' * 18)
        print(f'Você jogou {n} e o Computador {pc}. Total de {s}. deu {PI}!')
        print('Você ganhou! Vamos jogar novamente...')
        print('=-=' * 18)
        cv = cv + 1
    if e == 'P' and PI == 'ÍMPAR':
        print('=-=' * 18)
        print(f'Você jogou {n} e o Computador {pc}. Total de {s}. deu {PI}!')
        print(f'Você perdeu! Você venceu {cv} vezes!')
        print('=-=' * 18)
        break
    if e == 'I' and PI == 'PAR':
        print('=-=' * 18)
        print(f'Você jogou {n} e o Computador {pc}. Total de {s}. deu {PI}!')
        print(f'Você perdeu! Você venceu {cv} vezes!')
        print('=-=' * 18)
        break
    e = ' '
    pc = ' '
print('JOGO FINALIZADO!')
input("Pressione Enter para sair.")
