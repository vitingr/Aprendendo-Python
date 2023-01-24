prod = float(input('Qual o valor da sua compra? R$'))
prod1 = prod * 5 / 100
prod2 = prod - prod1
print('Ótimo, porém estamos com uma promoção de 5% de Desconto sobre o valor total da compra\nCom isso, o valor do '
      'total da sua compra será de R${:.2f}'.format(prod2))
