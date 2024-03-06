print('Conversor de Bases Numéricas')
num = int(input('Digite um número inteiro: '))
print('Qual a base para conversão?')
print('[ 1 ] BINÁRIO')
print('[ 2 ] OCTAL')
print('[ 3 ] HEXADECIMAL')
op = int(input('Sua escolha: '))
if op == 1:
    print(f'O número {num} em BINÁRIO é igual a: {num:b}')
elif op == 2:
    print(f'O número {num} em OCTAL é igual a: {num:o}')
elif op == 3:
    print(f'O número {num} em HEXADECIMAL é igual a: {num:x}')
else:
    print('OPÇÃO INVÁLIDA!')
