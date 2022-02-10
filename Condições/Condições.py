tempo = int(input('Quatos anos tem o seu carro ? '))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')

##########

nome = str(input('Qual o seu nome ? '))
if nome == 'Lucas':
    print('Prazer {}'.format(nome))
else:
    print('Prazer')

##########

n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
m = n1 + n2 / 2
if m >= 6:
    print('A sua Média é {}'.format(m))
    print('Você Passou de Ano')
else:
    print('A sua Média é {}'.format(m))
    print('Você Reprovou')
