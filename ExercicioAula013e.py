print('{:=^40}'.format(' \033[1;31mCalculadora\033[m '))
numbers = 0
cont = 0
number = int(input('Digite um número: '))
while number != 999:
    numbers += number
    number = int(input('Digite um número: '))
    cont += 1
print('A soma entre os valores informados é de {}'.format(numbers))
