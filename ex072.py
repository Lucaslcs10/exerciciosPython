#  Número por Extenso
lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
         'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
         'Dezoito', 'Dezenove', 'Vinte')
c = ' '
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n not in range(0, 21):
        print('Valor inválido. Tente novamente!')
        n = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número: {lista[n]}')
    while c != 'S' and c != 'N':
        c = input('Quer continuar? [S/N] ').upper().replace(' ', '')
    if c == 'N':
        break
    c = ' '
print('Finalizando...')
