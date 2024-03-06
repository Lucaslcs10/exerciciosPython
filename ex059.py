v1 = int(input('Qual o primeiro valor? '))
v2 = int(input('Qual o segundo valor? '))
op = 0
while op != 5:

    print('[1] SOMAR', '\n[2] MULTIPLICAR', '\n[3] MAIOR', '\n[4] NOVOS NÚMEROS', '\n[5] SAIR')
    op = int(input('Qual a opção? '))
    if op == 1:
        print(f'A soma entre {v1} e {v2} é igual a {v1 + v2}')
    elif op == 2:
        print(f'A multiplicação entre {v1} e {v2} é igual a {v1 * v2}')
    elif op == 3:
        if v1 == v2:
            print('Os valores são iguais!')
        elif v1 > v2:
            print(f'O {v1} é maior que o {v2}')
        else:
            print(f'O {v2} é maior que o {v1}')
    elif op == 4:
        v1 = int(input('Qual o primeiro valor??? '))
        v2 = int(input('Qual o segundo valor??? '))
    elif op == 5:
        print('Finalizando... Volte sempre!')
    else:
        print('Opção inválida! Tente novamente...')
    print('=-=' * 15)
