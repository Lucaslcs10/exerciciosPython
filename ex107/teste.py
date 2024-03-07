from ex107 import moeda

num = float(input("Digite um preço: R$"))
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'Aumentando R${num} em 10%, temos R${moeda.aumentar(num)}')
print(f'Diminuindo R${num} em 10%, temos R${moeda.diminuir(num)}')
