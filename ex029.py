print('Radar eletrônico')
ve = int(input('Quantos Km/h o carro estava? '))
if ve <= 80:
    print('Você estava dentro do limite de velocidade de 80km/h')
    print('Continue dirigindo com segurança!')
else:
    print('Você estava acima do limite de velocidade de 80km/h')
    print(f'Você foi multado em R${(ve-80) * 7}')
    print('Dirija com mais cuidado!')
print(' ')
print('Boa viagem!')
