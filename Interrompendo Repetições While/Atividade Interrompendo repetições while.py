# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condiçao de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma entre eles é {soma}')

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} {n * c}')
    print('-' * 30)

# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

'''v = 0
while True:
    player = int(input('Digite um número: ')
    comp = randint(0, 10)
    total = player + comp
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR ? [I/P]')).upper().strip()[0]
    print(f'VOcê jogou {player} e o Computador jogou {comp}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if total == 'P':
        if total % 2 == 0:
            print('Você GANHOU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você GANHOU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'FIM DE JOGO! Você venceu {v} vezes')'''

#  Crie um programa que leia a idade e o sexo de vários.
# A cada pessoa cadastrada,o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantos pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ''

    while sexo not in 'MmFf':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é {tot18}')
print(f'O total de homens cadastrado foi {totH}')
print(f'{totM20} mulheres com menos de 20 anos foram cadastrada')'''

# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
t_gasto = qtd_pro = cont = menor = 0
barato = ''
while True:
    produto = str(input('Informe o produto: '))
    valor = float(input('Digite o valor: R$'))
    cont += 1
    qtd_pro += valor
    if valor > 1000:
        qtd_pro += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    resp = ''
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais algum produto ? [S/N] ')).strip().upper()[0]
    if resp == 'n':
        break
print(f'O total de gasto foi R${t_gasto:.2f}')
print(f'{qtd_pro} produtos custam mais que R$1.000')
print(f'O produto mais barato foi o {barato} que custa R${menor:.2f}')

# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (Número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input('Que valor você deseja sacar ? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced == 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Volte sempre')