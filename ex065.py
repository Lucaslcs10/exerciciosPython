#  Maior e Menor valores
r = 'S'
soma = menor = maior = contador = media = 0
while r == 'S':
    n = int(input('Digite um número: '))
    contador = contador + 1
    soma = soma + n
    if contador == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    r = input('Quer continuar? ').upper().replace(" ", "")
media = soma / contador
if contador == 1:
    print(f'Você digitou apenas {contador} número!')
    print(f'{soma}! Finalizando...')
else:
    print(f'Você digitou {contador} números e a média entre eles é {media:.2f}')
    print(f'O maior valor digitado é {maior} e o menor é {menor}')
