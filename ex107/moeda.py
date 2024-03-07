def aumentar(valor, taxa):
    res = valor + (valor * taxa/100)
    return round(res, 2)


def diminuir(valor, taxa):
    res = valor - (valor * taxa/100)
    return round(res, 2)


def metade(valor):
    res = valor / 2
    return round(res, 2)


def dobro(valor):
    res = valor * 2
    return round(res, 2)
