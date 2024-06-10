# cores letras
normal = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
branco = '\033[97m'
# cores fundos
fnormal = '\033[m'
fpreto = '\033[40m'
fvermelho = '\033[41m'
fverde = '\033[42m'
famarelo = '\033[43m'
fazul = '\033[44m'
froxo = '\033[45m'
fciano = '\033[46m'
fcinza = '\033[47m'
fbranco = '\033[47m'


def Int(msg):
    """
    -> Checa se um valor(msg) se INTEIRO.
    :param msg: Valor a ser checado.
    :return: Retorna o valor se INTEIRO ou INTERROMPIDO.
    """
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'{vermelho}ERRO: Por favor, digite uma opção {verde}VÁLIDA.{normal}')
            continue
        except KeyboardInterrupt:
            print(f'{vermelho}Entrada não digitada pelo usuário.{normal}')
            continue
        else:
            return i


def linha(tam=40):
    return '_' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{vermelho}{c} {azul}-{normal} {verde}{item}{normal}')
        c = c+1
    print(linha())
    opc = Int(f'{amarelo}Sua Opção: {normal}')
    return opc
