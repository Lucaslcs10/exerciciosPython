print('Separando dígitos de um número')
num = int(input('digite um número inteiro de 0 a 9999: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print(f'UNIDADE: {u}')
print(f'DEZENA: {d:2}')
print(f'CENTENA: {c:}')
print(f'MILHAR: {m:2}')
