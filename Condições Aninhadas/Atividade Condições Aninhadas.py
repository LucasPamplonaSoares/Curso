# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa ? '))
salario = float(input('Qual o seu salário ? '))
anos = int(input('Quantos anos de Financiamento ? '))
prestancao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar a casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('a prestação será de R${:.2f} reais '.format(prestancao))
if prestancao <= minimo:
    print('Emprestimo pode ser Aceito')
else:
    print('Emprestimo negado')

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das 3 OPÇÕES ABAIXO:
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
opcao = int(input('Escolha uma OPÇÃO: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))

# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
n1 = int(input('Informe o Primeiro Número: '))
n2 = int(input('Informe o Segundo Número: '))
if n1 > n2:
    print('Primeiro Número é maior')
elif n2 > n1:
    print('Segundo Número é Maior')
else:
    print('Os dois números tem o mesmo valor')

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

atual = date.today().year
nasc = int(input('Qual o seu ano de Nascimento ? '))
idade = atual - nasc
print('Você nasceu no ano {} e tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você Precisa se alistar')
elif idade < 18:
    saldo = idade - 18
    print('Você não tem idade para se alistar. Faltam {} anos para se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos atrás'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO - Média 7.0
# ou superior: APROVADO
n1 = float(input('Informe uma Nota: '))
n2 = float(input('Informe uma Nota: '))
m = n1 + n2 / 2
print('Sua média é {}'.format(m))
if m < 5:
    print('REPROVADO')
elif m <6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade: - Até 9 anos : MIRIM - Até 14 anos : INFANTIL - Até 19 anos : JUNIOR - Até 20
# anos : SÊNIOR - Acima : MASTER
ano_atual = date.today().year
data = int(input('Qual o seu ano de Nascimento ? '))
idade_atleta = ano_atual - data
print('Você tem {} anos'.format(idade_atleta))
if idade_atleta <= 9:
    print('Categoria : MIRIM')
elif idade_atleta <= 14:
    print('Categoria : INFANTIL')
elif idade_atleta <= 19:
    print('Categoria : JUNIOR')
elif idade_atleta <= 20:
    print('Categoria : SÊNIOR')
else:
    print('Categoria : MASTER')

# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero : Todos os lados iguais
# - Isósceles : Dois lados iguais
# - Escaleno : Todos os lados diferentes
r1 = float(input('Primeiro segmento: '))
r2 = float (input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    if r1 != r2 != r3 != r1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos acima não podem formar um triangulo')

# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo: - Abaixo de 18.5 : Abaixo do Peso - Entre 18.5 e 25 : Peso ideal - 25 até 30 : Sobrepeso - 30 até 40
# : Obesidade - Acima de 40 : Obesidade mórbida
peso = float(input('Qual o seu peso ? '))
altura = float(input('Qual a sua altura ? '))
IMC = peso / (altura ** 2)
print('O IMC é de {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do Peso')
elif IMC < 25:
    print('Peso Idela')
elif IMC < 30:
    print('Sobrepeso')
elif IMC < 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade Mórbida')

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento: - Á vista dinheiro / cheque : 10% de desconto - Á vista no cartão : 5% de desconto - Em até 2x no cartão
# : preço normal - 3x ou mais no cartão : 20% de juros
preco = float(input('Preco das Compras'))
print('''FORMAS DE PAGAMENTO
[ 1 ] Dinheiro/ Cheque
[ 2 ] Cartão
[ 3 ] Cartão Parcelado 2x
[ 4 ] Cartão Parcelado 3x''')
opcao = int(input('Qual a opção : '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
if opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua comprar será parcelada por 2x em R${:.2f} reais'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcela = int(input('Quantas parcelas ? '))
    parcela = total / total_parcela
    print('Sua compra será parcelada em {}x de R${:.2f} reais com juros'.format(total_parcela,parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))

# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas Opções
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
player = int(input('Qual é a sua escolha ? '))
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[player]))
if comp == 0: # Computador jogou PEDRA
    if player == 0:
        print('EMPATE')
    elif == 1:
        print('Jogador VENCEU')
    elif == 2:
        print('Computador Venceu')
    else:
        print('Jogada Invalida')
elif comp == 1: # Computador jogou PAPEL
    if player == 0:
        print('Computador GANHA')
    elif == 1:
        print('EMPATE')
    elif == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Invalida')
elif comp == 2: # Computador jogou TESOURA
    if player == 0:
        print('Jogador VENCEU')
    elif == 1:
        print('Computador VENCEU')
    elif == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida')