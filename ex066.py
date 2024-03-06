#  Vários números com flag
c = s = 0
while True:
    n = int(input('Digite um valor. [999] para parar: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
if c < 1:
    print(f'Você não digitou algum valor!')
if c == 1:
    print(f'Você digitou o valor {s}')
if c > 1:
    print(f'Você digitou {c} valores e a soma entre eles é {s}')
