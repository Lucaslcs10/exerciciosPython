from time import sleep
#  Contagem regressiva
normal = '\033[m'
vermelho = '\033[31m'
n = int(input('Digite um número para contagem: '))
for c in range(n, 0, -1):
    sleep(1.2)
    print(f'{c}...')
sleep(1.2)
print(f'{vermelho}BOOOOOOOOM!{normal}')
