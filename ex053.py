#  Detector de Palíndromo
frase = input('Digite uma frase: ').strip().upper().replace(" ", "")
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[c]
print(frase, inverso, end='')
if inverso == frase:
    print('\nÉ um palíndromo!')
else:
    print('\nNão é um palíndromo!')
