# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Qual o seu sexo ? [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} informado com exato! ')

# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
comp = randint(0, 10)
print('Acabei de pensar em um número. Tente adivinhar qual é')
acertou = False
palpite = 0
while not acertou:
    player = int(input('Qual o seu palpite ? '))
    palpite += 1
    if player == comp:
        acertou = True
print(f'Acertou com {palpite} palpites')

# Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
# [1]SOMAR
# [2]MULTIPLICAR
# [3]MAIOR
# [4]NOVOS NÚMEROS
# [5]SAIR DO PROGRAMA
# Seu programa deverá realizar a operação solicitada em casa caso.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
opcao = 0
while opcao != 5:
    print('''           [1] SOMAR
               [2] MULTIPLICAR
               [3] MAIOR
               [4] NOVOS NÚMEROS
               [5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual a sua opção ? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2}  é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} resulta em {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior  = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:  ')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção invalida')
print('Volte sempre')

# faça um programa que leia um número qualquer e mostre o seu fatorial.
# EX: 5! = 5x4x3x2x1=120
n = int(input('Digite um número'))
c = n
f = 1
print(f'Fatorial de {n}!', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x  ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'{f}')

# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
primeiro = int(input('Digite um número: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}')
    termo += razao
    cont += 1

# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disse que quer mostrar O TERMOS.
primeiro = int(input('Digite um número: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    while cont <= total:
        print(f'{termo} > ', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar ? '))
print(f'Progressão finalizada com {total} termos mostrados')

# Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n' primeiros elementos de uma
# Sequência de Fibonacci. Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
n = int(input('Digite um valor: '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    cont += t1

# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    cont += num
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')

# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
res = 'S'
soma = quant = media = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Dejesa continuar ? [S/N] : ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {n} números e a média foi {media}')
print(f'O maior valor foi o {maior} e o menor foi {menor}')