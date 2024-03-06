#  from math import hypot
#  print('CALCULADOR DE HIPOTENUSA')
#  co = float(input('Qual o cateto oposto? '))
#  ca = float(input('Qual o cateto adjacente? '))
#  h = hypot(co, ca)
#  print(f'A medida da hipotenusa é {h:.2f}')
co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
h = (co ** 2 + ca ** 2) ** 0.5
print(f'A medida da hipotenusa é {h:.2f}')
