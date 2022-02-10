# + = Adição
# - = Subtração
# * = Multiplicação
# / = Divisão
# ** = Potência
# // = Divisão Inteira
# % = Resto da Divisão

# Ordem Precedência :
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a  divisão é {}'.format(s, m, d), end=' ')
print('Divisão inteira é {} e potência {}'.format(di, e))
