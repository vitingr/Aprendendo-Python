from datetime import datetime


def voto(a):
    atual = datetime.now().year
    idade = atual - a
    if 18 < idade <= 65:
        return f'Com {idade} anos: OBRIGADO VOTAR!'
    elif idade >= 16 or idade > 65:
        return f'Com {idade} anos: OPCIONAL VOTAR!'
    elif idade < 16:
        return f'Com {idade} anos: NÃO PODE VOTAR!'


print('-' * 40)
a = int(input('Em que ano você nasceu?: '))
voto(a)
print(voto(a))
