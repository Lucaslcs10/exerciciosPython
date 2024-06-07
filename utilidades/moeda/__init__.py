def aumentar(valor=0, taxa=0, form=False):
    """
    ->Calcula valores e taxas, retornando-os formatados ou não.
    :param valor: Recebe (num) como (valor).
    :param taxa: Recebe (taxa) como (taxa).
    :param form: Formata ou não os resultados.
    :return: Retorna o cálculo em (res).
    """
    res = valor + (valor * taxa / 100)
    if form:
        return moeda(res)
    else:
        return res


def diminuir(valor=float(0), taxa=float(0), form=False):
    res = (valor - (valor * taxa / 100))
    if form:
        return moeda(res)
    else:
        return res


def metade(valor=0, form=False):
    res = valor / 2
    if form:
        return moeda(res)
    else:
        return res


def dobro(valor=0, form=False):
    res = valor * 2
    if form:
        return moeda(res)
    else:
        return res


def moeda(valor=float(0), moedas='R$'):
    """
    -> Formata o resultado dos valores(moedas).
    :param valor: Valor a ser formatado.
    :param moedas: Moeda a ser definada. 'R$' por padrão
    :return: Retorna a (moedas) do (valor) em duas casas decimais e troca '.' por ','.
    """
    return f'{moedas}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, aum=0, dim=0):
    print(f'='*30)
    print('RESUMO'.center(30, '-'))
    print(f'=' * 30)
    print(f'  Preço analisado: \t{moeda(valor)}')
    print(f'  Dobro do preço: \t{dobro(valor, True)}')
    print(f'  Metade do preço: \t{metade(valor, True)}')
    print(f'  {aum}% de aumento: \t{aumentar(valor, aum, True)}')
    print(f'  {dim}% de redução: \t{diminuir(valor, dim, True)}')
    print(f'=' * 30)
