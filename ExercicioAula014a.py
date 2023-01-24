idades = list()
maior = 0
menor = 0
idades.append(int(input('Digite uma idade: ')))
idades.append(int(input('Digite uma idade: ')))
idades.append(int(input('Digite uma idade: ')))
idades.append(int(input('Digite uma idade: ')))
idades.append(int(input('Digite uma idade: ')))
for p in idades:
    print(p)
    if p > 10:
        print('\033[92mYES\033[m')
        menor += 1
    elif p <= 10:
        print('\033[91mNO\033[m')
        maior += 1
print(f'{maior}')
print(f'{menor}')