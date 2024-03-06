from math import sin, cos, tan, radians
print('CALCULADOR DE SENO, COSSENO E TANGENTE')
a = float(input('Qual ângulo você deseja? '))
ar = radians(a)
s = sin(ar)
c = cos(ar)
t = tan(ar)
print(f'O ângulo de {a:.2f} tem o SENO de {s:.2f}, o COSSENO de {c:.2f} e a TANGENTE DE {t:.2f}.')
