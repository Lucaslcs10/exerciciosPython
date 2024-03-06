print('Custo da Viagem')
dis = int(input('Quantos KM de distância tem a sua viagem? '))
if dis <= 200:
    print(f'A sua viagem de {dis} tem o valor de R${dis * 0.50:.2f}')
else:
    print(f'A sua viagem de {dis} tem o valor de R${dis * 0.45:.2f}')
print(' ')
print('Tenha uma boa viagem!')
