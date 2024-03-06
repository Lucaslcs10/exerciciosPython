#  Um print especial
def escreva(msg):
    print('-' * (len(msg) + 2))
    print(f' {msg}')
    print('-' * (len(msg) + 2))


#  programa principal
escreva(input('Digite uma mensagem: '))
