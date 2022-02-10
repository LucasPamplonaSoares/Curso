import math
import random
import pygame

# Cria um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: "Digite um número: 6.127. O número 6.127 tem a parte inteira 6.
num = float(input('Digite um Número: '))
porc = math.trunc(num)
print('O número informado foi {} e a sua parte inteira é {}'.format(num, porc))

# Faça um programa que leia o comprimeiro do cateto oposto e do cateto adjacento de um triangulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacento: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('O calculo do cateto oposto {}, do cateto adjacento {} resulta na hipotenusa que é {} '.format(co, ca, hi))

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {}'.format(angulo, tangente))

# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajuda ele,
# lendo o nome deles e escrevendo o nome do escolhido.
aln1 = str(input('Informe o Primeiro Aluno: '))
aln2 = str(input('Informe o Segundo Aluno: '))
aln3 = str(input('Informe o Terceiro Aluno: '))
aln4 = str(input('Informe o Quarto Aluno: '))
lista = [aln1, aln2, aln3, aln4]
sorteio = random.choice(lista)
print('O aluno sortudo foi: {}'.format(sorteio))

# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o
# nome dos quatros alunos e mostre a ordem sorteada.
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lis = [n1, n2, n3, n4]
random.shuffle(lis)

print('Essa é a ordem de apresentação : {}'.format(lis))
# Faça um programa em Python que abra e reproduza o áudio de arquivo MP3.
pygame.init()
pygame.mixer.music.load('') # por um arquivo mp3 ali no canto esquerdo aonde está os arquivos e depois por ali dentro dos parenteses
pygame.mixer.music.play()
pygame.mixer.music.wait()
