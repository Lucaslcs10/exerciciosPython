#   Analisador completo
soma = 0
contador = 0
media = 0
mv = 0
nome = ''
mulher = 0
for c in range(1, 5):
    print(f'=-=-=-{c}ª PESSOA-=-=-=')
    pessoa = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ').upper().strip()
    soma = soma + idade
    contador = contador + 1
    media = soma / 4
    if sexo == 'M':
        if c == 1:
            mv = idade
            nome = pessoa
        else:
            if idade > mv:
                mv = idade
                nome = pessoa
    elif sexo == 'F':
        if idade <= 20:
            mulher = mulher + 1
    else:
        print('Opção inválida!')
print(f'A média de idade do grupo é {media:.1f} anos!')
print(f'O homem mais velho do grupo tem {mv} anos! E se chama {nome.title()}!')
print(f'Existem {mulher} mulheres com 20 anos ou menos no grupo!')
