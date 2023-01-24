from time import sleep
print('{:=^40}'.format('\033[1;36mLOJA DO FRALDINHA\033[m'))
print(''*30)
nome = str(input('Seu nome: ')).strip()
preco = float(input('Digite o valor da sua compra: R$'))
print('Formas de pagamento:')
print('''
[ 1 ] A Vista no Cartão (10% Off)
[ 2 ] A Vista no Cartão (5% Off)
[ 3 ] 2x No Cartão (Normal)
[ 4 ] 3x ou mais No Cartão (20% Juros)
''')
print(''*30)
opcao = int(input('Qual sua forma de pagamento? '))
print(''*30)
print('PROCESSANDO...')
print(''*30)
sleep(2)
if opcao == 1:
    op1 = preco - (preco * 10 / 100)
    print('Sua compra de R${:.2f} irá ficar no valor de R${:.2f}'.format(preco, op1))
    print('Obrigado, volte sempre!')
elif opcao == 2:
    op2 = preco - (preco * 5 / 100)
    print('Sua compra de R${:.2f} irá ficar no valor de R${:.2f}'.format(preco, op2))
    print('Obrigado, volte sempre!')
elif opcao == 3:
    op3 = preco
    print('Sua compra ficou no valor de R${:.2f}'.format(op3))
    print('Obrigado, volte sempre!')
else:
    op4 = (preco * 20 / 100) + preco
    print('Sua compra de R${:.2f} irá ficar no valor de R${:.2f}'.format(preco, op4))
    print('Obrigado, volte sempre!')
