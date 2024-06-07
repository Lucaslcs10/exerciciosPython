vermelho = '\033[31m'
normal = '\033[m'


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip().split()
        if entrada[0].isalpha() or entrada == '':
            print(f'{vermelho}ERRO: "{entrada[0]}" não é um preço válido!{normal}')
        else:
            valido = True
            return float(entrada[0])
