exp = input('Digite uma expressão: ')
if '(' or ')' in exp:
    qtd1 = exp.count('(')
    qtd2 = exp.count(')')
    if qtd1 == qtd2:
        print('\033[92m Essa expressão está correta!')
    else:
        print('\033[91m Essa expressão está errada!')

#exp = str(input('Digite uma expressão: ')
#pilha = []
#for simb in exp
#   if simb == '(':
#       pilha.append('(')
#   elif simb == ')':
#       if len(pilha) > 0:
#           pilha.pop()
#       else:
#           pilha.append(')')
#           break
#if len(pilha) == 0:
#print('Valido!')
#else:
#print('Errado!')