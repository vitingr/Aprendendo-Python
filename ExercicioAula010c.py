num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal ''')
option = int(input('Digite sua opção: '))
if option == 1:
    print('O valor {} em Binário é {}'.format(num, bin(num)))
elif option == 2:
    print('O valor {} em Octal é {}'.format(num, oct(num)))
else:
    print('O valor {} em Hexadecimal é {}'.format(num, hex(num)))
