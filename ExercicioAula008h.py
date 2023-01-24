print('Digite 3 segmentos e veja se é possível formar um triângulo com eles.')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
if n1 < n2 + n3:
    print('Sim, com os segmentos {}, {}, {} é possível formar um triângulo'.format(n1, n2, n3))
else:
    print('Não, com os segmentos {}, {}, {} não é possível formar um triângulo'.format(n1, n2, n3))
