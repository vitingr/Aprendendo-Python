n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
print('Você digitou os seguintes números: ')
numeros = (n1, n2, n3, n4)
qtd = numeros.count(n1)
menor = min(numeros)
posicao = numeros.index(menor) + 1
if qtd == 1:
    print(f'O valor {n1} apareceu {qtd} vez')
else:
    print(f'O valor {n1} apareceu {qtd} vezes')
print(f'O valor {menor} é menor da lista, e ele apareceu na posição {posicao}')
print('Os valores pares digitados foram: ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
