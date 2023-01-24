from datetime import date
atual = date.today().year
totmenor = 0
totmaior = 0
for id in range(1, 9):
    nasc = int(input('Digite o ano que a {}ª pessoa nasceu: '.format(id)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Posusimos \033[32m{} \033[mpessoas de maior'.format(totmaior))
print('E \033[34m{} \033[mpessoas de menor de idade'.format(totmenor))
