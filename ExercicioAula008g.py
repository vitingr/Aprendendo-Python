v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite mais um valor: '))
if v1 < v2 and v1 < v3:
    print('O menor valor é o número {}'.format(v1))
if v2 < v1 and v2 < v3:
    print('O menor valor é o número {}'.format(v2))
if v3 < v1 and v3 < v2:
    print('O menor valor é o número {}'.format(v3))
if v1 > v2 and v1 > v3:
    print('O maior valor é o número {}'.format(v1))
if v2 > v1 and v2 > v3:
    print('O maior valor é o número {}'.format(v2))
if v3 > v1 and v3 > v2:
    print('O maior valor é o número {}'.format(v3))
