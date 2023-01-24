print('{:=^40}'.format('\033[1;31mProgressão Aritmética\033[m'))
print(' '*30)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão: '))
print(' '*30)
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' ')
print('FIM')