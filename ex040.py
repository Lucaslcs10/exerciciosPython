azul = '\033[34m'
verde = '\033[32m'
vermelho = '\033[31m'
normal = '\033[m'
amarelo = '\033[33m'
print(f'{azul}Aquele clássico da Média{normal}')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média >= 7:
    print(f'Média: {média:.1f} {verde}APROVADO!{normal}')
elif média <= 5:
    print(f'Média: {média:.1f} {vermelho}REPROVADO!{normal}')
else:
    print(f'Média {média} {amarelo}RECUPERAÇÃO!{normal}')
