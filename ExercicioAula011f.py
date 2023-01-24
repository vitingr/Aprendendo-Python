soma = 0
cont = 0
for c in range(0, 6):
    number = int(input('Digite um número: '))
    if number % 2 == 0:
        soma += number
        cont += 1
print('Você informou {} valores pares, e o valor da soma entre esses valores é {}'.format(cont, soma))
