from datetime import date
ano = int(input('Digite um ano para ver se ele é bissexto, caso queira analisar o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim, o ano de {} é bissexto.'.format(ano))
else:
    print('Não, o ano de {} não é bissexto.'.format(ano))
