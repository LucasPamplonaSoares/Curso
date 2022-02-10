nome = str(input('Qual o seu nome ? '))
if nome == 'Lucas':
    print('Que nome Lindo')
elif nome == 'Vitor' or 'Julia' or 'Maria':
    print('Nome Legal ')
elif nome in 'João Pedro Julia Vitoria':
    print('Belo Nome')
else:
    print('Seu Nome é feio')
print('Prazer em conhece-lo {}'.format(nome))