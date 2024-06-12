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
        print(a.read())

