vermelho = '\033[31m'
normal = '\033[m'


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
            print(f'{vermelho}ERRO: Por favor, digite um número INTEIRO válido.{normal}')
            continue
        except KeyboardInterrupt:
            print(f'{vermelho}Entrada não digitada pelo usuário.{normal}')
            return 0
        else:
            return i


def Float(msg):
    while True:
        try:
            i = float(input(msg))
        except (ValueError, TypeError):
            print(f'{vermelho}ERRO: Por favor, digite um número REAL válido.{normal}')
            continue
        except KeyboardInterrupt:
            print(f'{vermelho}Entrada não digitada pelo usuário.{normal}')
            return 0
        else:
            return i
