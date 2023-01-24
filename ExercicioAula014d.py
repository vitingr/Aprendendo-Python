from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print('{:=^50}'.format('\033[1;36mSORTEADOR\033[m'))
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(' '*30)
print('='*40)
print(' '*30)
print(f'O maior valor sorteado é o número {max(numeros)}')
print(f'O menor valor sorteado é o número {min(numeros)}')
