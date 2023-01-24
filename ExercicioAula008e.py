from time import sleep
print('='*30)
print(''*30)
print('Em viagens de até 200Km será cobrado uma tarifa de R$0,50 para cada Km.')
print('Em viagens mais longas, acima de 200Km será cobrado uma tarifa de R$0,45 para cada Km.')
print('Portanto, qual será a distância que você irá percorrer?')
dist = int(input('A distância a percorrer em quilometros é de: '))
print(''*30)
print('='*30)
print(''*30)
print('Processando... ')
print(''*30)
sleep(2)
if dist <= 200:
    valor = dist * 0.50
    print('A distância a ser percorrida é de {}Km, portanto será cobrado um valor de R${:.2f}'.format(dist, valor))
    print('Boa viagem!')
else:
    valor1 = dist * 0.45
    print('A distância a ser percorrida é de {}Km, portanto será cobrado um valor de R${:.2f}'.format(dist, valor1))
    print('Boa viagem!')
