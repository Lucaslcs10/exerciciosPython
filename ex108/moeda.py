def aumentar(valor=0, taxa=0):
    res = valor + (valor * taxa/100)
    return res


def diminuir(valor=0, taxa=0):
    res = valor - (valor * taxa/100)
    return res


def metade(valor=0):
    res = valor / 2
    return res


def dobro(valor=0):
    res = valor * 2
    return res


def moeda(valor=0, moedas='R$'):
    return f'{moedas}{valor:.2f}'.replace('.',',')
