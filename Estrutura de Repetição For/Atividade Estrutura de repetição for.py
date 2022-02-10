from time import sleep

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificios, indo de 10 até
# 0, com uma pausa de 1 segundo entre eles.
for foguete in range(10, -1, -1):
    sleep(1)
    print(foguete)
print('EXPLODIU')

# Faça um programa que calcule a soma entre todos os números imparse que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
soma = 0
cont = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
print('A soma de todos os {} valores solicitados são {}'.format(soma, cont))

# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um Número: '))
for g in range(1, 11):
    print('{} x {:2} = {}'.format(num, g, num * g))

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar, desconsidere-o.
s = 0
c = 0
for i in range(1, 7):
    numero = int(input('Digite o {} valor: '.format(i)))
    if numero % 2 == 0:
        s += numero
        c += 1
print('Você informou {} números e a soma foi {}'.format(s, c))

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for r in range(primeiro, decimo, razao):
    print('{} '.format(r), end=' > ')

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
núm = int(input('Digite um número: '))
for a in range(1, núm + 1):
    if núm % a == 0:
        print('\033[34m]', end=' ')
        to += 1
    else:
        print('\033[33m]', end=' ')
    print('{} '.format(a), end=' ')
print('O número {} foi divisivel {} vezes'.format(núm, to))
if to == 2:
    print('É primo')
else:
    print('Não É primo')

# Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Palindromo')
else:
    print('Não é um Palindromo')
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = nasc = int(input('Em que ano a {} nasceu ?  '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} pessoas de maior'.format(totmaior))
print('Temos {} pessoas de menor'.format(totmenor))

# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('O peso da {}° pessoa '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior Peso {}Kg'.format(maior))
print('Menor Peso {}Kg'.format(menor))

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre.
soma_idade = 0
somaidade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
totMulher20 = 0
for e in range(1, 5):
    print('------- {}° PESSOA -------'.format(e))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    Sexo = int(input('Sexo[F/M]: ')).strip()
    somaidade =+ idade
    if e == 1 and Sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if Sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if Sexo in 'Ff' and idade < 20:
        totMulher20 =+ 1

media_idade = somaidade / 4
print('A média de idade é {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maior_idade_homem, nome_velho))
print('Tem {} mulheres com menos de 20 anos'.format(totMulher20))