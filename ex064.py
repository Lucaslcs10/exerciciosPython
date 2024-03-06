#  Tratando vários valores v1.0
soma = 0
contador = 0
n = int(input('Digite um número: [999] para parar '))
while n != 999:
    contador = contador + 1
    soma = soma + n
    n = int(input('Digite um número [999] para parar: '))
if contador == 1:
    print(f'Você digitou {contador} número e o valor dele é {soma}')
else:
    print(f'Você digitou {contador} números e a soma entre eles é de {soma}')
