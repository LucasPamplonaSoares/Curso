# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
n = []
mais = 0
menos = 0
for c in range(0, 5):
    n.append(int(input(f'Digite um Número para a posição {c}: ')))
    if c == 0:
        mais = menos = n[c]
    else:
        if n[c] > mais:
            mais > n[c]
        if n[c] < menos:
            menos < n[c]
print()
print(f'Você digitou os números {n}')
print(f'O maior valor digitado foi {mais} na posição ', end='')
for i, v in enumerate(n):
    if v == mais:
        print(f'{i} ... ', end='')
print()
print(f'O menor valor digitado foi {menos} na posição ', end='')
for i, v in enumerate(n):
    if v == menos:
        print(f'{i} ... ', end='')
print()
# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numero = list()
while True:
    n = int(input('Digite um Número: '))
    if n not in numero:
        numero.append(n)
    else:
        print('Número já digitado. Por favor digita um número diferente')
    r = str(input('Deseja digitar mais algum número ? [S/N] '))
    if r in 'Nn':
        break
numero.sort()
print(f'Os números digitados foram esses {numero}')
# Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição
# correta de inserção( SEM USAR O SORT()). No final, mostre a lista ordenada na tela.
lista = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
while True:
    n = int(input('Digite um Número: '))
    numeros.append(n)
    r = str(input('Deseja informar mais algum número ? [S/N] ')).strip().upper()
    if r in 'Nn':
        break
print(f'Você digitou {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Os números em ordem decrescente são {numeros}')
if 5 in numeros:
    print('Número 5 está na Lista')
else:
    print('Número 5 não está na lista')

# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.
num = list()
pares = list()
impar = list()
while True:
    n = int(input('Digite um número: '))
    resp = str(input('Deseja informar mais algum Número ? [S/N] ')).strip().upper()
    if resp in 'Nn':
        break
for i, v in enumerate(n):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {n}')
print(f'A lista de pares é {pares}')
print(f'A lista de impar é {impar}')

# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo devevrá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp = str(input('Digite a expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() # pop remove o ultimo elemento da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está invalida')