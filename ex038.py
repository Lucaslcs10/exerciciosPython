print('Comparando números')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print(f'O primeiro valor {n1} é MAIOR que o segundo valor {n2}')
elif n2 > n1:
    print(f'O segundo valor {n2} é MAIOR que o primeiro valor {n1}')
elif n1 == n2:
    print(f'Os valores são iguais!')
