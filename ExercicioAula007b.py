nome = str(input('Digite seu nome: '))
maiu = nome.upper()
minu = nome.lower()
dividido = nome.split()
total = (len(nome) - nome.count(' '))
nome1 = (dividido[0])
print('Seu nome completo é: ')
print('Seu nome completo maiusculo é: {}'.format(maiu))
print('Seu nome completo minusculo é: {}'.format(minu))
print('Seu nome possui {} letras'.format(total))
print('Seu primeiro nome é {}'.format(nome1))
