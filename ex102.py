#  Função para Fatorial


def fatorial(n, show=False):
    """
    ->Calcula o fatorial do número digitado pelo usuário.
    :param n: Número digitado pelo usuário.
    :param show: Da a opção ao usuário de mostrar ou não o cálculo.
    :return: O valor fatorial de N.
    """
    f = conta = 1
    while conta != 'S' and conta != 'N':
        conta = input('Mostrar o cálculo? [S/N] ').strip().upper().replace(' ', '')
    if conta == 'S':
        show = True
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f = f * c
    return f


#  programa principal
print(fatorial(int(input('Digite um número: '))))
#  help(fatorial)
