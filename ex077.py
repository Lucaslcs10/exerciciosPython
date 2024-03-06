#  Contando vogais em Tupla
lista = ('APRENDER',
         'PROGRAMAR',
         'LINGUAGEM',
         'PYTHON',
         'CURSO',
         'GRATIS',
         'ESTUDAR',
         'PRATICAR',
         'TRABALHAR',
         'MERCADO',
         'PROGRAMADOR',
         'FUTURO',
         )
c = 0
for palavra in lista:
    if c == 0:
        print(f'Na palavra {palavra} temos: ', end='')
    else:
        print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in sorted(palavra.upper()):
        if letra in 'A Á Â Ã Ä E É Ê Ë I Í Î Ï O Ó Ô Õ Ö U Ú Û Ü':
            print(letra, end=' ')
    c = c + 1
