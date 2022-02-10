# Crie um programa que leia o nome completo de uma pessoa e mostre:
# *O nome com todas as letras maiúscula.
# *O nome com todas minúsculas.
# Quantas letras ao todo(Sem considerar espaços).
# *Quantas letras tem o primeiro nome. -
frase = str(input('Escreva o seu Nome Completo: ')).strip()
print('O seu nome Maiúsculo é : {}'.format(frase.upper()))
print('O seu nome Minúsculo é : {}'.format(frase.lower()))
print('O seu nome tem {} letras'.format(len(frase)))


# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
num = int(input('Digite um Número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Número: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cid = str(input('Qual a sua cidade ? ')).strip()  # strip retira os espaços
print(cid[:5].upper() == 'SANTO')

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual o seu Nome ? ')).strip()
print('SILVA' in nome.upper())

# Faça um programa que leia uma frase pelo teclado e mostra:
# *Quantas vezes aparece a letra "A".
# *Em que posição ela aparece a primeira vez.
# *Em que posição ela aparece a última vez.
tec = str(input('Escreva uma Frase ')).strip().upper()
print('A letra A aparece {}  vezes na frase'.format(tec.count('A')))
print('A Primeira letra A está na posição {}'.format(tec.find('A') + 1))
print('A Última letra A está na posição {}'.format(tec.rfind('A') + 1))

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente. Ex: Ana Maria de Souza Primeiro = Ana Último = Souza
n = str(input('Escreva o seu Nome Completo: ')).strip()
nome = n.split()  # Split fatia
print('O Primeiro Nome é {}'.format(nome[0]))
print('O Último Nome é {}'.format(nome[len(nome) - 1]))
