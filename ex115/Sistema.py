from ex115.lib.interface import *
while True:
    resposta = menu(['VER CADASTROS', 'NOVO CADASTRO', 'SAIR DO SISTEMA'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print(f'Opção {vermelho}INVÁLIDA!{normal} Digite uma opção {verde}VÁLIDA!{normal}')
