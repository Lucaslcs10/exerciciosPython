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
