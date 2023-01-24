import math
print('Bem-vindo à calculadora de hipotenusa')
x = float(input('Digite o valor de um cateto (x): '))
y = float(input('Digite o valor do outro cateto (y): '))
xy = (x ** 2) + (y ** 2)
hipo = math.sqrt(xy)
print('Com base nos valores dos catetos de {:.2f} e {:.2f}. O valor da hipotenusa será de {:.2f}'.format(x, y, hipo))
print('Obrigado por fazer o uso do nosso software, espero que tenha tido uma boa experiência :D')
