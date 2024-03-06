#  Função que calcula área
def calc_area(l, c):
    res = l * c
    print(f'A área do terreno de ({l:.1f} x {c:.1f}) é de {res:.1f}².')


#  programa principal
print('* ' * 15)
print(f'{'TERRENO':-^29}')
print('* ' * 15)
calc_area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
