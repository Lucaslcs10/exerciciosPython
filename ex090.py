#  Dicionário em Python
alunos = {'nome': input('Nome: ').strip().title().split()[0]}
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
print('* ' * 15)
print(f'* Nome: {alunos["nome"]:<20}*')
print(f'* Média: {alunos["media"]:<19.1f}*')
if alunos['media'] <= 5:
    print(f'* {'Situação: Reprovado!':<26}*')
elif alunos['media'] < 7:
    print(f'* {'Situação: Recuperação!':<26}*')
else:
    print(f'* {'Situação: Aprovado!':<26}*')
print('* ' * 15)
