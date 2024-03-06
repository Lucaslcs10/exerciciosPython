print('CALCULADOR DE DESCONTO')
p = float(input('Qual o atual valor do produto? R$'))
d = int(input('Qual a % de desconto? '))
df = d/100
vf = df*p
print(f'O produto com valor de R${p:.2f} com desconto de {d}% passa a custar R${p-vf:.2f}')
