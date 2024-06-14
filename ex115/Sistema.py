from ex115.lib.arquivo import *

arq = 'listaCadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['VER CADASTROS', 'NOVO CADASTRO', 'SAIR DO SISTEMA'])
    if resposta == 1:
        cabeçalho('LISTA DE PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = Int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print(f'Opção {vermelho}INVÁLIDA!{normal} Digite uma opção {verde}VÁLIDA!{normal}')
