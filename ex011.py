print('CALCULADOR DE TINTA PARA PAREDE')
a = float(input('Qual é a altura da parede? '))
la = float(input('Qual é a largura da parede? '))
p = a * la
t = p / 2
print(f'Você precisará de {t:.1f}L de tinta para pintar sua parede de {p:.1f}m² ')
