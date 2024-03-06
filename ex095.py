cadastro = {}
gols = []
lista = []
while True:
    cadastro['Nome:'] = str(input('Nome do jogador: ')).strip().title().split()[0]  # pega o primeiro nome do jogador
    partidas = int(input(f'Quantas partidas {cadastro["Nome:"]} jogou: '))  # conta quantas partidas jogador jogou
    for p in range(partidas):  # cria LISTA com gols que jogador fez em cada partida
        gols.append(int(input(f'    Quantos gols {cadastro["Nome:"]} fez na {p + 1}ª partida? ')))
    cadastro['Gols:'] = gols[:]  # cria DIC com gols do jogador da vez
    cadastro['Total:'] = sum(cadastro['Gols:'])
    lista.append(cadastro.copy())  # cria uma CÓPIA do DIC com os dados do jogador da vez
    gols.clear()  # limpa a LISTA de gols para o próximo jogador
    while True:  # pergunta se quer continuar
        c = input('Continuar? [S/N] ').upper().replace(' ', '')
        if c != 'S' and c != 'N':
            print('Opção inválida! Digite "S" ou "N" para continuar')
        else:
            break
    if c == 'N':
        break
print(gols)
print(cadastro)
print(lista)
print('* ' * 20)
print(f'Cód|{'Nome':<15}{'|Gols':<13}{'|Total|':<13}')
for k, v in enumerate(lista):  # k=index do primeiro jogador do grupo, v=todos os dados do jogador sendo tratado
    print(f'({k + 1:})|', end='')  # index do primeiro jogador + 1
    for d in v.values():  # d=cada elemento em v.values()=valores do dados do jogador sendo tratado
        print(f'{str(d):<15}', end='')
    print()
while True:  # pergunta se usuario quer saber dados de cada jogador
    s = int(input('Qual jogador deseja buscar resultados? (Cód) [999 = PARAR] ')) - 1  # pergunta o jogador
    if s == 998:  # se o usuario digitar 999 o programa para
        break
    if s >= len(lista):  # se o usuario digitar errado o programa pergunta novamente
        print('Cód inválido! Por gentileza digite um cód válido!')
    else:
        print('-' * 60)
        print(f'DADOS DO(A) JOGADOR(A) {lista[s]['Nome:'].upper()}')  # mostra os dados dos jogadores
        for i, g in enumerate(lista[s]['Gols:']):  # i=INDEX do gol/partida na lista, g=LISTA de gols(i) do jogador(s)
            print(f'Na {i+1}ª partida: {lista[s]['Nome:'].upper()} fez {g} GOL(s)!')
        print('-' * 60)
