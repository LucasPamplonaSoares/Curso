'''def t(txt): # cria comando personalizados
    print('-' * 30)
    print(txt)
    print('-' * 30)


t('     CURSO EM VIDEO      ')
t('     AULA DE FUNÇÕES     ')'''
'''def soma (a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre A + B = {s}')


soma(9, 8)'''

'''def contador(* num): # * serve pra quando for entrar vários paramentros
    tam = len(num)
    print(f'O tamanho é {tam}')


contador(1, 2, 3, 4)
contador(5, 6, 7, 8)
contador(9, 10)'''

'''def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *=2
        pos += 1


valores = [6, 5, 2, 6, 7]
dobra(valores)
print(valores)'''

'''def soma(* valores):
    s = 0
    for num in valores:
        s += num
        print(f'Somando os valores {valores} temos {s}')


soma(3, 5)
soma(4, 5, 6, 7)

help(print)

print(input.__doc__)'''

'''def contador(i, f, p):
    """"
    SKSKSKSKSKSKSKSKSKS
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


contador(0, 100, 5)'''

'''def soma(a, b, c=0):  # Caso vc não informe um valor pro 'C' ele fica com valor 0
    s = a + b + c
    print(f'A soma vale {s}')


soma(1, 2, 3)
soma(5, 8, 12)'''

'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''

'''def teste():
    global a # Usado para pegar a variavel que está fora do DEF e usar dentro dele
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste()
print(f'A fora vale {a}')'''

'''def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(2, 4, 5)
r2 = soma(5)
r3 = soma(190, 387, 2873)
print(f'Os resultados das minhas somas deram {r1} {r2} e {r3}')'''


'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(9)
f3 = fatorial()
print(f'Os resultados são : {f1} {f2} e {f3}')
n = (int(input('Digite um Número: ')))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''


def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False

num = int(input('Digite um Número: '))
if par(num):
    print('É par')
else:
    print('Não é par')
