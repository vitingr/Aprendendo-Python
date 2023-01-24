def area(a, b):
    valor = a * b
    print(f'As medidas do terreno são {a}x{b}')
    print(f'A área do terreno equivale a {valor}m²')


print('-' * 30)
print('Calculadora de Área')
print('-' * 30)
print(' ' * 30)
a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
area(a, b)
