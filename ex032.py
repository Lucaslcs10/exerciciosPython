from datetime import date
print('Ano Bissexto')
ano = int(input('Qual o ano que deseja consultar? Digite "0" para consultar o ano atual: '))
if ano == 0:
    ano = date.today().year
anob = ano % 4
if anob == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')

print('FIM')
