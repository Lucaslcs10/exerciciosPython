#  Cadastro de Trabalhador em Python
from datetime import date
cadastro = dict()
cadastro['Nome: '] = str(input('Nome: ')).strip().title().split()[0]
cadastro['Idade: '] = date.today().year - int(input('Ano de nascimento: '))
cadastro['Ctps: '] = int(input('CTPS [0 = Não possui]: '))
if cadastro['Ctps: '] != 0:
    cadastro['Ano de contratação: '] = int(input('Ano da contratação: '))
    cadastro['Salário: R$'] = float(input('Salário R$: '))
    cadastro['Aposentadoria: '] = (cadastro['Ano de contratação: '] + 35 - (date.today().year - cadastro['Idade: ']))
print('Não possui')
print('* ' * 20)
print(f'{'DADOS CADASTRADOS':^40}')
for k, v in cadastro.items():
    if k == 'Idade: ':
        print(f'-{k}{v} anos')
    elif k == 'Salário: R$':
        print(f'-{k}{v:.2f}')
    elif k == 'Aposentadoria: ':
        print(f'-{k}{v} anos')
    else:
        print(f'-{k}{v}')
