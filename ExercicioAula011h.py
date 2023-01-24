num = int(input('Digite um número: '))
tot = 0
for p in range(1, num + 1):
    if num % p == 0:
        print('\033[32m ', end='')
        tot += 1
    else:
        print('\033[31m ', end='')
    print('{}'.format(p), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Esse número é PRIMO!')
else:
    print('Esse número não é PRIMO!')
