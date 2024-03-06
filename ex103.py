#  Ficha do Jogador


def cadastrar(a, b):
    """
    ->Cadastra e 'valida' a ficha de um jogador.
    :param a: Primeiro nome do jogador.
    :param b: Número de gols do jogador.
    :return: Mostra a quantidade de gols que o jogador marcou!
    """
    if not a.replace(' ', '').isalpha():  # se (a) sem espaços não alpha
        a = '<desconhecido>'  # retorna '<desconhecido>' para (a)
    else:  # se (a) alpha
        a = a.split()[0]  # retorna primeiro nome de (a) para (a)
    if not b.replace(' ', '').isnumeric():  # se (b) sem espaços não numeric
        b = 0  # retorna 0 para (b)
    else:  # se (b) numeric
        b = b.split()[0]  # retorna primeiro número de (b) para (b)
    print(f'O(a) jogador(a) {a} marcou {b} gol(s) no jogo!')  # mostra o resultado final do programa


#  programa principal
while True:
    j = input('Nome do jogador: ').strip().title()  # recebe o nome e retira os espaços vazios antes e depois
    g = input('Gols(dígitos): ').strip().title()  # recebe os gols e retira os espaços vazios antes e depois
    cadastrar(j, g)  # chama a função (cadastrar)
    while True:
        c = input('Continuar? [S/N] ').upper().replace(' ', '')  # pergunta se usuário quer continuar
        if c != 'S' and c != 'N':  # se (c) não 'Ss' ou  (c) não 'Nn' entra em loop
            print('Opção inválida! Digite "S" ou "N" para continuar')  # mostra opção inválida
        else:  # se (c) 'Ss' ou (c) 'Nn'
            break  # quebra o loop
    if c == 'N':  # se (c) 'Nn' termina programa, se não loop
        break
