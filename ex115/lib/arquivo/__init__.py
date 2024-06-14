import cores
from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'ERRO ao criar o arquivo {cores.vermelho}{nome}{cores.normal}')
    else:
        print(f'Arquivo {cores.verde}{nome}{cores.normal} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Erro ao inicializar o arquivo {cores.vermelho}{nome}{cores.normal}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<32} {dado[1]:3>} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'Erro ao inicializar o arquivo {cores.vermelho}{arq}{cores.normal}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever dados')
        else:
            print(f'Novo registro de {verde}{nome}{normal} adicionado com sucesso!')
            a.close()
