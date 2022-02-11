# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente Novamente. ', end='')
# print(f'Você digitou o número {cont[]}')

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre: A) Os 5 primeiros. B) Os últimos 4 colocados. C) Times em ordem alfabética. D) Em que
# posição está o time da Chapecoense.
time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport', 'Vitória',
        'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-' * 30)
print('BRASILEIRÃO 2022')
print('-' * 30)
print(f'Os 5 primeiros times são: {time[0:5]}')
print(f'Os últimos 4 times são: {time[-4:]}')
print(f'Classificação em Ordem Alfabética: {sorted(time)}')
print(f'Chapecoense está na {time.index("Chapecoense")}° posição')

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10),randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números gerados são {n}')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\n O maior valor gerado foi {max(numeros)}')
print(f' O menor valor gerado foi {min(numeros)}')

# Desenvolva um programa que leia quatros valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = (int(input('Digite um Número: '),
     int(input('Digite um Número: '),
     int(input('Digite um Número: '),
     int(input('Digite um Número: '))))))
print(f'Você digitou os valores {n}')
print(f'O número 9 apareceu {n.coun(9)} vezes')
if 3 in n:
    print(f'A posição do número 3 foi {n.index(3)}°')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitas foram ', end=' ')
for num in n:
    if n % 2 ==0:
        print(n, end=' ')

# Crie um programa que tenha uma tupla única com nomes de produto e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Caderno', 10,
            'Estojo', 5.60,
            'Lapis', 3.50)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')

# Crie um programa que tenha uma tupla com várias palavras.
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Aprender', 'Caminhar', 'Chorar', 'Comer')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáãâeéêiou':
            print(letra, end='')