print('Bem-vindo ao leitor de unidades.')
number = int(input('Digite um número: '))
n = str(number)
mil = n[0]
cem = n[1]
dez = n[2]
uni = n[3]
print('Esse número possui {} milhares, {} centésimos, {} dezenas e {} unidades'.format(mil, cem, dez, uni))
