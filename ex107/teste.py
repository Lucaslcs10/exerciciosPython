import moeda

num = float(input("Digite um preço: R$"))
taxa = int(input("% de taxa: "))
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'Aumentando R${num} em {taxa}%, temos R${moeda.aumentar(num, taxa)}')
print(f'Diminuindo R${num} em {taxa}%, temos R${moeda.diminuir(num, taxa)}')
