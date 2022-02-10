# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('Olhando o número {} que você informou, o seu antecessor é {} e o seu sucessor é {}'.format(n, a,
                                                                                                  s))  # print('Olhando o número {} que você informou, o seu antecessor é {} e o seu sucessor é {}'.format(n, (n - 1), (n + 1))))

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('Digite um Número: '))
d = numero * 2
t = numero * 3
r = numero ** (1 / 2)
print('Seu número {}, seu dobro é {}, seu triplo é {} e sua raiz é {}'.format(numero, d, t, r))

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Informe sua Primeira Nota: '))
nota2 = float(input('Informe a sua Segunda Nota: '))
media = nota1 + nota2 / 2
print('Sua média é {}'.format(media))

# Escreva um programa que leia um valor em metros e o exiba covertido e o exiba convertido em centimetros e milimetros
medida = float(input('Informe a medida em metros: '))
cm = medida * 100
mm = medida * 1000
print('A conversão de {} metros, resulta em {} centimetros e {} milimetros'.format(medida, cm, mm))

# Faça um programa que leia um número inteiro  qualquer e mostre na tela a sua tabuada
tabuada = int(input('Informe qual a tabuada: '))
n1 = tabuada * 1
n2 = tabuada * 2
n3 = tabuada * 3
n4 = tabuada * 4
n5 = tabuada * 5
n6 = tabuada * 6
n7 = tabuada * 7
n8 = tabuada * 8
n9 = tabuada * 9
n10 = tabuada * 10
print('A tabuada {} é {} {} {} {} {} {} {} {} {} {}'.format(tabuada, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10))

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere que 1 dolar é 3.27 reais
real = float(input('Quanto de dinheiro você tem? $'))
dolar = real / 3.27
print('Com {} reais, você pode comprar {} dolares'.format(real, dolar))

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
larg = float(input('Qual a largura da parade ? '))
alt = float(input('Qual a altura da parade ? '))
area = larg * alt
tinta = area / 2
print('Dimensão da sua parede é {}X{} e sua area é de {}m²'.format(larg, alt, area))
print('Você precisa de {}l de tinta para pintar toda a parede'.format(tinta))

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Informe o valor do produto: $ '))
novo = preco - (preco * 5 / 100)
print('O novo preço do produto é ${}'.format(novo))

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe o seu salário atual: '))
novo = salario + (salario * 15 / 100)
print('Seu novo salário é ${} com aumento de 15%'.format(novo))

# Escreva um programa que converta uma temperatura digitada em °C e convertida para °F
c = float(input('Informe a temperatura em: °C '))
f = ((9 * c) / 5) + 32
print('Temperatura de {}°C corresponde a {}°F'.format(c, f))

# Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
dias = float(input('Quantos dias alugados ? '))
km = float(input('Quantos Km rodados ? '))
pago = (dias * 60) + (km * 0.15)
print('O valor a pagar será R${}'.format(pago))
