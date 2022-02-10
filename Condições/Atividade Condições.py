from random import randint
from time import sleep

# Escreva um programa que faça o computador "pensar" em um número inteiro entre o e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
comp = randint(0, 5)  # Faz o computador "PENSAR"
player = int(input('Em qual número eu pensei ? '))  # Jogador tentando acertar
print('PROCESSANDO...')
sleep(2)
if player == comp:
    print('Parabéns você ganhou')
else:
    print('RSRSRSRSRS VOCÊ PERDEU OTÁRIO')
    print('Pensei no número {} e não no {}'.format(comp, player))

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.
velocidade = int(input('Qual a velocidade do seu Carro ? '))
if velocidade > 80:
    print('Você ultrapassou a velocidade limite')
    multa = (velocidade - 80) * 7
    print('A sua multa será de R${} reais'.format(multa))
else:
    print('Sua velocidade está no limite permitido ')

# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
n = int(input('Digite um número: '))
result = n % 2
if result == 0:
    print('Número {} é PAR'.format(n))
else:
    print('Número {} é IMPAR'.format(n))

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50
# por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
distancia = int(input('Qual a distância da viagem em Km ? '))
print('Você ira começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    passagem = distancia * 0.50
    print('O valor da sua passagem será de R${:.2f} reais'.format(passagem))
else:
    passagem = distancia * 0.45
    print('O valor da sua passagem será de R${:.2f} reais'.format(passagem))

# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Qual ano quer analisar ?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é Bissexto'.format(ano))
else:
    print('{} não é Bissexto'.format(ano))

# Faça um programa que leia três números e mostre qual é o maior e qual o menor.
n1 = int(input('Digite um Número: '))
n2 = int(input('Digite um Número: '))
n3 = int(input('Digite um Número: '))

# MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# MAIOR

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número foi o {}'.format(menor))
print('O maior número foi o {}'.format(maior))

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superior a R$1.250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe o seu salário: '))
if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
    print('Seu novo salários será R${:.2f} reais'.format(aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('Seu novo salário será de R${:.2f} reais'.format(aumento))

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.
r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos podem formar um Triangulo')
else:
    print('Os seguimentos não podem formar um Triangulo')
