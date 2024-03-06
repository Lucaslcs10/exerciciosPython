print('Aprovando Empréstimo')
casa = float(input('Qual o valor da casa? R$'))
if casa < 10000:
    casa = casa * 100
sal = float(input('Qual o seu salário? R$'))
finan = int(input('Quantos anos de financiamento? '))
prest = float(casa / finan) / 12
if prest > sal * 30 / 100:
    print(f'O valor da prestação ultrapassa 30% do seu salário. O financiamento não pode ser feito.')
else:
    print(f'O valor da prestação será de R${prest:.2f} mensais')
    print(f'seu financiamento de R${casa:.2f} será pago em {finan} anos!')
