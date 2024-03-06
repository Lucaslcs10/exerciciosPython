#   Unindo dicionários e listas
pessoa = {}
lista = []
soma = 0
while True:
    pessoa['Nome'] = str(input("Nome: ")).strip().title().split()[0]
    while True:
        pessoa['Sexo'] = str(input("Sexo: [M/F] ")).upper().replace(" ", "")
        if pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
            print('Opção inválida! Digite "M" ou "F".')
        else:
            break
    pessoa['Idade'] = int(input('Idade: '))
    soma = soma + pessoa['Idade']
    lista.append(pessoa.copy())
    while True:
        c = str(input('Continuar: [S/N] ')).upper().replace(" ", "")
        if c != 'S' and c != 'N':
            print('Opção inválida! Digite "S" ou "N".')
        else:
            break
    if c == 'N':
        break
print(f'A) {len(lista)} pessoas foram cadastradas!')
print(f'B) A média de idade das pessoas cadastradas é de {soma / len(lista):.0f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for m in lista:
    if m['Sexo'] == 'F':
        print(f'"{m["Nome"]}" ', end='')
print()
print(f'D) As pessoas cadastradas com idade acima da média foram: ', end='')
for a in lista:
    if a['Idade'] > (soma / len(lista)):
        print(f'"{a["Nome"]}" ', end='')
print('\nFIM!')
while True:
    pass
