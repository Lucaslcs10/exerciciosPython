print('CALCULADOR DE ALUGUEL DE CARROS')
km = float(input('Qual a distância percorrida em KM? '))
d = int(input('Por quantos dias o carro foi alugado? '))
kmf = km * 0.15
df = d * 60
t = kmf + df
print(f'O total a ser pago pelo aluguel de {d} dias e pelos {km:.1f}km rodados é de: R${t:.2f}')
