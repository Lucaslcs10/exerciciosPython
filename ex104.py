#  Validando entrada de dados em Python


def leiaint(a):
    vermelho = '\033[31m'
    normal = '\033[m'
    """
    ->Valida números inteiros.
    :param a: Recebe um número digitado pelo usuário.
    :return: (r) Valida e retorna o número para o usuário.
    """
    r = input(a)  # recebe valor pelo usuário (r)
    while True:  # início de loop
        if not r.isnumeric():  # se (r) não númerico ↓
            print(f'{vermelho}ERRO! Digite um número inteiro válido!{normal}')
            r = input(a)  # recebe valor pelo usuário (r)
        else:  # se (r) númerico ↓
            break  # sai do loop
    return r  # retorna (r) validado


#  programa principal
n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
