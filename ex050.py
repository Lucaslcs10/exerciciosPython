soma = 0
contador = 0
contadorpar = 0

for c in range(1, 7):
    num = int(input(f'Digite {c}º valor inteiro: '))
    if num % 2 == 0:
        soma = soma + num
        contadorpar = contadorpar + 1
    contador = contador + 1
print(f'Você digitou {contador} números!')
print(f'{contadorpar} são números pares!')
print(f'A soma dos números pares é igual a {soma}')
