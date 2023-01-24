numeros = []
posicaomenor = []
posicaomaior = []
for n in range(0, 5):
    valor = int(input(f'Digite um valor na posição {n}: '))
    numeros.append(valor)
for posicao, valores in enumerate(numeros):
    if valores == min(numeros):
        posicaomenor.append(posicao)
    if valores == max(numeros):
        posicaomaior.append(posicao)
menor = min(numeros)
maior = max(numeros)
print(f'Você digitou os valores {numeros}')
print(f'O número {menor} foi o menor valor digitado na lista, ele apareceu na posição {posicaomenor}')
print(f'O número {maior} foi o maior valor digitado na lista, ele apareceu na posição {posicaomaior}')
