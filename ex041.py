from datetime import date
normal = '\033[m'
azul = '\033[34m'
print(f'{azul}Classificando Atletas{normal}')
ano = int(input('Qual o ano de nascimento do(a) Atleta? '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Atleta{azul} MIRIM{normal} com {azul}{idade}{normal} anos de idade!')
elif idade <= 14:
    print(f'Atleta{azul} INFANTIL{normal} com {azul}{idade}{normal} anos de idade!')
elif idade <= 19:
    print(f'Atleta{azul} JÚNIOR{normal} com {azul}{idade}{normal} anos de idade!')
elif idade <= 25:
    print(f'Atleta{azul} SÊNIOR{normal} com {azul}{idade}{normal} anos de idade!')
else:
    print(f'Atleta{azul} MASTER{normal} com {azul}{idade}{normal} anos de idade!')
