fazul = '\033[30:44m'
fbranco = '\033[7m'
fverde = '\033[30:42m'
fnormal = '\033[m'
fvermelho = '\033[41m'
#  Sistema interativo de ajuda em Python


def ih(fb):
    """

    :param fb: Recebe a função ou biblioteca desejada.
    :return: Mostra o manual da função ou biblioteca(fb)
    """
    while fb != 'sair':
        print(f'{fazul}-' * (35+(len(fb))))
        print(f'Acessando o manual do comando: {fb}'.center(35+(len(fb))))
        print(f'-' * (35 + (len(fb))))
        print(fnormal+fbranco, end='')
        help(fb)
        print(fnormal+fverde, end='')
        print(f'-' * 30)
        print(f'SISTEMA DE AJUDA PyHELP'.center(30))
        print(f'{fverde}-' * 30)
        print(fnormal, end='')
        fb = str(input('Função ou Biblioteca > ')).lower().replace(' ', '')
    print(f'{fvermelho}-' * 15)
    print(f'ATÉ LOGO'.center(15))
    print(f'{fvermelho}-' * 15)


ih(str(input('Função ou Biblioteca > ')).lower().replace(' ', ''))
#dd