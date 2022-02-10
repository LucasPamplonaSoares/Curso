# DESAFIOS
# Crie um programa que leia dois números e mostre a soma entre eles
n1 = int(input('Digite um Número: '))
n2 = int(input('Digite um Número: '))
result = n1 + n2
print('A soma entre {} e {} resulto em {}'.format(n1, n2, result))

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
# sobre ele
a = input('Digite algo : ')
print('O tipo primitivo desse valor é : ', type(a))
print('Tem espaços ? ', a.isspace())
print('É um número ? ', a.isnumeric())
print('É alfabético ? ', a.isalpha())
print('É alfonúmerico ? ', a.isalnum())
print('Está em maiúsculo ?  ', a.isupper())
print('Está em minúsculo ? ', a.islower())