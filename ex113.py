from utilidades import leia
vermelho = '\033[31m'
normal = '\033[m'
amarelo = '\033[33m'

ni = leia.Int('Digite um número INTEIRO: ')
nr = leia.Float('Digite um número REAL: ')
print(f'O número {amarelo}INTEIRO{normal} foi {ni} e o número REAL foi {nr}')
