number = int(input('Digite o número da tabuada que você deseja ver: '))
for c in range(0, 11):
    print('{} x {:2} = {} '.format(number, c, number*c))
