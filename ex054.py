from datetime import date
#  Grupo da Maioridade
contador = 0
for c in range(1, 8):
    ano = int(input(f'Qual o ano de nascimento da {c}ª pessoa? '))
    idade = date.today().year - ano
    print(f'{idade} anos')
    if idade <= 17:
        contador = contador + 1
        print('Menor de idade!')
    else:
        print('Maior de idade!')
print(f'{contador} pessoa(s) ainda são menores de idade!')
print(f'E {7 - contador} já são maiores de idade!')
